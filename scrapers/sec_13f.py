"""Scraper de 13F-HR holdings via SEC EDGAR.

Estrategia:
1. Tomamos una lista curada de top managers institucionales (CIK conocidos).
2. Para cada CIK consultamos data.sec.gov/submissions/CIK###.json y buscamos
   el ultimo filing 13F-HR.
3. Descargamos el information table del filing (formato XML) y extraemos
   ticker (cuando se conoce), nombre, CUSIP, shares, value_usd.
4. Top 50 managers por AUM agregado de todas sus holdings.

CUSIP -> ticker resolution: SEC no expone el ticker en el information table,
solo el nameOfIssuer. Hacemos best-effort: si el filing trae una tabla con
ticker propio se usa; si no, dejamos `ticker` vacio y la `asset_name` actua
como identificador. El dashboard puede mapear despues.
"""

from __future__ import annotations

import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from normalize.schema import (
    INSTITUTIONAL_REQUIRED,
    validate_records,
    write_json,
)
from scrapers._http import UA_SEC, get_json, make_session

OUTPUT_PATH = Path(__file__).resolve().parents[1] / "data" / "public" / "institutional_holdings_latest.json"
CHANGES_PATH = Path(__file__).resolve().parents[1] / "data" / "public" / "institutional_changes_latest.json"

# Lista curada de top managers (CIK SEC oficial). Incluye los gigantes 13F mas
# seguidos por la comunidad de retail/research. CIKs verificables en SEC EDGAR.
TOP_MANAGERS_CIK: dict[str, str] = {
    "Berkshire Hathaway Inc": "0001067983",
    "BlackRock Inc.": "0001086364",  # filer 13F real (no 0001364742 = BlackRock Finance, obsoleto)
    "Vanguard Group Inc": "0000102909",
    "State Street Corp": "0000093751",
    "Fidelity Management & Research": "0000315066",
    "JPMorgan Chase & Co": "0000019617",
    "Bank of America Corp": "0000070858",
    "Goldman Sachs Group Inc": "0000886982",
    "Morgan Stanley": "0000895421",
    "Wells Fargo & Company/MN": "0000072971",
    "T Rowe Price Associates Inc": "0000080255",
    "Geode Capital Management LLC": "0001214717",
    "Northern Trust Corp": "0000073124",
    "Wellington Management Group LLP": "0000902219",
    "Capital Research Global Investors": "0001262017",
    "Renaissance Technologies LLC": "0001037389",
    "Citadel Advisors LLC": "0001423053",
    "Two Sigma Investments LP": "0001179392",
    "D.E. Shaw & Co Inc": "0001009207",
    "Bridgewater Associates LP": "0001350694",
    "Millennium Management LLC": "0001273087",
    "Point72 Asset Management LP": "0001603466",
    "Tiger Global Management LLC": "0001167483",
    "Soros Fund Management LLC": "0001029160",
    "Pershing Square Capital Management LP": "0001336528",
    "Third Point LLC": "0001040273",
    "Coatue Management LLC": "0001135730",
    "Lone Pine Capital LLC": "0001061165",
    "Viking Global Investors LP": "0001103804",
    "Appaloosa LP": "0001656456",
    "Greenlight Capital Inc": "0001079114",
    "Pershing Square Holdings Ltd": "0001336528",
    "Baupost Group LLC": "0001061768",
    "Sequoia Capital": "0001050737",
    "ARK Investment Management LLC": "0001697748",
    "Invesco Ltd": "0000914208",
    "Franklin Resources Inc": "0000038777",
    "Affiliated Managers Group Inc": "0001004434",
    "Charles Schwab Investment Management": "0000883965",
    "PNC Financial Services Group Inc": "0000713676",
    "Bank Of New York Mellon Corp": "0001390777",
    "UBS Group AG": "0001114446",
    "Credit Suisse AG": "0000824468",
    "Deutsche Bank AG": "0001159508",
    "Royal Bank Of Canada": "0001000275",
    "TD Asset Management Inc": "0001271991",
    "Mitsubishi UFJ Financial Group": "0001260221",
    "Nomura Holdings Inc": "0001163653",
    "Hudson Bay Capital Management LP": "0001327068",
    "Balyasny Asset Management LLC": "0001162950",
    "Marshall Wace LLP": "0001719406",
}


