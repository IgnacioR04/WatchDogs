"""Tests del motor de metricas del paper trading (pipelines/build_paper_metrics.py)."""

from __future__ import annotations

import json

import pandas as pd
import pytest

import pipelines.build_paper_metrics as pm


def _write_prices(base, symbol, closes: dict[str, float]):
    """Crea el parquet de precios de un simbolo con el layout del history."""
    d = base / f"symbol={symbol}" / "timeframe=1d"
    d.mkdir(parents=True)
    s = pd.Series(closes)
    s.index = pd.to_datetime(s.index)
    pd.DataFrame({"Close": s}).to_parquet(d / "y.parquet")


@pytest.fixture
def env(tmp_path, monkeypatch):
    prices = tmp_path / "prices"
    public = tmp_path / "public"
    public.mkdir()
    monkeypatch.setattr(pm, "PRICES_DIR", prices)
    monkeypatch.setattr(pm, "PUBLIC_DIR", public)
    monkeypatch.setattr(pm, "LEDGER_PATH", public / "paper_ledger.json")
    monkeypatch.setattr(pm, "OUTPUT_PATH", public / "paper_trading.json")
    # Costes a 0 en los tests de logica de retornos (hay tests dedicados de costes).
    monkeypatch.setattr(pm, "COST_PER_SIDE", 0.0)
    return prices, public


def test_sin_ledger_no_revienta(env):
    _, public = env
    out = pm.build()
    assert out["n_cycles"] == 0
    assert out["metrics"]["n_days"] == 0
    assert out["equity_curve"] == []


def test_equity_curve_aplica_retornos_ponderados(env):
    prices, public = env
    days = {"2026-07-06": 100, "2026-07-07": 100, "2026-07-08": 100,
            "2026-07-09": 100, "2026-07-10": 100}
    _write_prices(prices, "SPY", days)
    # AAA salta +10% el dia 9
    _write_prices(prices, "AAA", {"2026-07-06": 10, "2026-07-07": 10,
                                  "2026-07-08": 10, "2026-07-09": 11, "2026-07-10": 11})
    ledger = [{"approved_at": "2026-07-07T15:00:00+00:00", "weights": {"AAA": 0.5}}]
    (public / "paper_ledger.json").write_text(json.dumps(ledger), encoding="utf-8")

    out = pm.build()
    m = out["metrics"]
    # dias de mercado tras la aprobacion: 8, 9, 10 de julio
    assert m["n_days"] == 3
    # dia 9: 0.5 * 10% = +5% -> 105 EUR
    assert m["equity_eur"] == pytest.approx(105.0, abs=0.01)
    assert m["total_return"] == pytest.approx(0.05, abs=1e-4)
    assert m["win_rate_days"] == pytest.approx(1 / 3, abs=1e-3)
    # posicion AAA: entro al cierre previo (10) y vale 11 -> +10%
    assert out["positions"]["AAA"]["ret_since_entry"] == pytest.approx(0.10, abs=1e-3)


def test_rebalanceo_usa_pesos_del_ultimo_ciclo(env):
    prices, public = env
    days = {"2026-07-06": 100, "2026-07-07": 100, "2026-07-08": 100,
            "2026-07-09": 100, "2026-07-10": 100}
    _write_prices(prices, "SPY", days)
    # AAA sube +10% el dia 9; BBB sube +20% el dia 10
    _write_prices(prices, "AAA", {"2026-07-06": 10, "2026-07-07": 10,
                                  "2026-07-08": 10, "2026-07-09": 11, "2026-07-10": 11})
    _write_prices(prices, "BBB", {"2026-07-06": 5, "2026-07-07": 5,
                                  "2026-07-08": 5, "2026-07-09": 5, "2026-07-10": 6})
    ledger = [
        {"approved_at": "2026-07-07T15:00:00+00:00", "weights": {"AAA": 1.0}},
        # rebalanceo el dia 9: sale AAA, entra BBB -> la subida de AAA del dia 9
        # ya no se captura (pesos nuevos aplican ese dia), la de BBB del 10 si
        {"approved_at": "2026-07-09T15:00:00+00:00", "weights": {"BBB": 1.0}},
    ]
    (public / "paper_ledger.json").write_text(json.dumps(ledger), encoding="utf-8")

    out = pm.build()
    m = out["metrics"]
    # dia 8: AAA plano (0%). dia 9: pesos nuevos, BBB plano (0%). dia 10: BBB +20%
    assert m["equity_eur"] == pytest.approx(120.0, abs=0.01)
    assert out["n_cycles"] == 2
    assert set(out["positions"].keys()) == {"BBB"}


