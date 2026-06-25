"""Indice de PTRs (Periodic Transaction Reports) de la Camara de Representantes.

Descarga el ZIP anual oficial del House Clerk y extrae la metadata de los
filings tipo 'P' (PTR): representante, estado/distrito, fecha de filing y
doc_id, con la URL del PDF correspondiente.

Este indice NO tiene tickers ni importes (eso esta dentro de cada PDF). Lo
consume congress_house_pdf_parser.py para decidir que PDFs descargar y parsear.
"""

from __future__ import annotations

import io
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any

from scrapers._dates import parse_date, within_last_days
from scrapers._http import Client, UA_DEFAULT

ZIP_URL_TEMPLATE = "https://disclosures-clerk.house.gov/public_disc/financial-pdfs/{year}FD.ZIP"
PDF_URL_TEMPLATE = "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/{year}/{docid}.pdf"


@dataclass
class PTRFiling:
    """Metadata de un filing PTR del House Clerk."""
    doc_id: str
    first: str
    last: str
    suffix: str
    state_dst: str
    filing_date: str   # ISO YYYY-MM-DD
    year: int
    pdf_url: str

    @property
    def politician(self) -> str:
        """Nombre completo del representante."""
        return " ".join(p for p in (self.first, self.last, self.suffix) if p).strip()


def _text(member: ET.Element, tag: str) -> str:
    """Texto de un subelemento del <Member>, o '' si falta."""
    el = member.find(tag)
    return (el.text or "").strip() if (el is not None and el.text) else ""


def parse_zip_xml(zip_bytes: bytes, year: int) -> list[PTRFiling]:
    """Parsea el XML dentro del ZIP del Clerk y devuelve los filings PTR (tipo P)."""
    try:
        zf = zipfile.ZipFile(io.BytesIO(zip_bytes))
    except zipfile.BadZipFile:
        return []
    xml_name = next((n for n in zf.namelist() if n.lower().endswith(".xml")), None)
    if not xml_name:
        return []
    try:
        root = ET.fromstring(zf.read(xml_name).decode("utf-8", errors="replace"))
    except ET.ParseError:
        return []

    out: list[PTRFiling] = []
    for member in root.iter("Member"):
        if _text(member, "FilingType") != "P":  # solo PTR
            continue
        doc_id = _text(member, "DocID")
        if not doc_id:
            continue
        # FilingDate viene como M/D/YYYY -> ISO
        filing_date = parse_date(_text(member, "FilingDate"))
        out.append(PTRFiling(
            doc_id=doc_id,
            first=_text(member, "First"),
            last=_text(member, "Last"),
            suffix=_text(member, "Suffix"),
            state_dst=_text(member, "StateDst"),
            filing_date=filing_date.date().isoformat() if filing_date else "",
            year=year,
            pdf_url=PDF_URL_TEMPLATE.format(year=year, docid=doc_id),
        ))
    return out


def fetch_index(years: list[int] | None = None, recent_days: int | None = None,
                client: Client | None = None) -> list[PTRFiling]:
    """Descarga el indice de PTRs para los anos dados.

    Args:
        years: lista de anos a descargar (default: ano actual + anterior).
        recent_days: si se indica, filtra a PTRs presentados en los ultimos N dias.
        client: cliente HTTP opcional (para reusar sesion).

    Returns:
        Lista de PTRFiling.
    """
    client = client or Client(user_agent=UA_DEFAULT, max_per_sec=5)
    if years is None:
        now = datetime.now(timezone.utc)
        years = [now.year, now.year - 1]

    filings: list[PTRFiling] = []
    for year in years:
        url = ZIP_URL_TEMPLATE.format(year=year)
        try:
            r = client.get(url, timeout=60)
            r.raise_for_status()
        except Exception as e:
            print(f"  [house_index] {year}: fallo descarga ({e})")
            continue
        year_filings = parse_zip_xml(r.content, year)
        print(f"  [house_index] {year}: {len(year_filings)} PTR filings")
        filings.extend(year_filings)

    if recent_days is not None:
        filings = [f for f in filings if f.filing_date and within_last_days(f.filing_date, recent_days)]
    return filings


def to_dict(filing: PTRFiling) -> dict[str, Any]:
    """Convierte un PTRFiling a dict serializable."""
    d = asdict(filing)
    d["politician"] = filing.politician
    return d
