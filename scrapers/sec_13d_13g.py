"""Scraper de SEC Schedule 13D/13G (grandes accionistas >5%).

13D/13G capturan beneficial ownership relevante (normalmente >5% de una clase),
complementando al 13F. Desde la modernizacion SEC de 2024, estos filings usan
un primary_doc.xml estructurado del que extraemos limpiamente:
  - issuer (nombre, CIK, CUSIP) y ticker (de display_names del search)
  - reporting person / filer (nombre, CIK)
  - percentOfClass (% de la clase) y aggregateAmountOwned (acciones)
  - dateOfEvent y submissionType (13D, 13G, 13D/A, 13G/A)

Fuente: EDGAR full-text search (efts) filtrando forms "SCHEDULE 13D"/"SCHEDULE
13G" de los ultimos 30 dias, luego el primary_doc.xml de cada filing.

Output: data/public/sec_13d_13g_30d.json
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from normalize.schema import temporal_block, write_json
from normalize.scoring import score_signal
from scrapers._dates import days_ago_iso, to_iso, today_iso
from scrapers._http import UA_SEC, Client

EFTS_URL = "https://efts.sec.gov/LATEST/search-index"
ARCHIVES = "https://www.sec.gov/Archives/edgar/data"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "data" / "public" / "sec_13d_13g_30d.json"

PAGE_SIZE = 100
MAX_DOCS = 250          # cap de primary_doc.xml a parsear por run (rate limit SEC)
WINDOW_DAYS = 30

# Mapea submissionType -> (form_kind, es_amendment)
FORM_FILTERS = ["SCHEDULE 13D", "SCHEDULE 13G"]


def _strip(tag: str) -> str:
    """Quita namespace XML."""
    return tag.split("}", 1)[-1] if "}" in tag else tag


def _extract_ticker(display_name: str) -> str:
    """Extrae el ticker del display_name del issuer: 'Foo Inc (NVGS) (CIK ...)'."""
    m = re.search(r"\(([A-Z]{1,6})\)", display_name or "")
    return m.group(1) if m else ""


def search_filings(client: Client, form: str, start: str, end: str) -> list[dict[str, Any]]:
    """Pagina el full-text search para un form en el rango de fechas dado."""
    out: list[dict[str, Any]] = []
    frm = 0
    while True:
        params = {"forms": form, "startdt": start, "enddt": end, "from": frm}
        try:
            data = client.get_json(EFTS_URL, params=params)
        except Exception:
            break
        hits = data.get("hits", {}).get("hits", [])
        if not hits:
            break
        out.extend(hits)
        frm += PAGE_SIZE
        if frm >= 1000 or len(hits) < PAGE_SIZE:  # EDGAR limita 'from' a ~1000
            break
    return out


def parse_primary_doc(xml_text: str) -> dict[str, Any]:
    """Extrae los campos clave del primary_doc.xml de un 13D/13G."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return {}
    fields: dict[str, str] = {}
    wanted = {
        "submissionType", "issuerName", "issuerCIK", "issuerCusipNumber",
        "dateOfEvent", "reportingPersonName", "reportingPersonCIK",
        "aggregateAmountOwned", "percentOfClass",
    }
    for el in root.iter():
        t = _strip(el.tag)
        if t in wanted and el.text and el.text.strip() and t not in fields:
            fields[t] = el.text.strip()
    return fields


def _doc_url(cik: str, accession: str, doc: str) -> str:
    """URL del documento dentro del filing."""
    return f"{ARCHIVES}/{int(cik)}/{accession.replace('-', '')}/{doc}"


def hit_to_record(client: Client, hit: dict[str, Any]) -> dict[str, Any] | None:
    """Convierte un hit del search + su primary_doc en un registro normalizado."""
    src = hit.get("_source", {})
    display = src.get("display_names", []) or []
    ciks = src.get("ciks", []) or []
    if not display or not ciks:
        return None

    issuer_display = display[0]
    ticker = _extract_ticker(issuer_display)
    issuer_name = re.sub(r"\s*\(.*$", "", issuer_display).strip()
    issuer_cik = ciks[0]
    filer_name = re.sub(r"\s*\(.*$", "", display[1]).strip() if len(display) > 1 else ""
    filer_cik = ciks[1] if len(ciks) > 1 else ""

    _id = hit.get("_id", "")
    accession, _, doc = _id.partition(":")
    if not doc.endswith(".xml"):
        return None
    url = _doc_url(issuer_cik, accession, doc)
    try:
        r = client.get(url, timeout=30)
        fields = parse_primary_doc(r.text) if r.status_code == 200 else {}
    except Exception:
        fields = {}

    sub_type = fields.get("submissionType") or src.get("file_type") or ""
    try:
        pct = float(fields["percentOfClass"]) if fields.get("percentOfClass") else None
    except ValueError:
        pct = None
    try:
        shares = int(float(fields["aggregateAmountOwned"])) if fields.get("aggregateAmountOwned") else None
    except ValueError:
        shares = None

    rec = {
        "id": f"{accession}",
        "source": "sec_13d" if "13D" in sub_type else "sec_13g",
        "source_type": "large_holder",
        "filer_name": fields.get("reportingPersonName") or filer_name,
        "filer_cik": fields.get("reportingPersonCIK") or filer_cik,
        "actor_name": fields.get("reportingPersonName") or filer_name,
        "actor_type": "large_holder",
        "company": fields.get("issuerName") or issuer_name,
        "issuer_cik": fields.get("issuerCIK") or issuer_cik,
        "ticker": ticker,
        "asset_name": fields.get("issuerName") or issuer_name,
        "ownership_pct": pct,
        "shares_owned": shares,
        "direction": "stake",
        "filing_type": sub_type,
        "filing_date": src.get("file_date") or "",
        "disclosure_date": src.get("file_date") or "",
        "source_url": _doc_url(issuer_cik, accession, doc),
    }
    # Bloque temporal: event=fecha del hecho (dateOfEvent), known=filing.
    rec.update(temporal_block(
        to_iso(fields.get("dateOfEvent")) or src.get("file_date"),
        src.get("file_date"),
    ))
    score_signal(rec)
    return rec


def run(max_docs: int = MAX_DOCS) -> Path:
    """Descarga 13D/13G de los ultimos 30 dias y escribe el JSON publico."""
    client = Client(user_agent=UA_SEC, max_per_sec=8)
    start, end = days_ago_iso(WINDOW_DAYS), today_iso()

    all_hits: list[dict[str, Any]] = []
    for form in FORM_FILTERS:
        hits = search_filings(client, form, start, end)
        print(f"  [13d13g] {form}: {len(hits)} filings")
        all_hits.extend(hits)

    # Ordenar por fecha desc y limitar el numero de docs a parsear.
    all_hits.sort(key=lambda h: h.get("_source", {}).get("file_date", ""), reverse=True)
    all_hits = all_hits[:max_docs]

    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for i, hit in enumerate(all_hits):
        rec = hit_to_record(client, hit)
        if rec and rec["id"] not in seen:
            seen.add(rec["id"])
            records.append(rec)
        if (i + 1) % 50 == 0:
            print(f"    {i + 1}/{len(all_hits)} ({len(records)} records)")

    records.sort(key=lambda r: r.get("filing_date", ""), reverse=True)
    write_json(OUTPUT_PATH, records)
    with_pct = sum(1 for r in records if r.get("ownership_pct") is not None)
    print(f"[sec_13d_13g] {len(records)} filings ({with_pct} con ownership%) -> {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == "__main__":
    run()
