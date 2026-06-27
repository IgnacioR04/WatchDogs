"""Tests de Fase B: market_prices (yfinance) y macro_fred (FRED), mockeados."""

from __future__ import annotations

import pandas as pd

from scrapers import macro_fred, market_prices


def test_archive_symbol_particiona_por_ano(tmp_path, monkeypatch):
    """archive_symbol escribe un parquet por año en la ruta particionada."""
    monkeypatch.setattr(market_prices, "PRICES_DIR", tmp_path / "prices")
    idx = pd.to_datetime(["2024-12-30", "2024-12-31", "2025-01-02", "2025-01-03"])
    df = pd.DataFrame({"Open": [1, 2, 3, 4], "Close": [1.1, 2.1, 3.1, 4.1]}, index=idx)
    n = market_prices.archive_symbol("SPY", df)
    assert n == 4
    files = list((tmp_path / "prices").rglob("*.parquet"))
    assert len(files) == 2  # un parquet por año (2024 y 2025)


def test_build_snapshot_calcula_retornos(tmp_path, monkeypatch):
    """build_snapshot lee el parquet y calcula close + retornos."""
    monkeypatch.setattr(market_prices, "PRICES_DIR", tmp_path / "prices")
    idx = pd.to_datetime([f"2025-01-{d:02d}" for d in range(1, 26)])
    df = pd.DataFrame({"Close": [100 + i for i in range(25)]}, index=idx)
    market_prices.archive_symbol("SPY", df)
    snap = market_prices.build_snapshot(["SPY"])
    assert len(snap) == 1
    s = snap[0]
    assert s["symbol"] == "SPY"
    assert s["close"] == 124.0
    assert s["ret_1d"] is not None and s["ret_20d"] is not None


def test_safe_symbol():
    """_safe_symbol limpia caracteres problematicos (^, -, /)."""
    assert market_prices._safe_symbol("^VIX") == "IDX_VIX"
    assert market_prices._safe_symbol("BTC-USD") == "BTC_USD"


def test_fred_fetch_series_parsea_y_temporal(monkeypatch):
    """fetch_series parsea observaciones, salta missing '.' y añade temporal."""
    class _Resp:
        status_code = 200
        def raise_for_status(self): pass
        def json(self):
            return {"observations": [
                {"date": "2026-05-01", "value": "4.3"},
                {"date": "2026-06-01", "value": "."},      # missing -> se salta
                {"date": "2026-06-15", "value": "4.4"},
            ]}
    class _Sess:
        def get(self, url, params=None, timeout=30): return _Resp()

    monkeypatch.setenv("FRED_API_KEY", "testkey")
    recs = macro_fred.fetch_series("UNRATE", session=_Sess())
    assert len(recs) == 2  # el '.' se omite
    r = recs[0]
    assert r["series_id"] == "UNRATE"
    assert r["value"] == 4.3
    assert r["event_date"] == "2026-05-01"
    # known_date = event + lag (UNRATE lag 7) y marcado estimado
    assert r["known_date"] > r["event_date"]
    assert r["known_date_estimated"] is True


def test_fred_sin_key_lanza(monkeypatch):
    """Sin FRED_API_KEY, _api_key lanza."""
    monkeypatch.delenv("FRED_API_KEY", raising=False)
    import pytest
    with pytest.raises(RuntimeError):
        macro_fred._api_key()
