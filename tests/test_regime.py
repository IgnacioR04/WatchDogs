"""Tests del motor de regimen (regime/market_regime.py) — Fase E."""

from __future__ import annotations

import pandas as pd

from regime.market_regime import (
    compose_risk,
    credit_rule,
    rates_rule,
    trend_rule,
    volatility_rule,
)


def test_volatility_rule_tramos():
    """VIX por tramos: calm/normal/elevated/stress."""
    assert volatility_rule(12)[0] == "calm"
    assert volatility_rule(17)[0] == "normal"
    assert volatility_rule(24)[0] == "elevated"
    assert volatility_rule(35)[0] == "stress"
    assert volatility_rule(None)[0] == "unknown"


def test_trend_rule_bull_bear_neutral():
    """SPY vs MA50/MA200: bull (subiendo), bear (bajando), neutral."""
    # serie alcista: 300 dias creciendo -> close > ma50 > ma200
    up = pd.Series(range(100, 400), index=pd.date_range("2024-01-01", periods=300))
    assert trend_rule(up)[0] == "bull"
    # serie bajista
    down = pd.Series(range(400, 100, -1), index=pd.date_range("2024-01-01", periods=300))
    assert trend_rule(down)[0] == "bear"
    # serie corta -> unknown
    assert trend_rule(pd.Series([1, 2, 3]))[0] == "unknown"


def test_credit_rule_spread():
    """HY spread: tight/normal/widening/stress."""
    assert credit_rule(2.5)[0] == "tight"
    assert credit_rule(3.8)[0] == "normal"
    assert credit_rule(5.0)[0] == "widening"
    assert credit_rule(7.0)[0] == "stress"


def test_rates_rule_curva():
    """Curva 10Y-2Y: invertida/flat/steep."""
    assert rates_rule(-0.4)[0] == "inverted"
    assert rates_rule(0.2)[0] == "flat"
    assert rates_rule(1.2)[0] == "steep"


def test_compose_risk_on():
    """Entorno alcista + credito tenso -> risk_on con budget alto."""
    risk, budget, reasons = compose_risk("normal", "bull", "tight", "flat")
    assert risk == "risk_on"
    assert budget >= 0.70
    assert any("alcista" in r for r in reasons)


def test_compose_risk_off():
    """Entorno de estres -> risk_off con budget bajo."""
    risk, budget, reasons = compose_risk("stress", "bear", "stress", "inverted")
    assert risk == "risk_off"
    assert budget <= 0.45


def test_budget_acotado_0_1():
    """recommended_risk_budget siempre entre 0.1 y 1.0."""
    _, b_hi, _ = compose_risk("calm", "bull", "tight", "steep")
    _, b_lo, _ = compose_risk("stress", "bear", "stress", "inverted")
    assert 0.1 <= b_lo <= b_hi <= 1.0
