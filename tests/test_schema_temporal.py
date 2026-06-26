"""Tests del modelo temporal (normalize/schema.py) — Fase A v3."""

from __future__ import annotations

import pytest

from normalize.schema import TEMPORAL_FIELDS, temporal_block, validate_temporal


def test_bloque_temporal_campos_y_delay():
    """temporal_block emite los 4 campos y calcula delay_days correcto."""
    b = temporal_block("2026-06-18", "2026-06-20")
    assert TEMPORAL_FIELDS.issubset(b.keys())
    assert b["event_date"] == "2026-06-18"
    assert b["known_date"] == "2026-06-20"
    assert b["delay_days"] == 2
    assert b["scrape_date"]  # no vacio


def test_known_igual_event_si_no_se_pasa():
    """Sin known_date (dato publico al instante), known=event y delay=0."""
    b = temporal_block("2026-06-22")
    assert b["known_date"] == b["event_date"]
    assert b["delay_days"] == 0


def test_acepta_formato_us():
    """Acepta fechas US M/D/YYYY y las normaliza a ISO."""
    b = temporal_block("06/18/2026", "06/20/2026")
    assert b["event_date"] == "2026-06-18"
    assert b["known_date"] == "2026-06-20"
    assert b["delay_days"] == 2


def test_anti_lookahead_se_corrige():
    """Si known_date < event_date (imposible), se fuerza known=event."""
    b = temporal_block("2026-06-20", "2026-06-18")
    assert b["known_date"] == "2026-06-20"
    assert b["delay_days"] == 0


def test_estimated_flag():
    """estimated=True marca known_date_estimated."""
    b = temporal_block("2020-01-01", estimated=True)
    assert b.get("known_date_estimated") is True


def test_validate_temporal_detecta_falta():
    """validate_temporal lanza si falta el bloque."""
    with pytest.raises(ValueError):
        validate_temporal({"event_date": "2026-06-18"}, "x")


def test_validate_temporal_detecta_lookahead():
    """validate_temporal lanza si known_date < event_date."""
    bad = {"event_date": "2026-06-20", "known_date": "2026-06-18",
           "scrape_date": "2026-06-26T00:00:00Z", "delay_days": -2}
    with pytest.raises(ValueError):
        validate_temporal(bad, "x")


def test_no_lookahead_helper_sobre_lista():
    """Helper de no-lookahead: ningun registro tiene known_date < event_date."""
    records = [
        temporal_block("2026-06-01", "2026-06-05"),
        temporal_block("2026-05-30", "2026-06-30"),
        temporal_block("2026-06-20"),
    ]
    for r in records:
        assert r["known_date"] >= r["event_date"]
