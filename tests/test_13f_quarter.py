"""Tests de la logica por quarter de 13F (scrapers/sec_13f.py)."""

from __future__ import annotations

from scrapers import sec_13f


def test_quarter_of():
    """reportDate ISO -> quarter YYYYQX."""
    assert sec_13f._quarter_of("2026-03-31") == "2026Q1"
    assert sec_13f._quarter_of("2025-12-31") == "2025Q4"
    assert sec_13f._quarter_of("2026-06-30") == "2026Q2"
    assert sec_13f._quarter_of("bad") == "?"


def test_find_13f_ordena_por_reportdate():
    """_find_13f_filings devuelve 13F-HR (y /A) ordenados por reportDate desc."""
    subs = {"filings": {"recent": {
        "form": ["13F-HR", "10-K", "13F-HR", "13F-HR/A"],
        "accessionNumber": ["a1", "x", "a2", "a3"],
        "primaryDocument": ["d1", "x", "d2", "d3"],
        "filingDate": ["2026-05-14", "2026-01-01", "2026-02-13", "2026-05-20"],
        "reportDate": ["2026-03-31", "2025-12-31", "2025-12-31", "2026-03-31"],
    }}}
    filings = sec_13f._find_13f_filings(subs)
    assert len(filings) == 3  # excluye el 10-K
    assert filings[0]["report_date"] == "2026-03-31"  # mas reciente primero
    assert any(f["is_amendment"] for f in filings)     # detecta el /A


def test_compute_changes_direcciones():
    """_compute_changes detecta new/increased/decreased/exited."""
    rec = {
        "manager": "Test", "quarter": "2026Q1",
        "holdings": [
            {"cusip": "AAA", "asset_name": "Alpha", "ticker": "ALP", "value_usd": 200},  # increased
            {"cusip": "BBB", "asset_name": "Beta", "ticker": "BET", "value_usd": 50},     # new
        ],
        "_previous_holdings": [
            {"cusip": "AAA", "asset_name": "Alpha", "ticker": "ALP", "value_usd": 100},
            {"cusip": "CCC", "asset_name": "Gamma", "ticker": "GAM", "value_usd": 80},     # exited
        ],
    }
    changes = sec_13f._compute_changes(rec)
    by_dir = {c["direction"] for c in changes}
    assert "increased" in by_dir
    assert "new" in by_dir
    assert "exited" in by_dir
    alpha = next(c for c in changes if c["cusip"] == "AAA")
    assert alpha["change_value_usd"] == 100
    assert alpha["change_pct"] == 1.0


def test_compute_changes_sin_previo_vacio():
    """Sin quarter previo, no hay cambios."""
    assert sec_13f._compute_changes({"holdings": [], "_previous_holdings": []}) == []
