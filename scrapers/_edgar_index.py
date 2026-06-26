"""Utilidades para recorrer los indices historicos de EDGAR (backfill).

EDGAR publica un indice maestro por trimestre con TODOS los filings:
    https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{q}/form.idx

Cada linea (ancho fijo) tiene: tipo de formulario, nombre de empresa, CIK,
fecha de filing (= known_date, cuando el filing fue diseminado) y la ruta al
.txt del submission. Este modulo permite iterar esos indices filtrando por
tipo de formulario para reconstruir el historico de cualquier fuente SEC.

Respeta el limite de 10 req/s de la SEC y exige User-Agent declarado.
"""

from __future__ import annotations

import re
from typing import Any, Iterator

from scrapers._http import UA_SEC, Client

FULL_INDEX_URL = "https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{q}/form.idx"
ARCHIVES_BASE = "https://www.sec.gov/Archives/"

# Formularios de interes por fuente WATCHDOG.
FORMS_BY_SOURCE = {
    "sec_insiders": {"3", "4", "5", "3/A", "4/A", "5/A"},
    "sec_13f": {"13F-HR", "13F-HR/A"},
    "sec_13d_13g": {"SC 13D", "SC 13G", "SC 13D/A", "SC 13G/A",
                    "SCHEDULE 13D", "SCHEDULE 13G", "SCHEDULE 13D/A", "SCHEDULE 13G/A"},
}

# Linea de datos del form.idx: form_type (puede tener espacios internos) hasta
# 2+ espacios, luego company, CIK, fecha YYYY-MM-DD y la ruta edgar/...
_LINE_RE = re.compile(
    r"^(?P<form>\S+(?:\s\S+)*?)\s{2,}"
    r"(?P<company>.+?)\s+"
    r"(?P<cik>\d+)\s+"
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<file>edgar/\S+\.txt)\s*$"
)


def _accession_from_path(file_name: str) -> str:
    """Extrae el accession number de la ruta edgar/data/CIK/ACCESSION.txt."""
    base = file_name.rsplit("/", 1)[-1]
    return base.replace(".txt", "")


def parse_form_idx(text: str, forms: set[str] | None = None) -> list[dict[str, Any]]:
    """Parsea el contenido de un form.idx y devuelve entradas (opcional: filtradas).

    Cada entrada: {form_type, company, cik, date_filed, file_name, accession,
    filing_url}. `date_filed` es la known_date (fecha de diseminacion publica).
    """
    out: list[dict[str, Any]] = []
    for line in text.splitlines():
        m = _LINE_RE.match(line)
        if not m:
            continue
        form = m.group("form").strip()
        if forms is not None and form not in forms:
            continue
        file_name = m.group("file")
        out.append({
            "form_type": form,
            "company": m.group("company").strip(),
            "cik": m.group("cik"),
            "date_filed": m.group("date"),  # known_date
            "file_name": file_name,
            "accession": _accession_from_path(file_name),
            "filing_url": ARCHIVES_BASE + file_name,
        })
    return out


def fetch_quarter_index(year: int, quarter: int, forms: set[str] | None = None,
                        client: Client | None = None) -> list[dict[str, Any]]:
    """Descarga y parsea el form.idx de un (year, quarter). Filtra por `forms`."""
    client = client or Client(user_agent=UA_SEC, max_per_sec=8)
    url = FULL_INDEX_URL.format(year=year, q=quarter)
    try:
        r = client.get(url, timeout=60)
        if r.status_code != 200:
            return []
        return parse_form_idx(r.text, forms=forms)
    except Exception:
        return []


def iter_quarters(from_year: int, to_year: int) -> Iterator[tuple[int, int]]:
    """Itera (year, quarter) de from_year Q1 a to_year Q4 en orden cronologico."""
    for year in range(from_year, to_year + 1):
        for q in (1, 2, 3, 4):
            yield year, q


def index_url(year: int, quarter: int) -> str:
    """Devuelve la URL del form.idx de un (year, quarter)."""
    return FULL_INDEX_URL.format(year=year, q=quarter)
