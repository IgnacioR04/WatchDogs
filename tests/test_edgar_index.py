"""Tests del parser de indices EDGAR (scrapers/_edgar_index.py) — Fase A v3."""

from __future__ import annotations

from scrapers._edgar_index import (
    FORMS_BY_SOURCE,
    _accession_from_path,
    iter_quarters,
    parse_form_idx,
)

# Muestra real del formato form.idx (ancho fijo).
SAMPLE = """Description:           Master Index of EDGAR Dissemination Feed by Form Type
Form Type   Company Name                                                  CIK         Date Filed  File Name
---------------------------------------------------------------------------------------------------------------------------------------------
4                APPLE INC                                                     320193      2024-04-15  edgar/data/320193/0001209191-24-001.txt
13F-HR           1060 Capital, LLC                                             1602119     2024-05-15  edgar/data/1602119/0001602119-24-000004.txt
SC 13D           111 Equity Group                                              2024448     2024-06-07  edgar/data/2024448/0001193125-24-157548.txt
SC 13G/A         Big Holder LLC                                                999999      2024-06-08  edgar/data/999999/0001-24-002.txt
"""


def test_parsea_lineas_ancho_fijo():
    """Parsea form_type, cik, fecha y accession de cada linea."""
    rows = parse_form_idx(SAMPLE)
    assert len(rows) == 4
    by_form = {r["form_type"]: r for r in rows}
    assert by_form["4"]["cik"] == "320193"
    assert by_form["4"]["date_filed"] == "2024-04-15"
    assert by_form["4"]["accession"] == "0001209191-24-001"
    # Formularios con espacio interno (SC 13D) se parsean correctamente
    assert "SC 13D" in by_form
    assert "SC 13G/A" in by_form


def test_filtro_por_forms():
    """parse_form_idx filtra por el set de formularios pedido."""
    rows = parse_form_idx(SAMPLE, forms={"13F-HR", "13F-HR/A"})
    assert len(rows) == 1
    assert rows[0]["form_type"] == "13F-HR"


def test_date_filed_es_known_date():
    """date_filed (diseminacion) es la known_date del filing."""
    rows = parse_form_idx(SAMPLE, forms={"SC 13D"})
    assert rows[0]["date_filed"] == "2024-06-07"
    assert rows[0]["filing_url"].endswith("edgar/data/2024448/0001193125-24-157548.txt")


def test_forms_by_source_cubre_fuentes():
    """Hay mapeo de formularios para cada fuente SEC."""
    assert "4" in FORMS_BY_SOURCE["sec_insiders"]
    assert "13F-HR" in FORMS_BY_SOURCE["sec_13f"]
    assert "SC 13D" in FORMS_BY_SOURCE["sec_13d_13g"]


def test_iter_quarters_orden_cronologico():
    """iter_quarters recorre (year, quarter) en orden."""
    qs = list(iter_quarters(2023, 2024))
    assert qs[0] == (2023, 1)
    assert qs[-1] == (2024, 4)
    assert len(qs) == 8


def test_accession_from_path():
    """Extrae el accession de la ruta del .txt."""
    assert _accession_from_path("edgar/data/320193/0001209191-24-001.txt") == "0001209191-24-001"
