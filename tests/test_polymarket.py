"""Tests del scraper Polymarket v2 (scrapers/polymarket_leaderboard.py).

Cubre: mapeo correcto de campos (vol->volume, userName->username), paginacion
de closed positions, separacion smart/whale y los scores.
"""

from __future__ import annotations

from scrapers import polymarket_leaderboard as pm


class _FakeClient:
    """Cliente falso que devuelve paginas predefinidas para closed-positions."""

    def __init__(self, pages):
        # pages: lista de listas (cada una es una pagina/batch)
        self._pages = pages
        self.calls = 0

    def get_json(self, url, *, params=None, timeout=30):
        idx = (params or {}).get("offset", 0) // pm.POSITIONS_PAGE
        self.calls += 1
        return self._pages[idx] if idx < len(self._pages) else []


def _pos(pnl, bought, title="Will X win on 2026-06-22?"):
    return {"realizedPnl": pnl, "totalBought": bought, "title": title, "outcome": "Yes"}


def test_paginacion_agota_todas_las_paginas():
    """fetch_all_closed_positions concatena hasta una pagina incompleta."""
    full = [_pos(10, 100) for _ in range(pm.POSITIONS_PAGE)]   # pagina completa
    partial = [_pos(-5, 50) for _ in range(10)]                # pagina incompleta -> fin
    client = _FakeClient([full, partial])
    positions = pm.fetch_all_closed_positions(client, "0xabc")
    assert len(positions) == pm.POSITIONS_PAGE + 10
    assert client.calls == 2  # para tras la pagina incompleta


def test_build_profile_mapea_vol_y_username():
    """vol->volume y userName->username; win_rate calculado sobre todas las pos."""
    entry = {"proxyWallet": "0xabc", "userName": "whale_x", "vol": 2_100_000,
             "pnl": 542_000, "verifiedBadge": True}
    positions = [_pos(100, 5000), _pos(-50, 3000), _pos(200, 8000), _pos(-10, 1000)]
    prof = pm.build_profile(entry, positions)
    assert prof["volume"] == 2_100_000          # antes quedaba en 0
    assert prof["username"] == "whale_x"
    assert prof["closed_positions"] == 4
    assert prof["winning_positions"] == 2
    assert prof["win_rate"] == 0.5
    assert prof["verified"] is True
    assert 0 <= prof["smart_score"] <= 100
    assert 0 <= prof["whale_score"] <= 100


def test_winrate_no_inflado_con_perdedoras():
    """Con mitad perdedoras, el win rate es 0.5 (no inflado)."""
    positions = [_pos(10, 100) for _ in range(5)] + [_pos(-10, 100) for _ in range(5)]
    prof = pm.build_profile({"proxyWallet": "0x1", "vol": 1000, "pnl": 0}, positions)
    assert prof["win_rate"] == 0.5


def test_clasifica_categorias():
    """Detecta categoria dominante por palabras clave del titulo."""
    positions = [
        _pos(10, 100, "Will France win on 2026-06-22?"),
        _pos(10, 100, "NBA: Spurs vs. Knicks"),
        _pos(10, 100, "Will Trump win the election?"),
    ]
    prof = pm.build_profile({"proxyWallet": "0x1", "vol": 1, "pnl": 1}, positions)
    assert "sports" in prof["categories"] or "politics" in prof["categories"]


def test_smart_vs_whale_scores_distintos():
    """Un trader pequeno-preciso tiene smart alto; uno grande tiene whale alto."""
    # Smart: muchas posiciones ganadoras, poco volumen
    smart_pos = [_pos(100, 500) for _ in range(40)]
    smart = pm.build_profile({"proxyWallet": "0x1", "vol": 50_000, "pnl": 500_000}, smart_pos)
    # Whale: pocas posiciones, volumen enorme
    whale_pos = [_pos(0, 5_000_000) for _ in range(3)]
    whale = pm.build_profile({"proxyWallet": "0x2", "vol": 20_000_000, "pnl": 100_000}, whale_pos)
    assert smart["smart_score"] > whale["smart_score"]
    assert whale["whale_score"] > smart["whale_score"]
