"""Scraper de trades de congresistas USA (House + Senate).

Fuentes (estado junio 2026):
- Senate: github mirror de timothycarambat (datos pre-parseados, con ticker
  y monto). Buckets S3 originales caidos.
- House: ZIP oficial de disclosures-clerk.house.gov con metadata de PTRs.
  Los detalles (ticker, monto, fecha tx) estan en PDFs separados; aqui
  guardamos solo politico, fecha de filing y url del PDF. Para tickers/monto
  habria que OCR-ear los PDFs (fuera de scope v1).

Ambos endpoints fallan ocasionalmente, asi que cada fuente reporta sus
errores pero no aborta el conjunto.
"""

from __future__ import annotations

import io
import re
import xml.etree.ElementTree as ET
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from normalize.schema import (
    CONGRESS_REQUIRED,
    dedupe_by_key,
    stable_id,
    validate_records,
    write_json,
)
from scrapers._http import get_json, make_session

# Senate via github raw del repo de timothycarambat (autor original del proyecto).
URL_SENATE = "https://raw.githubusercontent.com/timothycarambat/senate-stock-watcher-data/master/aggregate/all_transactions.json"

# House via ZIP oficial del Clerk. Construimos URL para el ano actual + ano anterior.
# Cada ZIP contiene un XML con metadata de todos los filings del ano.
URL_HOUSE_ZIP_TEMPLATE = "https://disclosures-clerk.house.gov/public_disc/financial-pdfs/{year}FD.ZIP"
URL_HOUSE_PTR_PDF_TEMPLATE = "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/{year}/{docid}.pdf"

# Fallback url para senate si github raw cae
URL_HOUSE = URL_HOUSE_ZIP_TEMPLATE.format(year=datetime.now(timezone.utc).year)

OUTPUT_PATH = Path(__file__).resolve().parents[1] / "data" / "public" / "congress_trades_30d.json"

# Mapeo de tipos de transaccion crudos a categorias canonicas.
TX_TYPE_MAP = {
    "purchase": "purchase",
    "p": "purchase",
    "sale_full": "sale",
    "sale_partial": "sale",
    "sale (full)": "sale",
    "sale (partial)": "sale",
    "sale": "sale",
    "s": "sale",
    "exchange": "exchange",
    "e": "exchange",
}


def _norm_tx_type(raw: str | None) -> str:
    """Normaliza el tipo de transaccion al set canonico {purchase, sale, exchange, other}."""
    if not raw:
        return "other"
    key = str(raw).strip().lower()
    return TX_TYPE_MAP.get(key, "other")


# Valores que NUNCA son tickers validos (contaminaban el ranking, ej "PDF").
INVALID_TICKERS = {"", "--", "N/A", "NONE", "PDF", "N", "A", "THE", "INC", "LLC",
                   "CORP", "CO", "LTD", "ETF", "FUND", "TRUST", "COM", "CLASS"}

# Patrones explicitos de ticker dentro de una descripcion de activo.
# Solo aceptamos ticker si aparece de forma inequivoca, no por regex bruto.
_TICKER_PATTERNS = [
    re.compile(r"\(([A-Z]{1,5})\)"),              # "NVIDIA Corporation (NVDA)"
    re.compile(r"\b(?:NASDAQ|NYSE|NYSEARCA|AMEX|BATS)\s*:\s*([A-Z]{1,5})\b"),  # "NASDAQ: NVDA"
]


def _clean_ticker(raw: str | None) -> str:
    """Limpia un ticker explicito: uppercase, sin '$', sin basura.

    Devuelve '' si el valor esta en INVALID_TICKERS o no parece un ticker.
    """
    if not raw:
        return ""
    t = str(raw).strip().upper().lstrip("$").split()[0] if str(raw).strip() else ""
    if t in INVALID_TICKERS:
        return ""
    return t


