"""Metodos de ponderacion de cartera (Fase G v3).

Empezamos por lo simple y robusto (equal weight e inverse volatility), como
manda el documento; PyPortfolioOpt/HRP/Black-Litterman vendran despues. La
ventaja de inverse-vol es que da menos peso a los activos mas volatiles sin
necesidad de estimar retornos esperados (que es lo que mas se equivoca).
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def equal_weight(tickers: list[str]) -> dict[str, float]:
    """Reparte el 100% a partes iguales entre los tickers."""
    if not tickers:
        return {}
    w = 1.0 / len(tickers)
    return {t: round(w, 4) for t in tickers}


def inverse_vol(tickers: list[str], returns: pd.DataFrame) -> dict[str, float]:
    """Pondera por 1/volatilidad: menos peso a los mas volatiles.

    Los tickers sin datos de retorno reciben la volatilidad media (peso neutro).
    Devuelve pesos que suman 1.
    """
    if not tickers:
        return {}
    vols = {}
    for t in tickers:
        if t in returns.columns and returns[t].std() > 0:
            vols[t] = float(returns[t].std())
    if not vols:
        return equal_weight(tickers)
    avg_vol = float(np.mean(list(vols.values())))
    inv = {t: 1.0 / vols.get(t, avg_vol) for t in tickers}
    total = sum(inv.values())
    return {t: round(v / total, 4) for t, v in inv.items()}


def cap_weights(weights: dict[str, float], max_position: float) -> dict[str, float]:
    """Limita cada peso a max_position redistribuyendo el exceso proporcionalmente.

    Itera hasta que ningun peso supere el cap (o converge). Mantiene la suma.
    """
    if not weights:
        return {}
    w = dict(weights)
    total = sum(w.values())
    # Si el cap es demasiado bajo para el total (max*n < total) es imposible
    # cumplirlo sin bajar la exposicion; en ese caso repartimos a partes iguales al cap.
    if max_position * len(w) < total - 1e-9:
        return {t: round(max_position, 4) for t in w}
    for _ in range(20):
        over = {t: v for t, v in w.items() if v > max_position + 1e-9}
        if not over:
            break
        excess = sum(v - max_position for v in over.values())
        for t in over:
            w[t] = max_position
        under = {t: v for t, v in w.items() if v < max_position - 1e-9}
        if not under:
            break
        under_total = sum(under.values())
        for t in under:
            w[t] += excess * (under[t] / under_total) if under_total else 0
    return {t: round(v, 4) for t, v in w.items()}
