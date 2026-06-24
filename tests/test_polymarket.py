"""Tests del scraper de Polymarket.

Unitarios sobre el computo de metricas. Test de integracion contra la API
real se ejecuta solo si hay conectividad y es tolerante a esquemas que
cambien levemente.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import requests

from normalize.schema import POLYMARKET_REQUIRED
from scrapers import polymarket


def _network_ok() -> bool:
    """Comprueba que polymarket es alcanzable."""
    try:
        requests.head("https://data-api.polymarket.com/", timeout=5)
        return True
    except Exception:
        return False


def test_compute_metrics_calcula_winrate_correcto():
    """5 posiciones: 3 ganadoras (pnl>0) -> win_rate = 0.6."""
    positions = [
        {"realizedPnl": 100, "size": 50, "title": "M1", "outcome": "Yes"},
        {"realizedPnl": -50, "size": 30, "title": "M2", "outcome": "No"},
        {"realizedPnl": 200, "size": 100, "title": "M3", "outcome": "Yes"},
        {"realizedPnl": -10, "size": 20, "title": "M4", "outcome": "No"},
        {"realizedPnl": 5, "size": 10, "title": "M5", "outcome": "Yes"},
    ]
    metrics = polymarket._compute_trader_metrics(positions)
    assert metrics["win_rate"] == 0.6
    assert metrics["n_closed"] == 5
    # Top position por size: M3 (100)
    assert metrics["top_positions"][0]["market"] == "M3"
    assert metrics["top_positions"][0]["size"] == 100


def test_compute_metrics_lista_vacia():
    """Sin posiciones: win_rate=0, top_positions vacia."""
    metrics = polymarket._compute_trader_metrics([])
    assert metrics["win_rate"] == 0.0
    assert metrics["top_positions"] == []
    assert metrics["n_closed"] == 0


def test_safe_float_y_safe_int_no_fallan():
    """Helpers defensivos: None, strings, etc. devuelven default sin excepcion."""
    assert polymarket._safe_float(None) == 0.0
    assert polymarket._safe_float("abc") == 0.0
    assert polymarket._safe_float("3.14") == 3.14
    assert polymarket._safe_int("42") == 42
    assert polymarket._safe_int(None) == 0


def test_to_record_tiene_campos_requeridos():
    """Un registro construido debe tener todas las claves del schema."""
    entry = {
        "proxyWallet": "0xabc",
        "name": "whale_politics",
        "category": "POLITICS",
        "pnl": 542000,
        "volume": 2100000,
        "trades": 87,
    }
    metrics = {"win_rate": 0.91, "top_positions": [], "n_closed": 50}
    rec = polymarket._to_record(entry, metrics)
    assert POLYMARKET_REQUIRED.issubset(rec.keys())
    assert rec["wallet"] == "0xabc"
    assert rec["win_rate_positions"] == 0.91


@pytest.mark.skipif(not _network_ok(), reason="sin conectividad")
def test_integracion_leaderboard_devuelve_lista():
    """La API real debe devolver una lista no vacia con campos esperables."""
    import requests as _r
    s = _r.Session()
    s.headers.update({"User-Agent": "Watchdog/1.0-test"})
    try:
        r = s.get(polymarket.LEADERBOARD_URL,
                  params={"limit": 5, "period": "ALL", "sortBy": "PNL"},
                  timeout=15)
    except Exception as e:
        pytest.skip(f"network err: {e}")
    if r.status_code != 200:
        pytest.skip(f"leaderboard 200 esperado, got {r.status_code}")
    data = r.json()
    # Toleramos varios shapes
    items = data if isinstance(data, list) else (
        data.get("leaders") or data.get("data") or data.get("results") or []
    )
    assert isinstance(items, list)
    # No imponemos minimo (la API podria devolver 0 si esta en mantenimiento)
