"""Scraper de SEC Insider Trades (Forms 3/4/5) via EDGAR full-text search.

Estrategia:
1. Hace una busqueda full-text en EDGAR filtrando form=4 en los ultimos 30 dias.
   La API es publica, devuelve metadata paginada (max 100 por pagina).
2. Por cada filing, descarga el XML del Form 4 (campo 'primary_doc') y extrae
   las transacciones (insider, titulo, ticker, tx_type, shares, price, fecha).

SEC requiere User-Agent con email valido y limita a ~10 req/s.
Para no excedernos, limitamos a ~5 req/s y a un maximo de filings configurable.
"""

from __future__ import annotations

import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterator

from normalize.schema import (
    INSIDER_REQUIRED,
    dedupe_by_key,
    validate_records,
    write_json,
)
from scrapers._http import UA_SEC, get_json, make_session

# Endpoints publicos
EDGAR_SEARCH = "https://efts.sec.gov/LATEST/search-index"
EDGAR_ARCHIVES = "https://www.sec.gov/Archives/edgar/data"

OUTPUT_PATH = Path(__file__).resolve().parents[1] / "data" / "public" / "sec_insiders_30d.json"

# Limites operativos: 30 dias de ventana y un cap razonable para no tardar horas.
DEFAULT_DAYS = 30
MAX_FILINGS = 400        # cap de filings a parsear por ejecucion
PAGE_SIZE = 100

# Codigos de transaccion de Form 4 mapeados a etiquetas legibles.
# Spec: https://www.sec.gov/files/forms-3-4-5.pdf
TX_CODE_MAP = {
    "P": "P-Purchase",
    "S": "S-Sale",
    "A": "A-Grant",
    "D": "D-Disposition",
    "F": "F-PaymentByShares",
    "I": "I-DiscretionaryTx",
    "M": "M-OptionExercise",
    "C": "C-ConvDerivative",
    "G": "G-Gift",
    "X": "X-OptionExercise",
    "V": "V-VoluntaryDisclosure",
    "J": "J-Other",
    "K": "K-EquitySwap",
    "U": "U-TenderResponse",
    "W": "W-Inheritance",
}


def _date_range(days: int) -> tuple[str, str]:
    """Devuelve (startdt, enddt) en formato YYYY-MM-DD para los ultimos N dias."""
    end = datetime.now(timezone.utc).date()
    start = end - timedelta(days=days)
    return start.isoformat(), end.isoformat()


def _search_filings(session, days: int, max_filings: int) -> Iterator[dict[str, Any]]:
    """Itera metadata de filings Form 4 publicados en los ultimos `days` dias."""
    startdt, enddt = _date_range(days)
    fetched = 0
    page_from = 0
    while fetched < max_filings:
        params = {
            "q": "",
            "dateRange": "custom",
            "startdt": startdt,
            "enddt": enddt,
            "forms": "4",
            "from": page_from,
        }
        data = get_json(session, EDGAR_SEARCH, params=params, timeout=30, sleep_after=0.2)
        hits = (data.get("hits", {}) or {}).get("hits", [])
        if not hits:
            break
        for h in hits:
            yield h
            fetched += 1
            if fetched >= max_filings:
                return
        page_from += PAGE_SIZE


def _accession_from_id(hit_id: str) -> str:
    """Extrae el accession number normalizado del campo _id del hit.

    El _id viene como '0001209191-25-079821:wf-form4.xml' o similar. Lo dejamos
    en formato con guiones ya que es lo que la URL espera.
    """
    return hit_id.split(":", 1)[0]


def _filing_doc_url(cik: str, accession: str, primary_doc: str) -> str:
    """Construye la URL del XML del Form 4 dentro del directorio del filing."""
    acc_nodash = accession.replace("-", "")
    return f"{EDGAR_ARCHIVES}/{int(cik)}/{acc_nodash}/{primary_doc}"


def _text(elem: ET.Element | None, path: str, default: str = "") -> str:
    """Extrae texto de un subelemento; devuelve default si no existe."""
    if elem is None:
        return default
    found = elem.find(path)
    if found is None or found.text is None:
        return default
    return found.text.strip()


