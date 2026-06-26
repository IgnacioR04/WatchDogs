"""Descarga y parseo de los datasets bulk trimestrales de la SEC.

Para el backfill historico de insiders, descargar millones de Forms 4 uno a uno
es inviable. La SEC publica datasets trimestrales estructurados (un ZIP por
quarter con TSVs) que contienen TODAS las transacciones de insiders del periodo:

    https://www.sec.gov/files/structureddata/data/insider-transactions-data-sets/{year}q{q}_form345.zip

El ZIP trae varias TSV. Para reconstruir cada transaccion hacemos join por
ACCESSION_NUMBER de:
- SUBMISSION.tsv      -> filing_date (known_date), issuer, ticker, document_type
- REPORTINGOWNER.tsv  -> nombre del insider y su relacion (cargo)
- NONDERIV_TRANS.tsv  -> transaccion (fecha=event_date, codigo, shares, precio)

Esto permite backfillear anos de insiders con una descarga por quarter.
"""

from __future__ import annotations

import csv
import io
import zipfile
from datetime import datetime
from typing import Any

from normalize.schema import temporal_block
from scrapers._http import Client, UA_SEC

INSIDER_ZIP_URL = (
    "https://www.sec.gov/files/structureddata/data/insider-transactions-data-sets/"
    "{year}q{q}_form345.zip"
)

# Mapeo de codigos de transaccion a etiqueta legible (igual que sec_insider).
TX_CODE_MAP = {
    "P": "P-Purchase", "S": "S-Sale", "A": "A-Grant", "D": "D-Disposition",
    "F": "F-PaymentByShares", "M": "M-OptionExercise", "G": "G-Gift",
    "C": "C-ConvDerivative", "X": "X-OptionExercise", "J": "J-Other",
}


def _iso(value: str) -> str:
    """Convierte fechas del bulk ('31-MAY-2024' o ISO) a ISO YYYY-MM-DD."""
    s = (value or "").strip()
    if not s:
        return ""
    for fmt in ("%d-%b-%Y", "%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            continue
    return ""


def _actor_type(relationship: str, title: str) -> str:
    """Infiere actor_type del campo de relacion + titulo del insider."""
    r = (relationship or "").lower()
    t = (title or "").lower()
    if "ceo" in t or "chief executive" in t or "president" in t:
        return "ceo"
    if "cfo" in t or "chief financial" in t:
        return "cfo"
    if "10%" in r or "ten percent" in r:
        return "ten_percent_owner"
    if "officer" in r:
        return "officer"
    if "director" in r:
        return "director"
    return "insider"


def _read_tsv(zf: zipfile.ZipFile, name: str) -> Any:
    """Itera filas de un TSV del ZIP como dicts (csv.DictReader, tab)."""
    with zf.open(name) as f:
        text = io.TextIOWrapper(f, encoding="utf-8", errors="replace", newline="")
        yield from csv.DictReader(text, delimiter="\t")


def parse_insider_quarter(zip_bytes: bytes) -> list[dict[str, Any]]:
    """Parsea un ZIP trimestral de insiders en registros normalizados.

    Devuelve una lista de transacciones (no-derivativas) con el bloque temporal
    (event=TRANS_DATE, known=FILING_DATE) y los campos del schema de insiders.
    """
    zf = zipfile.ZipFile(io.BytesIO(zip_bytes))

    # 1. SUBMISSION: accession -> metadata del filing (issuer, ticker, fechas).
    submissions: dict[str, dict[str, str]] = {}
    for row in _read_tsv(zf, "SUBMISSION.tsv"):
        submissions[row["ACCESSION_NUMBER"]] = {
            "filing_date": _iso(row.get("FILING_DATE", "")),
            "document_type": row.get("DOCUMENT_TYPE", ""),
            "issuer_cik": (row.get("ISSUERCIK", "") or "").lstrip("0"),
            "company": row.get("ISSUERNAME", ""),
            "ticker": (row.get("ISSUERTRADINGSYMBOL", "") or "").strip().upper(),
        }

    # 2. REPORTINGOWNER: accession -> primer insider (nombre, relacion, titulo).
    owners: dict[str, dict[str, str]] = {}
    for row in _read_tsv(zf, "REPORTINGOWNER.tsv"):
        acc = row["ACCESSION_NUMBER"]
        if acc not in owners:  # primer owner del filing
            owners[acc] = {
                "name": row.get("RPTOWNERNAME", ""),
                "relationship": row.get("RPTOWNER_RELATIONSHIP", ""),
                "title": row.get("RPTOWNER_TITLE", ""),
            }

    # 3. NONDERIV_TRANS: una transaccion por fila -> registro completo.
    out: list[dict[str, Any]] = []
    for i, row in enumerate(_read_tsv(zf, "NONDERIV_TRANS.tsv")):
        acc = row["ACCESSION_NUMBER"]
        sub = submissions.get(acc, {})
        own = owners.get(acc, {})
        code = (row.get("TRANS_CODE", "") or "").strip().upper()
        try:
            shares = float(row.get("TRANS_SHARES") or 0)
        except ValueError:
            shares = 0.0
        try:
            price = float(row.get("TRANS_PRICEPERSHARE") or 0)
        except ValueError:
            price = 0.0
        tx_date = _iso(row.get("TRANS_DATE", ""))
        filing_date = sub.get("filing_date", "")
        rec = {
            "id": f"{acc}-{row.get('NONDERIV_TRANS_SK', i)}",
            "source": "sec_form_4",
            "insider_name": own.get("name", ""),
            "insider_title": own.get("title") or own.get("relationship", "") or "Insider",
            "actor_type": _actor_type(own.get("relationship", ""), own.get("title", "")),
            "company": sub.get("company", ""),
            "issuer_cik": sub.get("issuer_cik", ""),
            "ticker": sub.get("ticker", ""),
            "tx_code": code,
            "tx_type": TX_CODE_MAP.get(code, code or "Unknown"),
            "shares": int(shares) if shares.is_integer() else shares,
            "price_per_share": price,
            "value_usd": round(shares * price, 2),
            "tx_date": tx_date,
            "filing_date": filing_date,
            "document_type": sub.get("document_type", ""),
            "source_url": f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&filenum=&State=0&SIC=&dateb=&owner=include&count=40&search_text=",
        }
        rec.update(temporal_block(tx_date, filing_date or tx_date))
        out.append(rec)
    return out


def fetch_insider_quarter(year: int, quarter: int, client: Client | None = None) -> list[dict[str, Any]]:
    """Descarga y parsea el dataset bulk de insiders de un (year, quarter)."""
    client = client or Client(user_agent=UA_SEC, max_per_sec=5)
    url = INSIDER_ZIP_URL.format(year=year, q=quarter)
    r = client.get(url, timeout=180)
    if r.status_code != 200 or not r.content:
        return []
    return parse_insider_quarter(r.content)