def _extract_ticker(raw_ticker: str | None, asset_description: str | None) -> tuple[str, str, float]:
    """Resuelve (ticker, ticker_source, ticker_confidence) sin inventar tickers.

    Prioridad:
    1. Campo ticker explicito de la fuente -> confidence 0.98.
    2. Patron explicito en la descripcion '(NVDA)' o 'NASDAQ: NVDA' -> 0.9.
    3. Nada (NO se hace regex bruto de mayusculas) -> '' confidence 0.

    Esto elimina el bug del ticker falso 'PDF' que venia de extraer las
    primeras letras mayusculas de descripciones sin ticker real.
    """
    t = _clean_ticker(raw_ticker)
    if t:
        return t, "source_field", 0.98
    desc = asset_description or ""
    for pat in _TICKER_PATTERNS:
        m = pat.search(desc)
        if m:
            cand = _clean_ticker(m.group(1))
            if cand:
                return cand, "description_pattern", 0.9
    return "", "none", 0.0


def _parse_house_xml(xml_text: str, year: int) -> list[dict[str, Any]]:
    """Parsea el XML del ZIP del Clerk y devuelve filings tipo PTR (Periodic Tx Report).

    El XML tiene estructura <FinancialDisclosure><Member>... con campos
    Prefix, Last, First, Suffix, FilingType, StateDst, Year, FilingDate, DocID.
    Solo nos quedamos con FilingType='P' (PTR). Como un PTR puede tener
    decenas de transacciones que solo estan en el PDF, generamos UN registro
    por filing con ticker/amount/tx_type vacios y enlace al PDF.
    """
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []
    out: list[dict[str, Any]] = []
    for member in root.iter("Member"):
        def _t(tag: str) -> str:
            el = member.find(tag)
            return (el.text or "").strip() if (el is not None and el.text) else ""

        filing_type = _t("FilingType")
        # 'P' = Periodic Transaction Report (compras/ventas). Otros tipos:
        # A=Annual, X=Extension, etc. Filtramos solo P.
        if filing_type != "P":
            continue
        first = _t("First")
        last = _t("Last")
        suffix = _t("Suffix")
        politician = " ".join(p for p in (first, last, suffix) if p).strip()
        if not politician:
            continue
        filing_date = _t("FilingDate")  # formato M/D/YYYY
        doc_id = _t("DocID")
        # state_dst no es sigla de partido, pero util. Partido no esta en este XML.
        rec_id = stable_id("house", politician, doc_id, filing_date)
        pdf_url = URL_HOUSE_PTR_PDF_TEMPLATE.format(year=year, docid=doc_id) if doc_id else URL_HOUSE_ZIP_TEMPLATE.format(year=year)
        out.append({
            "id": rec_id,
            "politician": politician,
            "chamber": "house",
            "party": "",  # no esta en el XML del Clerk
            "ticker": "",  # no esta en metadata, solo en PDF
            "asset_name": "",
            "tx_type": "ptr",  # marcador: filing PTR, ver PDF para detalles
            "amount_range": "",
            "tx_date": "",
            "disclosure_date": filing_date,
            "source_url": pdf_url,
        })
    return out


def _to_record_house(raw: dict[str, Any]) -> dict[str, Any] | None:
    """[Legacy] Convierte registros del antiguo formato S3 house-stock-watcher.

    Se mantiene por si en el futuro se restaura el bucket, o si alguien
    sirve datos en el mismo formato. No se usa en run() actual.
    """
    politician = raw.get("representative") or raw.get("politician") or ""
    ticker = _clean_ticker(raw.get("ticker"))
    tx_date = raw.get("transaction_date") or raw.get("tx_date") or ""
    disclosure_date = raw.get("disclosure_date") or ""
    tx_type = _norm_tx_type(raw.get("type"))
    amount = raw.get("amount") or ""

    if not politician or not tx_date:
        return None

    rec_id = stable_id(politician, ticker, tx_date, amount, tx_type)
    return {
        "id": rec_id,
        "politician": politician.strip(),
        "chamber": "house",
        "party": (raw.get("party") or "").strip()[:1] or "",
        "ticker": ticker,
        "asset_name": (raw.get("asset_description") or "").strip(),
        "tx_type": tx_type,
        "amount_range": amount,
        "tx_date": tx_date,
        "disclosure_date": disclosure_date,
        "source_url": raw.get("ptr_link") or URL_HOUSE,
    }