def _parse_form4_xml(xml_text: str) -> dict[str, Any] | None:
    """Parsea un XML de Form 4 y devuelve dict con campos clave o None si falla.

    Devuelve:
      issuer_name, issuer_ticker, insider_name, insider_title (Officer/Director/...),
      transactions: lista de dicts con tx_date, tx_code, shares, price.
    """
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return None

    issuer = root.find("issuer")
    company = _text(issuer, "issuerName")
    ticker = _text(issuer, "issuerTradingSymbol")

    rep_owner = root.find("reportingOwner")
    insider_name = _text(rep_owner, "reportingOwnerId/rptOwnerName")

    # Titulo: combinamos Director / Officer + officerTitle / TenPercentOwner
    rel = rep_owner.find("reportingOwnerRelationship") if rep_owner is not None else None
    titles: list[str] = []
    if rel is not None:
        if _text(rel, "isDirector") in {"1", "true"}:
            titles.append("Director")
        if _text(rel, "isOfficer") in {"1", "true"}:
            ot = _text(rel, "officerTitle")
            titles.append(ot or "Officer")
        if _text(rel, "isTenPercentOwner") in {"1", "true"}:
            titles.append("10%-Owner")
        if _text(rel, "isOther") in {"1", "true"}:
            titles.append("Other")
    title = ", ".join(titles) or "Insider"

    transactions: list[dict[str, Any]] = []
    # Non-derivative tx: <nonDerivativeTransaction>
    for tx in root.iter("nonDerivativeTransaction"):
        tx_date = _text(tx, "transactionDate/value")
        amounts = tx.find("transactionAmounts")
        coding = tx.find("transactionCoding")
        tx_code_raw = _text(coding, "transactionCode")
        shares = _text(amounts, "transactionShares/value")
        price = _text(amounts, "transactionPricePerShare/value")
        transactions.append({
            "tx_date": tx_date,
            "tx_code": tx_code_raw,
            "shares": shares,
            "price": price,
        })

    return {
        "company": company,
        "ticker": ticker.upper() if ticker else "",
        "insider_name": insider_name,
        "insider_title": title,
        "transactions": transactions,
    }


def _to_records(hit: dict[str, Any], parsed: dict[str, Any]) -> list[dict[str, Any]]:
    """Convierte el parseo de un Form 4 en N registros (uno por transaccion)."""
    accession = _accession_from_id(hit.get("_id", ""))
    source = hit.get("_source", {})
    cik_list = source.get("ciks", []) or []
    cik = cik_list[0] if cik_list else ""
    primary_doc = (source.get("display_names") or [""])[0]  # fallback no usado
    # source_url del filing entero (mas amigable que apuntar al XML crudo)
    if cik and accession:
        acc_nodash = accession.replace("-", "")
        source_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={int(cik)}&type=4&dateb=&owner=include&action=getcompany&accession_number={accession}"
        source_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc_nodash}/"
    else:
        source_url = "https://www.sec.gov/cgi-bin/browse-edgar"

    out: list[dict[str, Any]] = []
    for i, tx in enumerate(parsed.get("transactions", []) or []):
        tx_code = tx.get("tx_code") or ""
        try:
            shares = float(tx.get("shares") or 0)  # mantener float para .is_integer()
        except ValueError:
            shares = 0.0
        try:
            price = float(tx.get("price") or 0)
        except ValueError:
            price = 0.0
        value_usd = round(shares * price, 2)
        out.append({
            "id": f"{accession}-{i}",
            "insider_name": parsed.get("insider_name") or "",
            "insider_title": parsed.get("insider_title") or "Insider",
            "company": parsed.get("company") or "",
            "ticker": parsed.get("ticker") or "",
            "tx_code": tx_code,
            "tx_type": TX_CODE_MAP.get(tx_code, tx_code or "Unknown"),
            "shares": int(shares) if shares.is_integer() else shares,
            "price_per_share": price,
            "value_usd": value_usd,
            "tx_date": tx.get("tx_date") or "",
            "source_url": source_url,
        })
    return out


def run(days: int = DEFAULT_DAYS, max_filings: int = MAX_FILINGS) -> Path:
    """Ejecuta el scraping completo y escribe data/insider_trades.json."""
    session = make_session(user_agent=UA_SEC)
    all_records: list[dict[str, Any]] = []
    parsed_filings = 0
    parse_errors = 0

    for hit in _search_filings(session, days=days, max_filings=max_filings):
        src = hit.get("_source", {})
        ciks = src.get("ciks", [])
        if not ciks:
            continue
        accession = _accession_from_id(hit.get("_id", ""))
        # Documento primario: 'xsl' lo ignoramos, usamos el campo 'primary_doc' del search.
        # En search-index el campo se llama 'file_type' a veces; fallback robusto:
        files = src.get("primary_doc_description") or src.get("file_type") or ""
        # Heuristica: en el hit _id viene 'accession:doc.xml'
        doc_part = hit.get("_id", "").split(":", 1)
        primary_doc = doc_part[1] if len(doc_part) == 2 else ""
        if not primary_doc.endswith(".xml"):
            # No es el XML estructurado, skip
            continue
        url = _filing_doc_url(ciks[0], accession, primary_doc)
        try:
            r = session.get(url, timeout=20)
            if r.status_code != 200:
                continue
            parsed = _parse_form4_xml(r.text)
        except Exception:
            parse_errors += 1
            continue
        if not parsed:
            parse_errors += 1
            continue
        parsed_filings += 1
        all_records.extend(_to_records(hit, parsed))
        # Rate limit suave: ~5 req/s
        time.sleep(0.2)

    deduped = dedupe_by_key(all_records, key="id")
    # Ordenar por fecha descendente
    deduped.sort(key=lambda r: r.get("tx_date", ""), reverse=True)
    if deduped:
        validate_records(deduped[:1], INSIDER_REQUIRED, "sec_insider")
    out_path = write_json(OUTPUT_PATH, deduped)
    print(
        f"[sec_insider] {parsed_filings} filings parseados, {parse_errors} errores, "
        f"{len(deduped)} transacciones unicas -> {out_path}"
    )
    return out_path


if __name__ == "__main__":
    run()
