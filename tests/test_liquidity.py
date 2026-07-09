"""Tests del filtro de liquidez del allocator (portfolio/allocator.py)."""

from __future__ import annotations

import pandas as pd
import pytest

import portfolio.allocator as al


def _write_pv(base, symbol, close: float, volume: float, days: int = 20):
    """Parquet de precios con Close y Volume constantes."""
    d = base / f"symbol={symbol}" / "timeframe=1d"
    d.mkdir(parents=True)
    idx = pd.bdate_range("2026-06-01", periods=days)
    pd.DataFrame({"Close": close, "Volume": volume}, index=idx).to_parquet(d / "y.parquet")


@pytest.fixture
def prices(tmp_path, monkeypatch):
    p = tmp_path / "prices"
    monkeypatch.setattr(al, "PRICES_DIR", p)
    return p


def test_liquido_pasa(prices):
    # $50 x 1M acciones/dia = $50M/dia de volumen -> pasa
    _write_pv(prices, "GOOD", close=50.0, volume=1_000_000)
    assert al.liquidity_ok("GOOD") is True


def test_penny_stock_falla(prices):
    # precio < $5 -> fuera aunque tenga volumen
    _write_pv(prices, "PENNY", close=0.63, volume=10_000_000)
    assert al.liquidity_ok("PENNY") is False


def test_sin_volumen_falla(prices):
    # $20 x 5,000 acciones = $100K/dia < $2M -> fuera
    _write_pv(prices, "THIN", close=20.0, volume=5_000)
    assert al.liquidity_ok("THIN") is False


def test_sin_datos_falla(prices):
    # sin parquet -> sin liquidez demostrable -> fuera
    assert al.liquidity_ok("NODATA") is False
