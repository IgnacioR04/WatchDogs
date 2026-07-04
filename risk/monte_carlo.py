"""Monte Carlo por bootstrap historico (Fase F v3).

Simula la evolucion futura de una cartera remuestreando (con reemplazo) sus
retornos diarios historicos reales. El bootstrap historico se usa PRIMERO
porque no asume normalidad y respeta las colas gordas y la autocorrelacion
aproximada del mercado (mejor que un Monte Carlo gaussiano ingenuo).

Devuelve la distribucion de rentabilidad a `horizon_days`: media, mediana,
percentiles, probabilidad de perdida y VaR/CVaR del horizonte.

Salida (via risk_engine): seccion monte_carlo del risk_report.json.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


def _portfolio_returns(weights: dict[str, float], returns: pd.DataFrame) -> np.ndarray:
    """Retornos diarios de la cartera como array numpy."""
    cols = [t for t in weights if t in returns.columns]
    if not cols:
        return np.array([])
    w = np.array([weights[t] for t in cols])
    return returns[cols].to_numpy() @ w


def bootstrap_report(weights: dict[str, float], returns: pd.DataFrame,
                     horizon_days: int = 21, n_sims: int = 5000,
                     seed: int = 42) -> dict[str, Any]:
    """Simula n_sims trayectorias de horizon_days por bootstrap historico.

    Returns:
        dict con la distribucion de rentabilidad al horizonte (mean, median,
        p5, p25, p75, p95), prob_loss y VaR/CVaR del horizonte.
    """
    pr = _portfolio_returns(weights, returns)
    if pr.size < horizon_days:
        return {"error": "historico insuficiente para simular"}

    rng = np.random.default_rng(seed)
    # Muestreo con reemplazo: n_sims x horizon_days indices sobre los retornos.
    idx = rng.integers(0, len(pr), size=(n_sims, horizon_days))
    sampled = pr[idx]                                   # (n_sims, horizon_days)
    # Rentabilidad compuesta de cada trayectoria.
    terminal = np.prod(1 + sampled, axis=1) - 1         # (n_sims,)

    p = lambda q: round(float(np.percentile(terminal, q)) * 100, 2)
    var5 = float(-np.percentile(terminal, 5))
    tail = terminal[terminal <= -var5]
    cvar5 = float(-tail.mean()) if tail.size else var5
    return {
        "horizon_days": horizon_days,
        "n_sims": n_sims,
        "method": "historical_bootstrap",
        "expected_return_pct": round(float(terminal.mean()) * 100, 2),
        "median_return_pct": p(50),
        "p5_return_pct": p(5),
        "p25_return_pct": p(25),
        "p75_return_pct": p(75),
        "p95_return_pct": p(95),
        "prob_loss": round(float((terminal < 0).mean()), 3),
        "var_95_horizon": round(var5, 4),
        "cvar_95_horizon": round(cvar5, 4),
    }
