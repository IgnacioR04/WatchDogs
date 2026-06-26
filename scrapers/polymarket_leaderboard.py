"""Scraper de Polymarket: leaderboard + perfiles de traders.

Corrige los problemas detectados en la v1:
- `volume` se mapea desde el campo real `vol` del leaderboard (antes 0).
- `username` se mapea desde `userName` (antes vacio con la clave equivocada).
- Las closed positions se paginan completas con `sortBy=TIMESTAMP&sortDirection=DESC`
  hasta agotar (antes solo las primeras ordenadas por PnL, lo que inflaba el
  win rate).
- Se separan dos rankings distintos:
    * smart_traders: precision (win_rate, PnL, consistencia, nº posiciones).
    * whales: tamano (volumen, tamano medio de posicion).

Outputs:
    data/public/polymarket_smart_traders.json
    data/public/polymarket_whales.json
"""

from __future__ import annotations

import math
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from normalize.schema import temporal_block, write_json
from scrapers._http import UA_DEFAULT, Client

# Endpoints publicos de la Data API.
LEADERBOARD_URL = "https://data-api.polymarket.com/v1/leaderboard"
CLOSED_POSITIONS_URL = "https://data-api.polymarket.com/v1/closed-positions"

OUT_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
OUT_SMART = OUT_DIR / "polymarket_smart_traders.json"
OUT_WHALES = OUT_DIR / "polymarket_whales.json"

LEADERBOARD_LIMIT = 100        # cuantos top pedir
POSITIONS_PAGE = 50            # tamano de pagina de closed-positions
MAX_POSITIONS = 1000          # cap de posiciones a paginar por trader
MIN_CLOSED_FOR_SMART = 10     # minimo de posiciones para evaluar precision
TOP_POSITIONS_KEEP = 5        # cuantas posiciones guardamos en el output
SLEEP_BETWEEN = 0.1           # 10 req/s, por debajo del limite 150/10s

# Palabras clave para clasificar la categoria dominante de un trader.
CATEGORY_KEYWORDS = {
    "sports": ["win on", "vs.", "vs ", "spread:", "nba", "nfl", "fifwc", "soccer",
               "match", "game", "champions", "premier", "league", "cup"],
    "politics": ["president", "election", "senate", "congress", "trump", "biden",
                 "governor", "primary", "vote", "parliament", "minister"],
    "crypto": ["bitcoin", "btc", "ethereum", "eth", "solana", "crypto", "coin"],
    "economy": ["fed", "rate", "inflation", "gdp", "recession", "cpi", "jobs"],
}


def _safe_float(v: Any, default: float = 0.0) -> float:
    """Convierte v a float; default si no es convertible."""
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


def _classify_category(title: str) -> str | None:
    """Devuelve la categoria de un mercado segun palabras clave en el titulo."""
    t = (title or "").lower()
    for cat, kws in CATEGORY_KEYWORDS.items():
        if any(k in t for k in kws):
            return cat
    return None


def fetch_leaderboard(client: Client) -> list[dict[str, Any]]:
    """Descarga el leaderboard PNL all-time. Devuelve lista de entradas crudas."""
    params = {"limit": LEADERBOARD_LIMIT, "period": "ALL", "sortBy": "PNL"}
    data = client.get_json(LEADERBOARD_URL, params=params)
    if isinstance(data, dict):
        for key in ("leaders", "data", "results"):
            if isinstance(data.get(key), list):
                return data[key]
        return []
    return data if isinstance(data, list) else []


def fetch_all_closed_positions(client: Client, wallet: str) -> list[dict[str, Any]]:
    """Pagina TODAS las closed positions de un wallet ordenadas por timestamp desc.

    Clave anti-sesgo: al ordenar por TIMESTAMP (no por PnL) y paginar hasta
    agotar, obtenemos el win rate real sobre todas las posiciones, no solo las
    ganadoras del top.
    """
    positions: list[dict[str, Any]] = []
    offset = 0
    while offset < MAX_POSITIONS:
        params = {
            "user": wallet,
            "limit": POSITIONS_PAGE,
            "offset": offset,
            "sortBy": "TIMESTAMP",
            "sortDirection": "DESC",
        }
        try:
            data = client.get_json(CLOSED_POSITIONS_URL, params=params)
        except Exception:
            break
        batch = data if isinstance(data, list) else data.get("data", [])
        if not batch:
            break
        positions.extend(batch)
        if len(batch) < POSITIONS_PAGE:
            break
        offset += POSITIONS_PAGE
        time.sleep(SLEEP_BETWEEN)
    return positions


def _smart_score(win_rate: float, pnl: float, n_closed: int, avg_pnl: float) -> float:
    """Score de precision (0-100): premia win rate alto con muestra suficiente.

    Combina: win_rate (50%), PnL log-escalado (30%), consistencia por nº de
    posiciones (20%). Una cuenta con pocas posiciones queda penalizada en
    consistencia aunque tenga win rate perfecto.
    """
    pnl_factor = max(0.0, min(1.0, (math.log10(pnl) - 3) / 4)) if pnl > 0 else 0.0  # 1k..10M
    consistency = min(n_closed / 50.0, 1.0)
    score = win_rate * 50 + pnl_factor * 30 + consistency * 20
    return round(max(0.0, min(100.0, score)), 1)