def _submissions_url(cik: str) -> str:
    """URL del JSON de submissions de un CIK (zero-padded a 10 digitos)."""
    cik10 = str(int(cik)).zfill(10)
    return f"https://data.sec.gov/submissions/CIK{cik10}.json"


def _find_13f_filings(submissions: dict[str, Any]) -> list[dict[str, Any]]:
    """Devuelve TODOS los 13F-HR (y amendments /A) ordenados por reportDate desc.

    Cada elemento: {accession, primary_doc, filing_date, report_date, is_amendment}.
    Trabajar por reportDate (periodOfReport) permite emparejar quarters y detectar
    managers que se han quedado atras, en vez de coger ciegamente el ultimo filing.
    """
    recent = submissions.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    accs = recent.get("accessionNumber", [])
    primary_docs = recent.get("primaryDocument", [])
    filing_dates = recent.get("filingDate", [])
    report_dates = recent.get("reportDate", [])
    out: list[dict[str, Any]] = []
    for i, f in enumerate(forms):
        if f.startswith("13F-HR"):  # incluye '13F-HR' y '13F-HR/A'
            out.append({
                "accession": accs[i],
                "primary_doc": primary_docs[i],
                "filing_date": filing_dates[i],
                "report_date": report_dates[i] or filing_dates[i],
                "is_amendment": f.endswith("/A"),
            })
    out.sort(key=lambda x: x["report_date"], reverse=True)
    return out


def _filing_index_url(cik: str, accession: str) -> str:
    """URL del listado de archivos del filing (index.json del directorio)."""
    cik_int = int(cik)
    acc_nodash = accession.replace("-", "")
    return f"https://www.sec.gov/Archives/edgar/data/{cik_int}/{acc_nodash}/"


def _info_table_url(cik: str, accession: str, info_table_filename: str) -> str:
    """URL del informationTable.xml dentro del filing."""
    return _filing_index_url(cik, accession) + info_table_filename


def _find_info_table_filename(session, cik: str, accession: str) -> str | None:
    """Lista el directorio del filing y devuelve el nombre del information table XML."""
    url = _filing_index_url(cik, accession) + "index.json"
    try:
        data = get_json(session, url, timeout=20, sleep_after=0.15)
    except Exception:
        return None
    items = (data.get("directory", {}) or {}).get("item", []) or []
    # Heuristica: archivo XML cuyo nombre contiene 'infotable' / 'information' o un patron NPORT
    for it in items:
        name = it.get("name", "")
        low = name.lower()
        if low.endswith(".xml") and ("infotable" in low or "informationtable" in low or "info_table" in low):
            return name
    # Fallback: cualquier XML que no sea el primary_doc (que suele ser el cover)
    for it in items:
        name = it.get("name", "")
        if name.lower().endswith(".xml") and "primary_doc" not in name.lower():
            return name
    return None


def _strip_ns(tag: str) -> str:
    """Quita namespace XML para que find/iter sean mas comodos."""
    return tag.split("}", 1)[-1] if "}" in tag else tag