def test_costes_de_rotacion_se_descuentan(env, monkeypatch):
    """La compra inicial y cada rebalanceo pagan COST_PER_SIDE sobre el turnover."""
    monkeypatch.setattr(pm, "COST_PER_SIDE", 0.0015)
    prices, public = env
    flat = {"2026-07-06": 100, "2026-07-07": 100, "2026-07-08": 100,
            "2026-07-09": 100, "2026-07-10": 100}
    _write_prices(prices, "SPY", flat)
    _write_prices(prices, "AAA", {k: 10 for k in flat})
    ledger = [{"approved_at": "2026-07-07T15:00:00+00:00", "weights": {"AAA": 1.0}}]
    (public / "paper_ledger.json").write_text(json.dumps(ledger), encoding="utf-8")

    out = pm.build()
    m = out["metrics"]
    # compra inicial: turnover 1.0 -> coste 100 * 1.0 * 0.0015 = 0.15 EUR
    assert m["costs_eur"] == pytest.approx(0.15, abs=1e-3)
    assert m["turnover_total"] == pytest.approx(1.0, abs=1e-6)
    # activos planos: la equity solo baja por el coste
    assert m["equity_eur"] == pytest.approx(99.85, abs=0.01)
    # el ciclo registra su turnover y coste
    assert out["cycles"][0]["turnover"] == pytest.approx(1.0, abs=1e-6)


def test_fx_convierte_activos_usd_a_eur(env):
    """Si el dolar se fortalece (EURUSD baja), los activos USD valen mas en EUR."""
    prices, public = env
    flat = {"2026-07-06": 100, "2026-07-07": 100, "2026-07-08": 100,
            "2026-07-09": 100, "2026-07-10": 100}
    _write_prices(prices, "SPY", flat)
    _write_prices(prices, "AAA", {k: 10 for k in flat})  # activo plano en USD
    # EURUSD cae de 1.00 a 0.95 el dia 9 (dolar +5.26% en EUR)
    _write_prices(prices, "EURUSD_X", {"2026-07-06": 1.0, "2026-07-07": 1.0,
                                       "2026-07-08": 1.0, "2026-07-09": 0.95, "2026-07-10": 0.95})
    ledger = [{"approved_at": "2026-07-07T15:00:00+00:00", "weights": {"AAA": 1.0}}]
    (public / "paper_ledger.json").write_text(json.dumps(ledger), encoding="utf-8")

    out = pm.build()
    # activo plano en USD pero +5.26% en EUR por el movimiento de divisa
    assert out["metrics"]["total_return"] == pytest.approx(1 / 0.95 - 1, abs=1e-3)


def test_instrument_type():
    """Heuristica de operabilidad UE: ETF USA, mutual fund, cripto, accion."""
    assert pm.instrument_type("SPY") == "etf_us"
    assert pm.instrument_type("VFLEX") == "fund_us"
    assert pm.instrument_type("FTECX") == "fund_us"
    assert pm.instrument_type("BTC-USD") == "crypto"
    assert pm.instrument_type("AAPL") == "stock"
    assert pm.instrument_type("GF") == "stock"  # 2 letras, no es fondo


def test_benchmark_spy_captura_primer_dia(env):
    prices, public = env
    # SPY sube +3% el dia 8, el PRIMER dia de mercado tras la aprobacion: el
    # benchmark debe capturarlo (base = cierre del dia de aprobacion, no del dia 1)
    _write_prices(prices, "SPY", {"2026-07-06": 100, "2026-07-07": 100,
                                  "2026-07-08": 103, "2026-07-09": 103, "2026-07-10": 103})
    _write_prices(prices, "AAA", {"2026-07-06": 10, "2026-07-07": 10,
                                  "2026-07-08": 10, "2026-07-09": 10, "2026-07-10": 10})
    ledger = [{"approved_at": "2026-07-07T15:00:00+00:00", "weights": {"AAA": 1.0}}]
    (public / "paper_ledger.json").write_text(json.dumps(ledger), encoding="utf-8")

    out = pm.build()
    assert out["metrics"]["spy_return"] == pytest.approx(0.03, abs=1e-3)


def test_benchmark_spy_rebasado(env):
    prices, public = env
    # SPY sube +2% el dia 9
    _write_prices(prices, "SPY", {"2026-07-06": 100, "2026-07-07": 100,
                                  "2026-07-08": 100, "2026-07-09": 102, "2026-07-10": 102})
    _write_prices(prices, "AAA", {"2026-07-06": 10, "2026-07-07": 10,
                                  "2026-07-08": 10, "2026-07-09": 10, "2026-07-10": 10})
    ledger = [{"approved_at": "2026-07-07T15:00:00+00:00", "weights": {"AAA": 1.0}}]
    (public / "paper_ledger.json").write_text(json.dumps(ledger), encoding="utf-8")

    out = pm.build()
    m = out["metrics"]
    assert m["spy_return"] == pytest.approx(0.02, abs=1e-3)
    # cartera plana vs SPY +2% -> excess -2%
    assert m["excess_return"] == pytest.approx(-0.02, abs=1e-3)