def _whale_score(volume: float, avg_size: float) -> float:
    """Score de tamano (0-100): premia volumen y tamano medio de posicion.

    Combina: volumen log-escalado (70%), tamano medio log-escalado (30%).
    """
    vol_factor = max(0.0, min(1.0, (math.log10(volume) - 4) / 4)) if volume > 0 else 0.0  # 10k..100M
    size_factor = max(0.0, min(1.0, (math.log10(avg_size) - 2) / 4)) if avg_size > 0 else 0.0  # 100..1M
    score = vol_factor * 70 + size_factor * 30
    return round(max(0.0, min(100.0, score)), 1)


def build_profile(entry: dict[str, Any], positions: list[dict[str, Any]]) -> dict[str, Any]:
    """Construye el perfil de un trader a partir del leaderboard + posiciones."""
    wallet = entry.get("proxyWallet") or entry.get("address") or entry.get("user") or ""
    volume = _safe_float(entry.get("vol") or entry.get("volume"))
    pnl = _safe_float(entry.get("pnl") or entry.get("profit"))

    n_closed = len(positions)
    wins = sum(1 for p in positions if _safe_float(p.get("realizedPnl")) > 0)
    losses = n_closed - wins
    win_rate = round(wins / n_closed, 4) if n_closed else 0.0
    realized_total = sum(_safe_float(p.get("realizedPnl")) for p in positions)
    avg_pnl = round(realized_total / n_closed, 2) if n_closed else 0.0

    # Tamano: usamos totalBought (USDC apostados) como proxy de tamano de posicion.
    sizes = [abs(_safe_float(p.get("totalBought"))) for p in positions if p.get("totalBought")]
    avg_size = round(sum(sizes) / len(sizes), 2) if sizes else 0.0

    # Categorias dominantes
    cat_counts: dict[str, int] = {}
    for p in positions:
        cat = _classify_category(p.get("title") or p.get("eventSlug") or "")
        if cat:
            cat_counts[cat] = cat_counts.get(cat, 0) + 1
    categories = sorted(cat_counts, key=cat_counts.get, reverse=True)[:3]

    # Top posiciones por tamano
    top_positions = []
    for p in sorted(positions, key=lambda x: abs(_safe_float(x.get("totalBought"))), reverse=True)[:TOP_POSITIONS_KEEP]:
        top_positions.append({
            "market": p.get("title") or p.get("eventSlug") or "",
            "outcome": p.get("outcome") or "",
            "size": round(abs(_safe_float(p.get("totalBought"))), 2),
            "realized_pnl": round(_safe_float(p.get("realizedPnl")), 2),
        })

    profile = {
        "wallet": wallet,
        "username": entry.get("userName") or entry.get("name") or "",
        "x_username": entry.get("xUsername") or "",
        "verified": bool(entry.get("verifiedBadge")),
        "pnl": round(pnl, 2),
        "volume": round(volume, 2),
        "closed_positions": n_closed,
        "winning_positions": wins,
        "losing_positions": losses,
        "win_rate": win_rate,
        "avg_realized_pnl": avg_pnl,
        "avg_position_size": avg_size,
        "categories": categories,
        "smart_score": _smart_score(win_rate, pnl, n_closed, avg_pnl),
        "whale_score": _whale_score(volume, avg_size),
        "top_positions": top_positions,
        "source": "polymarket_data_api",
    }
    # Polymarket es publico al instante (on-chain): el perfil es un snapshot del
    # momento de captura. event=known=scrape_date.
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    profile.update(temporal_block(now[:10], now[:10], scrape_date=now))
    return profile


def run() -> tuple[Path, Path]:
    """Ejecuta el scraping completo y escribe smart_traders + whales."""
    client = Client(user_agent=UA_DEFAULT, max_per_sec=10)
    leaders = fetch_leaderboard(client)
    print(f"[polymarket] leaderboard: {len(leaders)} entradas")

    profiles: list[dict[str, Any]] = []
    for i, entry in enumerate(leaders):
        wallet = entry.get("proxyWallet") or entry.get("address") or entry.get("user") or ""
        if not wallet:
            continue
        positions = fetch_all_closed_positions(client, wallet)
        profile = build_profile(entry, positions)
        profiles.append(profile)
        if (i + 1) % 10 == 0:
            print(f"  procesados {i + 1}/{len(leaders)}")
        time.sleep(SLEEP_BETWEEN)

    # Smart traders: minimo de posiciones para que el win rate sea significativo.
    smart = [p for p in profiles if p["closed_positions"] >= MIN_CLOSED_FOR_SMART]
    smart.sort(key=lambda p: p["smart_score"], reverse=True)

    # Whales: ordenados por whale_score (volumen + tamano), sin minimo de posiciones.
    whales = sorted(profiles, key=lambda p: p["whale_score"], reverse=True)

    write_json(OUT_SMART, smart)
    write_json(OUT_WHALES, whales)
    print(
        f"[polymarket] {len(smart)} smart traders (>= {MIN_CLOSED_FOR_SMART} pos), "
        f"{len(whales)} whales -> {OUT_DIR}"
    )
    return OUT_SMART, OUT_WHALES


if __name__ == "__main__":
    run()
