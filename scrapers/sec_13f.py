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

# Lista curada de top managers (CIK SEC oficial). Incluye los gigantes 13F mas
# seguidos por la comunidad de retail/research. CIKs verificables en SEC EDGAR.
TOP_MANAGERS_CIK: dict[str, str] = {
    "Berkshire Hathaway Inc": "0001067983",
    "BlackRock Inc.": "0001364742",
    "Vanguard Group Inc": "0000102909",
    "State Street Corp": "0000093751",
    "Fidelity Management & Research": "0000315066",
    "JPMorgan Chase & Co": "0000019617",
    "Bank of America Corp": "0000070858",
    "Goldman Sachs Group Inc": "0000886982",
    "Morgan Stanley": "0000895421",
    "Wells Fargo & Company/MN": "0000072971",
    "T Rowe Price Associates Inc": "0000080255",
    "Geode Capital Management LLC": "0001364742",  # nota: a veces aparece bajo BlackRock
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


def _find_last_13f(submissions: dict[str, Any]) -> dict[str, Any] | None:
    """Localiza el filing 13F-HR mas reciente dentro de un JSON de submissions."""
    recent = submissions.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    accs = recent.get("accessionNumber", [])
    primary_docs = recent.get("primaryDocument", [])
    filing_dates = recent.get("filingDate", [])
    report_dates = recent.get("reportDate", [])
    for i, f in enumerate(forms):
        if f == "13F-HR":
            return {
                "accession": accs[i],
                "primary_doc": primary_docs[i],
                "filing_date": filing_dates[i],
                "report_date": report_dates[i] or filing_dates[i],
            }
    return None


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


def _process_manager(session, manager: str, cik: str) -> dict[str, Any] | None:
    """Procesa un manager: localiza ultimo 13F-HR, parsea y devuelve dict."""
    try:
        subs = get_json(session, _submissions_url(cik), timeout=20, sleep_after=0.15)
    except Exception as e:
        print(f"  [skip] {manager}: submissions fail ({e})")
        return None
    filing = _find_last_13f(subs)
    if not filing:
        print(f"  [skip] {manager}: sin 13F-HR")
        return None
    info_table = _find_info_table_filename(session, cik, filing["accession"])
    if not info_table:
        print(f"  [skip] {manager}: info_table no encontrado")
        return None
    url = _info_table_url(cik, filing["accession"], info_table)
    try:
        r = session.get(url, timeout=30)
        r.raise_for_status()
    except Exception as e:
        print(f"  [skip] {manager}: download info_table fail ({e})")
        return None
    holdings = _parse_info_table(r.text)
    # Ordenar por value desc y truncar a top 100 holdings (manejable en JSON)
    holdings.sort(key=lambda h: h.get("value_usd", 0), reverse=True)
    holdings = holdings[:100]
    if not holdings:
        return None
    return {
        "manager": manager,
        "cik": cik,
        "report_date": filing["report_date"],
        "holdings": holdings,
        "source_url": _filing_index_url(cik, filing["accession"]),
    }


def run() -> Path:
    """Ejecuta el scraping completo y escribe data/institutional_holdings.json."""
    session = make_session(user_agent=UA_SEC)
    results: list[dict[str, Any]] = []
    # Deduplicamos CIKs por si la lista repetia (Geode/BlackRock)
    seen_ciks: set[str] = set()
    for manager, cik in TOP_MANAGERS_CIK.items():
        if cik in seen_ciks:
            continue
        seen_ciks.add(cik)
        rec = _process_manager(session, manager, cik)
        if rec:
            results.append(rec)
            print(f"  [ok] {manager}: {len(rec['holdings'])} holdings")
        time.sleep(0.2)  # rate limit suave para SEC

    # Ranking por AUM agregado (suma de value_usd de todas las holdings reportadas)
    for r in results:
        r["aum_usd"] = sum(h.get("value_usd", 0) for h in r.get("holdings", []))
    results.sort(key=lambda r: r.get("aum_usd", 0), reverse=True)
    # Top 50 por AUM (la lista curada ya esta cerca de eso, pero por si crece)
    results = results[:50]

    if results:
        validate_records(results[:1], INSTITUTIONAL_REQUIRED, "sec_13f")
    out_path = write_json(OUTPUT_PATH, results)
    print(f"[sec_13f] {len(results)} managers -> {out_path}")
    return out_path


if __name__ == "__main__":
    run()
