"""Tests del health report (pipelines/build_health_report.py).

Usa datos mock escritos a un data/public/ temporal monkeypatcheando las rutas
del modulo, para no depender de los JSON reales del repo.
"""

from __future__ import annotations

import json

import pipelines.build_health_report as hr
from scrapers._dates import days_ago_iso, today_iso


def _write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


def test_build_report_estructura_y_overall(tmp_path, monkeypatch):
    """Con datos mock frescos, todos ok -> overall ok y estructura correcta."""
    public = tmp_path / "public"
    monkeypatch.setattr(hr, "PUBLIC_DIR", public)
    monkeypatch.setattr(hr, "OUTPUT_PATH", public / "health_report.json")

    # Congress fresco con tickers limpios
    _write(public / "congress_trades_30d.json", [
        {"ticker": "NVDA", "tx_date": today_iso(), "disclosure_date": today_iso(),
         "ticker_confidence": 0.98},
    ])
    # SEC insiders fresco
    _write(public / "sec_insiders_30d.json", [
        {"insider_name": "HUANG", "ticker": "NVDA", "tx_date": today_iso(),
         "filing_date": today_iso()},
    ])
    # 13F del quarter esperado (no stale): usamos el report_date esperado
    from scrapers._dates import expected_13f_quarter, quarter_end_date
    _write(public / "institutional_holdings_latest.json", [
        {"manager": "Test Fund", "cik": "1", "report_date": quarter_end_date(expected_13f_quarter()),
         "holdings": [], "aum_usd": 1},
    ])
    # Polymarket sano: volume>0, win rate realista
    _write(public / "polymarket_smart_traders.json", [
        {"wallet": "0x1", "volume": 100000, "win_rate": 0.55, "closed_positions": 30},
    ])
    _write(public / "polymarket_whales.json", [
        {"wallet": "0x1", "volume": 5_000_000, "win_rate": 0.4, "closed_positions": 12},
    ])

    report = hr.build()
    assert report["overall_status"] == "ok"
    assert set(report["datasets"]) == {"congress", "sec_insiders", "institutional_13f", "polymarket"}
    for ds in report["datasets"].values():
        assert "status" in ds and "issues" in ds


def test_detecta_senate_viejo_y_ticker_pdf(tmp_path, monkeypatch):
    """Datos viejos + ticker 'PDF' -> warning con issues correctas."""
    public = tmp_path / "public"
    monkeypatch.setattr(hr, "PUBLIC_DIR", public)
    monkeypatch.setattr(hr, "OUTPUT_PATH", public / "health_report.json")

    _write(public / "congress_trades_30d.json", [
        {"ticker": "PDF", "tx_date": "2019-01-01", "disclosure_date": "2019-01-05"},
    ])
    cong = hr.check_congress()
    assert cong["status"] in {"warning", "error"}
    assert any("stale_source" in i for i in cong["issues"])
    assert any("invalid_tickers_present" in i for i in cong["issues"])
    assert cong["blocked_for_signals"] is True


def test_detecta_polymarket_volume_cero_y_winrate_inflado(tmp_path, monkeypatch):
    """Todos volume=0 y win rate medio alto -> issues correctas."""
    public = tmp_path / "public"
    monkeypatch.setattr(hr, "PUBLIC_DIR", public)
    monkeypatch.setattr(hr, "OUTPUT_PATH", public / "health_report.json")

    _write(public / "polymarket_smart_traders.json", [
        {"wallet": "0x1", "volume": 0, "win_rate": 0.95, "closed_positions": 20},
        {"wallet": "0x2", "volume": 0, "win_rate": 0.92, "closed_positions": 15},
    ])
    _write(public / "polymarket_whales.json", [])
    pm = hr.check_polymarket()
    assert "all_volume_zero" in pm["issues"]
    assert any("inflated_avg_win_rate" in i for i in pm["issues"])


def test_sec_missing_es_error(tmp_path, monkeypatch):
    """Fichero SEC ausente -> error (posible bloqueo SEC)."""
    public = tmp_path / "public"
    monkeypatch.setattr(hr, "PUBLIC_DIR", public)
    public.mkdir(parents=True)
    sec = hr.check_sec_insiders()
    assert sec["status"] == "error"
    assert sec["blocked_for_signals"] is True