def _to_record_senate(raw: dict[str, Any]) -> dict[str, Any] | None:
    """Convierte un registro crudo del Senate dataset al schema canonico.

    El dataset del Senate usa otras claves: senator, transaction_date, asset_type,
    asset_description, type, amount, comment, ptr_link.
    """
    politician = (
        raw.get("senator")
        or raw.get("politician")
        or raw.get("first_name", "") + " " + raw.get("last_name", "")
    ).strip()
    # Resolucion de ticker sin regex bruto (arregla el bug del ticker falso 'PDF').
    ticker, ticker_source, ticker_confidence = _extract_ticker(
        raw.get("ticker"), raw.get("asset_description")
    )
    tx_date = raw.get("transaction_date") or raw.get("tx_date") or ""
    disclosure_date = raw.get("disclosure_date") or raw.get("date_received") or ""
    tx_type = _norm_tx_type(raw.get("type") or raw.get("transaction_type"))
    amount = raw.get("amount") or raw.get("amount_range") or ""

    if not politician or not tx_date:
        return None

    rec_id = stable_id(politician, ticker, tx_date, amount, tx_type)
    return {
        "ticker_source": ticker_source,
        "ticker_confidence": ticker_confidence,
        "id": rec_id,
        "politician": politician,
        "chamber": "senate",
        "party": (raw.get("party") or "").strip()[:1] or "",
        "ticker": ticker,
        "asset_name": (raw.get("asset_description") or "").strip(),
        "tx_type": tx_type,
        "amount_range": amount,
        "tx_date": tx_date,
        "disclosure_date": disclosure_date,
        "source_url": raw.get("ptr_link") or URL_SENATE,
    }


def fetch_house(session) -> list[dict[str, Any]]:
    """Descarga el ZIP del Clerk del ano actual + ano anterior y parsea PTRs.

    El XML del ZIP contiene solo metadata. Los detalles estan en PDFs.
    Aqui generamos un registro por filing PTR con campos vacios.
    """
    out: list[dict[str, Any]] = []
    now = datetime.now(timezone.utc)
    years_to_try = [now.year, now.year - 1]
    for year in years_to_try:
        url = URL_HOUSE_ZIP_TEMPLATE.format(year=year)
        try:
            r = session.get(url, timeout=60)
            r.raise_for_status()
        except Exception as e:
            print(f"  [house] {year}: download fail ({e})")
            continue
        try:
            zf = zipfile.ZipFile(io.BytesIO(r.content))
        except zipfile.BadZipFile:
            print(f"  [house] {year}: ZIP corrupto")
            continue
        # El XML dentro suele llamarse 2026FD.xml. Tomamos el primer XML.
        xml_name = next((n for n in zf.namelist() if n.lower().endswith(".xml")), None)
        if not xml_name:
            print(f"  [house] {year}: sin XML en ZIP")
            continue
        xml_text = zf.read(xml_name).decode("utf-8", errors="replace")
        records = _parse_house_xml(xml_text, year)
        print(f"  [house] {year}: {len(records)} PTR filings")
        out.extend(records)
    return out


def fetch_senate(session) -> list[dict[str, Any]]:
    """Descarga y normaliza el dataset del Senado desde el mirror github."""
    raw = get_json(session, URL_SENATE, timeout=120)
    out = [r for r in (_to_record_senate(x) for x in raw) if r]
    return out


def run() -> Path:
    """Ejecuta el scraping completo, deduplica y escribe data/congress_trades.json."""
    session = make_session()
    house = fetch_house(session)
    senate = fetch_senate(session)
    merged = dedupe_by_key(house + senate, key="id")
    # Ordenar por fecha desc para que el JSON sea legible y el dashboard muestre lo reciente.
    merged.sort(key=lambda r: r.get("tx_date", ""), reverse=True)
    validate_records(merged[:1], CONGRESS_REQUIRED, "congress")
    out_path = write_json(OUTPUT_PATH, merged)
    print(f"[congress] {len(house)} house + {len(senate)} senate -> {len(merged)} unicos -> {out_path}")
    return out_path


if __name__ == "__main__":
    run()
