"""Scraper de top traders de Polymarket.

Estrategia:
1. Leaderboard global por PNL all-time (limit 100).
2. Por cada trader: descarga sus closed positions (limit 200).
3. Calcula win_rate = posiciones con realizedPnl > 0 / total cerradas.
4. Filtra traders con < 10 posiciones cerradas.

Rate limits Polymarket: la doc dice ~1000 req/10s general, 150 req/10s para
positions/trades. Mantenemos sleep(0.1) entre llamadas a positions (10 req/s,
muy por debajo del limite).
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any

from normalize.schema import POLYMARKET_REQUIRED, validate_records, write_json
from scrapers._http import get_json, make_session

OUTPUT_PATH = Path(__file__).resolve().parents[1] / "data" / "polymarket_top_traders.json"

# Endpoints publicos. La API Data ofrece leaderboard + closed-positions.
LEADERBOARD_URL = "https://data-api.polymarket.com/v1/leaderboard"
CLOSED_POSITIONS_URL = "https://data-api.polymarket.com/v1/closed-positions"

LEADERBOARD_LIMIT = 100        # cuantos top a pedir del leaderboard
POSITIONS_LIMIT = 200          # cuantas posiciones por trader
MIN_CLOSED_POSITIONS = 10      # filtro: traders con >= 10 closed positions
TOP_POSITIONS_KEEP = 5         # cuantas top positions guardamos en el output
SLEEP_BETWEEN_TRADERS = 0.1    # 10 req/s, por debajo del limite 15/s


def _safe_float(v: Any, default: float = 0.0) -> float:
    """Convierte v a float, default si no es convertible."""
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


def _safe_int(v: Any, default: int = 0) -> int:
    """Convierte v a int, default si no es convertible."""
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return default


def fetch_leaderboard(session) -> list[dict[str, Any]]:
    """Descarga el leaderboard PNL all-time. Devuelve lista de entradas crudas."""
    params = {
        "limit": LEADERBOARD_LIMIT,
        "period": "ALL",
        "sortBy": "PNL",
    }
    data = get_json(session, LEADERBOARD_URL, params=params, timeout=30, sleep_after=0.2)
    # La API a veces devuelve {"leaders": [...]} o lista directa. Robustez:
    if isinstance(data, dict):
        for key in ("leaders", "data", "results"):
            if isinstance(data.get(key), list):
                return data[key]
        return []
    return data if isinstance(data, list) else []


def fetch_closed_positions(session, wallet: str) -> list[dict[str, Any]]:
    """Descarga closed positions de un wallet. Devuelve [] si error."""
    params = {"user": wallet, "limit": POSITIONS_LIMIT}
    try:
        data = get_json(session, CLOSED_POSITIONS_URL, params=params, timeout=20)
    except Exception:
        return []
    if isinstance(data, dict):
        for key in ("data", "positions", "results"):
            if isinstance(data.get(key), list):
                return data[key]
        return []
    return data if isinstance(data, list) else []


def _compute_trader_metrics(positions: list[dict[str, Any]]) -> dict[str, Any]:
    """Calcula win_rate y top_positions a partir de closed positions."""
    if not positions:
        return {"win_rate": 0.0, "top_positions": [], "n_closed": 0}
    wins = 0
    for p in positions:
        if _safe_float(p.get("realizedPnl") or p.get("realized_pnl")) > 0:
            wins += 1
    win_rate = wins / len(positions) if positions else 0.0
    # Top 5 por size absoluto (size = stake en USDC)
    positions_sorted = sorted(
        positions,
        key=lambda p: abs(_safe_float(p.get("size") or p.get("initialValue") or 0)),
        reverse=True,
    )
    top_positions: list[dict[str, Any]] = []
    for p in positions_sorted[:TOP_POSITIONS_KEEP]:
        top_positions.append({
            "market": p.get("title") or p.get("market") or p.get("eventTitle") or "",
            "position": p.get("outcome") or p.get("position") or "",
            "size": _safe_float(p.get("size") or p.get("initialValue") or 0),
            "realized_pnl": _safe_float(p.get("realizedPnl") or p.get("realized_pnl")),
        })
    return {"win_rate": round(win_rate, 4), "top_positions": top_positions, "n_closed": len(positions)}


def _to_record(entry: dict[str, Any], metrics: dict[str, Any]) -> dict[str, Any]:
    """Convierte una entrada del leaderboard + metricas en un registro canonico."""
    wallet = entry.get("proxyWallet") or entry.get("address") or entry.get("user") or ""
    return {
        "wallet": wallet,
        "username": entry.get("name") or entry.get("username") or "",
        "category": entry.get("category") or "ALL",
        "pnl": _safe_float(entry.get("pnl") or entry.get("profit") or 0),
        "volume": _safe_float(entry.get("volume") or 0),
        "markets_traded": _safe_int(entry.get("trades") or entry.get("markets") or metrics["n_closed"]),
        "win_rate_positions": metrics["win_rate"],
        "top_positions": metrics["top_positions"],
    }


def run() -> Path:
    """Ejecuta el scraping completo y escribe data/polymarket_top_traders.json."""
    session = make_session()
    leaders = fetch_leaderboard(session)
    print(f"[polymarket] leaderboard: {len(leaders)} entradas")

    out: list[dict[str, Any]] = []
    skipped_few_positions = 0
    for i, entry in enumerate(leaders):
        wallet = entry.get("proxyWallet") or entry.get("address") or entry.get("user") or ""
        if not wallet:
            continue
        positions = fetch_closed_positions(session, wallet)
        if len(positions) < MIN_CLOSED_POSITIONS:
            skipped_few_positions += 1
            time.sleep(SLEEP_BETWEEN_TRADERS)
            continue
        metrics = _compute_trader_metrics(positions)
        out.append(_to_record(entry, metrics))
        if (i + 1) % 10 == 0:
            print(f"  procesados {i + 1}/{len(leaders)}")
        time.sleep(SLEEP_BETWEEN_TRADERS)

    # Ordenar por PNL desc
    out.sort(key=lambda r: r.get("pnl", 0), reverse=True)

    if out:
        validate_records(out[:1], POLYMARKET_REQUIRED, "polymarket")
    out_path = write_json(OUTPUT_PATH, out)
    print(
        f"[polymarket] {len(out)} traders >= {MIN_CLOSED_POSITIONS} pos cerradas, "
        f"{skipped_few_positions} descartados -> {out_path}"
    )
    return out_path


if __name__ == "__main__":
    run()
