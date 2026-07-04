"""Tests del risk engine (risk/risk_engine.py, risk/monte_carlo.py) — Fase F."""

from __future__ import annotations

import numpy as np
import pandas as pd

from risk.monte_carlo import bootstrap_report
from risk.risk_engine import RiskLimits, compute_metrics, validate


def _returns(n=300, seed=1):
    """Matriz sintetica de retornos diarios de 3 activos."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range("2024-01-01", periods=n)
    return pd.DataFrame({
        "SPY": rng.normal(0.0004, 0.01, n),
        "TLT": rng.normal(0.0001, 0.008, n),
        "NVDA": rng.normal(0.001, 0.03, n),
    }, index=idx)


def test_compute_metrics_basico():
    """compute_metrics devuelve vol, VaR, CVaR, drawdown, beta, concentracion."""
    r = _returns()
    w = {"SPY": 0.5, "TLT": 0.3, "NVDA": 0.2}
    m = compute_metrics(w, r)
    assert m["ann_vol"] > 0
    assert m["var_95_1d"] > 0
    assert m["cvar_95_1d"] >= m["var_95_1d"]   # CVaR es peor (o igual) que VaR
    assert m["max_drawdown"] <= 0
    assert m["beta_spy"] is not None
    assert m["gross_exposure"] == 1.0
    assert m["effective_positions"] > 1


def test_validate_pasa_cartera_valida():
    """Una cartera diversificada dentro de limites pasa el gate."""
    w = {"SPY": 0.14, "TLT": 0.14, "NVDA": 0.12, "GLD": 0.10}  # suma 0.5
    g = validate(w, RiskLimits(), regime_budget=0.9)
    assert g["passed"] is True
    assert g["violations"] == []


def test_validate_rechaza_concentracion():
    """Peso por encima de max_position -> violacion."""
    w = {"SPY": 0.40, "TLT": 0.10}
    g = validate(w, RiskLimits(max_position=0.15))
    assert g["passed"] is False
    assert any("concentracion" in v for v in g["violations"])


def test_validate_rechaza_apalancamiento():
    """Suma de pesos > 1 -> violacion de apalancamiento."""
    w = {"SPY": 0.6, "TLT": 0.6}
    g = validate(w, RiskLimits())
    assert any("apalancamiento" in v for v in g["violations"])


def test_validate_respeta_presupuesto_regimen():
    """En risk-off (budget bajo), exposicion > budget -> violacion."""
    w = {"SPY": 0.10, "TLT": 0.10, "NVDA": 0.10, "GLD": 0.10, "QQQ": 0.10}  # 0.5
    g = validate(w, RiskLimits(max_position=0.2), regime_budget=0.4)  # budget 0.4 < 0.5
    assert any("regimen" in v for v in g["violations"])


def test_validate_limite_volatilidad():
    """Volatilidad por encima del limite -> violacion."""
    g = validate({"NVDA": 0.1}, RiskLimits(max_ann_vol=0.10),
                 metrics={"ann_vol": 0.30})
    assert any("volatilidad" in v for v in g["violations"])


def test_monte_carlo_bootstrap():
    """El bootstrap devuelve una distribucion coherente (p5 < mediana < p95)."""
    r = _returns()
    w = {"SPY": 0.5, "TLT": 0.3, "NVDA": 0.2}
    mc = bootstrap_report(w, r, horizon_days=21, n_sims=2000)
    assert mc["p5_return_pct"] < mc["median_return_pct"] < mc["p95_return_pct"]
    assert 0 <= mc["prob_loss"] <= 1
    assert mc["var_95_horizon"] > 0
