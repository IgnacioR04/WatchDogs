"""Scoring fino de senales de insiders y deteccion de cluster buying (Fase D v3).

El patron de mayor alfa historico en insiders es el CLUSTER BUYING: varios
insiders distintos de la misma empresa comprando en mercado abierto (codigo P)
en una ventana corta. Este modulo detecta clusters y calcula un signal_score
que pondera:
  - Codigo de transaccion (P = compra en mercado abierto = la senal fuerte;
    S = venta = informativa pero menos; A/F/M/G = ruido de compensacion).
  - Rol del actor (CEO/CFO > director).
  - Importe economico.
  - Cluster (varios insiders comprando lo mismo -> boost).

Tambien produce risk_flags (avisos de calidad) y confidence (0-1).
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any

from normalize.scoring import actor_score, amount_score

# Peso base por codigo de transaccion de insider (0-100).
CODE_BASE = {
    "P": 90,   # compra en mercado abierto: la senal mas fuerte
    "S": 55,   # venta: informativa
    "D": 45,   # disposicion
    "M": 40,   # ejercicio de opciones (poca señal si no hay compra posterior)
    "F": 20,   # pago de impuestos con acciones (no es venta discrecional)
    "A": 20,   # grant (compensacion, no conviccion)
    "G": 25,   # gift
    "C": 40, "X": 40, "J": 40,
}

# Pesos de las componentes del signal_score de insiders.
W_CODE = 0.35
W_ACTOR = 0.20
W_AMOUNT = 0.25
W_CLUSTER = 0.20


def detect_clusters(signals: list[dict[str, Any]], min_distinct: int = 2) -> dict[str, int]:
    """Detecta cluster buying: nº de insiders DISTINTOS comprando (P) cada ticker.

    Args:
        signals: senales de insiders (con ticker, tx_code/direction, actor_name).
        min_distinct: minimo de insiders distintos para considerarlo cluster.

    Returns:
        {ticker: nº_insiders_distintos_comprando} solo para tickers con cluster.
    """
    buyers: dict[str, set[str]] = defaultdict(set)
    for s in signals:
        code = (s.get("tx_code") or "").upper()
        is_buy = code == "P" or s.get("direction") == "buy"
        tk = (s.get("ticker") or "").upper()
        if is_buy and tk:
            buyers[tk].add(s.get("actor_name") or s.get("insider_name") or "?")
    return {tk: len(bs) for tk, bs in buyers.items() if len(bs) >= min_distinct}


def _cluster_component(ticker: str, clusters: dict[str, int]) -> float:
    """Componente 0-100 del cluster: mas insiders distintos = mas alto."""
    n = clusters.get((ticker or "").upper(), 0)
    if n < 2:
        return 0.0
    # 2 insiders -> 60, 3 -> 80, 4+ -> 100
    return min(100.0, 40 + n * 20)


def insider_signal_score(sig: dict[str, Any], clusters: dict[str, int]) -> float:
    """Calcula el signal_score (0-100) de una senal de insider."""
    code = (sig.get("tx_code") or "").upper()
    code_c = CODE_BASE.get(code, 40.0)
    actor_c = actor_score(sig.get("actor_type"))
    amt = sig.get("amount_estimated") or sig.get("value_usd")
    amount_c = amount_score(amt)
    cluster_c = _cluster_component(sig.get("ticker", ""), clusters)
    score = (code_c * W_CODE + actor_c * W_ACTOR + amount_c * W_AMOUNT + cluster_c * W_CLUSTER)
    return round(min(100.0, score), 1)


def risk_flags(sig: dict[str, Any]) -> list[str]:
    """Avisos de calidad/riesgo de una senal (para el LLM y el risk engine)."""
    flags: list[str] = []
    # Frescura: retraso de disclosure alto -> senal envejecida
    dd = sig.get("delay_days")
    if isinstance(dd, int) and dd > 45:
        flags.append("stale_disclosure")
    # Confianza de ticker baja (House PDF sin ticker explicito)
    tc = sig.get("ticker_confidence")
    if isinstance(tc, (int, float)) and tc < 0.5:
        flags.append("low_ticker_confidence")
    # Importe pequeno (ruido)
    amt = sig.get("amount_estimated") or sig.get("value_usd") or 0
    if amt and amt < 25000:
        flags.append("small_amount")
    # Codigos que no son conviccion real
    if (sig.get("tx_code") or "").upper() in {"A", "F", "M"}:
        flags.append("non_discretionary")
    # Sin ticker resoluble
    if not sig.get("ticker"):
        flags.append("no_ticker")
    return flags


def confidence(sig: dict[str, Any]) -> float:
    """Confianza global de la senal (0-1): calidad de fuente + ticker + flags."""
    base = 0.9
    tc = sig.get("ticker_confidence")
    if isinstance(tc, (int, float)):
        base = min(base, 0.5 + tc * 0.5)
    n_flags = len(sig.get("risk_flags", []))
    return round(max(0.1, base - 0.1 * n_flags), 2)