def _parse_info_table(xml_text: str) -> list[dict[str, Any]]:
    """Parsea el information table XML y devuelve lista de holdings."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []
    holdings: list[dict[str, Any]] = []
    for info in root.iter():
        if _strip_ns(info.tag) != "infoTable":
            continue
        name = ""
        cusip = ""
        value = 0
        shares = 0
        for child in info:
            tag = _strip_ns(child.tag)
            if tag == "nameOfIssuer":
                name = (child.text or "").strip()
            elif tag == "cusip":
                cusip = (child.text or "").strip()
            elif tag == "value":
                # Pre-2022 era en miles, post-2022 en dolares. Asumimos dolares.
                # Si el valor parece "miles" (issuer claims X * 1000), no podemos
                # detectarlo sin la cover. Best effort: dejamos como esta.
                try:
                    value = int(float(child.text or 0))
                except ValueError:
                    value = 0
            elif tag == "shrsOrPrnAmt":
                for sub in child:
                    if _strip_ns(sub.tag) == "sshPrnamt":
                        try:
                            shares = int(float(sub.text or 0))
                        except ValueError:
                            shares = 0
        if name:
            holdings.append({
                "asset_name": name,
                "cusip": cusip,
                "ticker": "",  # no esta en info_table, lo dejamos vacio
                "shares": shares,
                "value_usd": value,
            })
    return holdings


def _quarter_of(report_date: str) -> str:
    """Convierte un reportDate ISO (YYYY-MM-DD) a quarter 'YYYYQX'."""
    try:
        y, m, _ = report_date.split("-")
        q = (int(m) - 1) // 3 + 1
        return f"{y}Q{q}"
    except (ValueError, AttributeError):
        return "?"


def _fetch_holdings(session, cik: str, filing: dict[str, Any]) -> list[dict[str, Any]]:
    """Descarga y parsea el information table de un filing concreto. Top 100 por valor."""
    info_table = _find_info_table_filename(session, cik, filing["accession"])
    if not info_table:
        return []
    url = _info_table_url(cik, filing["accession"], info_table)
    try:
        r = session.get(url, timeout=30)
        r.raise_for_status()
    except Exception:
        return []
    holdings = _parse_info_table(r.text)
    holdings.sort(key=lambda h: h.get("value_usd", 0), reverse=True)
    return holdings[:100]


def _process_manager(session, manager: str, cik: str) -> dict[str, Any] | None:
    """Procesa un manager por QUARTER: coge el 13F mas reciente + el anterior.

    Devuelve dict con holdings actuales, holdings previos (para changes),
    quarter, report_date, is_amendment y la metadata necesaria.
    """
    try:
        subs = get_json(session, _submissions_url(cik), timeout=20, sleep_after=0.15)
    except Exception as e:
        print(f"  [skip] {manager}: submissions fail ({e})")
        return None
    filings = _find_13f_filings(subs)
    if not filings:
        print(f"  [skip] {manager}: sin 13F-HR")
        return None

    current = filings[0]
    # Previous = primer filing con reportDate distinto al actual (quarter anterior).
    previous = next((f for f in filings[1:] if f["report_date"] != current["report_date"]), None)

    current_holdings = _fetch_holdings(session, cik, current)
    if not current_holdings:
        print(f"  [skip] {manager}: info_table actual vacio")
        return None
    time.sleep(0.15)
    previous_holdings = _fetch_holdings(session, cik, previous) if previous else []

    return {
        "manager": manager,
        "cik": cik,
        "report_date": current["report_date"],
        "filing_date": current["filing_date"],
        "quarter": _quarter_of(current["report_date"]),
        "is_amendment": current["is_amendment"],
        "holdings": current_holdings,
        "aum_usd": sum(h.get("value_usd", 0) for h in current_holdings),
        "source_url": _filing_index_url(cik, current["accession"]),
        "_previous_report_date": previous["report_date"] if previous else None,
        "_previous_holdings": previous_holdings,
    }


def _compute_changes(rec: dict[str, Any]) -> list[dict[str, Any]]:
    """Calcula cambios por posicion entre el quarter actual y el anterior.

    Empareja por CUSIP (fallback asset_name). Marca direction:
    new / increased / decreased / exited.
    """
    prev = rec.get("_previous_holdings") or []
    if not prev:
        return []
    cur = rec.get("holdings", [])

    def key(h):
        return h.get("cusip") or h.get("asset_name")

    prev_map = {key(h): h for h in prev}
    cur_map = {key(h): h for h in cur}
    changes: list[dict[str, Any]] = []

    for k, ch in cur_map.items():
        pv = prev_map.get(k, {}).get("value_usd", 0)
        cv = ch.get("value_usd", 0)
        if pv == 0 and cv == 0:
            continue
        delta = cv - pv
        direction = "new" if pv == 0 else ("increased" if delta > 0 else
                                           ("decreased" if delta < 0 else "held"))
        changes.append({
            "manager": rec["manager"],
            "ticker": ch.get("ticker", ""),
            "asset_name": ch.get("asset_name", ""),
            "cusip": ch.get("cusip", ""),
            "prev_value_usd": pv,
            "current_value_usd": cv,
            "change_value_usd": delta,
            "change_pct": round(delta / pv, 4) if pv else None,
            "direction": direction,
            "quarter": rec["quarter"],
        })
    # Posiciones que desaparecieron (exited)
    for k, ph in prev_map.items():
        if k not in cur_map and ph.get("value_usd", 0) > 0:
            changes.append({
                "manager": rec["manager"],
                "ticker": ph.get("ticker", ""),
                "asset_name": ph.get("asset_name", ""),
                "cusip": ph.get("cusip", ""),
                "prev_value_usd": ph.get("value_usd", 0),
                "current_value_usd": 0,
                "change_value_usd": -ph.get("value_usd", 0),
                "change_pct": -1.0,
                "direction": "exited",
                "quarter": rec["quarter"],
            })
    return changes


def run() -> Path:
    """Procesa todos los managers por quarter y escribe holdings + changes.

    Determina el quarter de CONSENSO (el reportDate mas reciente entre todos)
    y marca como stale a los managers que se han quedado atras. Esto se adapta
    al ritmo real de publicacion de la SEC (los datos van por detras del reloj).
    """
    session = make_session(user_agent=UA_SEC)
    results: list[dict[str, Any]] = []
    seen_ciks: set[str] = set()
    for manager, cik in TOP_MANAGERS_CIK.items():
        if cik in seen_ciks:
            continue
        seen_ciks.add(cik)
        rec = _process_manager(session, manager, cik)
        if rec:
            results.append(rec)
            print(f"  [ok] {manager}: {len(rec['holdings'])} holdings ({rec['quarter']})")
        time.sleep(0.2)

    if not results:
        write_json(OUTPUT_PATH, [])
        return OUTPUT_PATH

    # Quarter de consenso = reportDate mas reciente visto.
    consensus = max(r["report_date"] for r in results)
    consensus_q = _quarter_of(consensus)

    # Descartar managers severamente stale (>366d tras el consenso): suelen ser
    # CIKs defuntos o equivocados (ej una entidad BlackRock parada en 2016) y su
    # data es engañosa. Los moderadamente atrasados (1-2 quarters) si se conservan.
    from datetime import date
    def _days_behind(rd: str) -> int:
        try:
            cy, cm, cd = map(int, consensus.split("-"))
            ry, rm, rd_ = map(int, rd.split("-"))
            return (date(cy, cm, cd) - date(ry, rm, rd_)).days
        except ValueError:
            return 0
    dropped = [r["manager"] for r in results if _days_behind(r["report_date"]) > 366]
    if dropped:
        print(f"  [drop] managers obsoletos (>366d): {dropped}")
    results = [r for r in results if _days_behind(r["report_date"]) <= 366]

    # Construir changes (Q vs Q-1) y marcar stale.
    all_changes: list[dict[str, Any]] = []
    for r in results:
        r["is_current_quarter"] = (r["report_date"] == consensus)
        r["is_stale"] = (r["report_date"] < consensus)
        all_changes.extend(_compute_changes(r))
        # Limpiar campos internos antes de serializar.
        r.pop("_previous_holdings", None)

    results.sort(key=lambda r: r.get("aum_usd", 0), reverse=True)
    results = results[:50]

    # Top changes por magnitud absoluta de cambio.
    all_changes.sort(key=lambda c: abs(c.get("change_value_usd", 0)), reverse=True)

    if results:
        validate_records(results[:1], INSTITUTIONAL_REQUIRED, "sec_13f")
    write_json(OUTPUT_PATH, results)
    write_json(CHANGES_PATH, all_changes[:500])

    stale = sum(1 for r in results if r.get("is_stale"))
    print(
        f"[sec_13f] {len(results)} managers, quarter consenso {consensus_q}, "
        f"{stale} stale, {len(all_changes)} cambios -> {OUTPUT_PATH.parent}"
    )
    return OUTPUT_PATH


if __name__ == "__main__":
    run()
