"""Construye top_movements_30d.json: los movimientos mas importantes del mes.

Toma las senales de mayor importance_score, les genera un titulo y un resumen
legibles por humanos, y enlaza noticias relacionadas (por ticker) si existen.
Alimenta el dashboard (tab Top Movements) y el llm_context.

Salida: data/public/top_movements_30d.json
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
OUTPUT_PATH = PUBLIC_DIR / "top_movements_30d.json"
TOP_N = 40

# Etiquetas legibles por tipo de actor.
ACTOR_LABEL = {
    "ceo": "CEO", "cfo": "CFO", "director": "Director",
    "ten_percent_owner": "10% owner", "officer": "Officer", "insider": "Insider",
    "house_rep": "House representative", "senator": "Senator",
    "top_institutional_manager": "Institutional manager", "large_holder": "Large holder",
}

DIRECTION_VERB = {
    "buy": "compro", "sell": "vendio", "stake": "declaro participacion en",
    "hold": "mantuvo", "other": "opero", "increase": "aumento", "decrease": "redujo",
}


def _load(name: str) -> list[dict]:
    p = PUBLIC_DIR / name
    if not p.exists():
        return []
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def _fmt_amount(v: Any) -> str:
    """Formatea un importe USD compacto."""
    if not v:
        return ""
    v = float(v)
    if v >= 1e9:
        return f"${v/1e9:.1f}B"
    if v >= 1e6:
        return f"${v/1e6:.1f}M"
    if v >= 1e3:
        return f"${v/1e3:.0f}K"
    return f"${v:.0f}"


def _title_and_summary(sig: dict[str, Any]) -> tuple[str, str]:
    """Genera (titulo, resumen) legibles para una senal."""
    actor_label = ACTOR_LABEL.get(sig.get("actor_type"), "Actor")
    actor = sig.get("actor_name", "")
    ticker = sig.get("ticker") or sig.get("asset_name", "")
    verb = DIRECTION_VERB.get(sig.get("direction"), "opero")
    amount = _fmt_amount(sig.get("amount_estimated"))
    src = sig.get("source_type", "")

    title = f"{actor_label} {verb} {ticker}".strip()
    if amount:
        title += f" ({amount})"

    parts = [f"{actor_label} {actor}".strip(), verb, ticker]
    if amount:
        parts.append(f"por {amount}")
    if sig.get("ownership_pct"):
        parts.append(f"({sig['ownership_pct']}% de la clase)")
    if sig.get("event_date"):
        parts.append(f"el {sig['event_date']}")
    if sig.get("cross_source_score", 0) > 0:
        parts.append("[senal en multiples fuentes]")
    summary = " ".join(str(p) for p in parts if p) + "."
    return title, summary


def build() -> dict[str, Any]:
    """Construye el objeto top_movements con las N senales mas importantes."""
    signals = _load("signals_30d.json")
    news = _load("news_context_30d.json")

    # Indexar noticias por ticker para enlazarlas.
    news_by_ticker: dict[str, list[str]] = {}
    for a in news:
        for tk in a.get("tickers_detected", []):
            news_by_ticker.setdefault(tk, []).append(a["id"])

    signals_sorted = sorted(signals, key=lambda s: s.get("importance_score", 0), reverse=True)
    movements = []
    for rank, sig in enumerate(signals_sorted[:TOP_N], start=1):
        title, summary = _title_and_summary(sig)
        movements.append({
            "id": f"move_{rank}",
            "rank": rank,
            "title": title,
            "summary": summary,
            "source": sig.get("source"),
            "source_type": sig.get("source_type"),
            "actor_name": sig.get("actor_name"),
            "actor_type": sig.get("actor_type"),
            "ticker": sig.get("ticker"),
            "direction": sig.get("direction"),
            "amount_estimated": sig.get("amount_estimated"),
            "event_date": sig.get("event_date"),
            "importance_score": sig.get("importance_score"),
            "cross_source_score": sig.get("cross_source_score", 0),
            "related_news": news_by_ticker.get(sig.get("ticker"), [])[:3],
            "source_url": sig.get("source_url"),
        })

    from scrapers._dates import now_utc, rolling_window
    f, t = rolling_window(30)
    return {
        "generated_at": now_utc().isoformat(),
        "window_days": 30,
        "window": {"from": f, "to": t},
        "count": len(movements),
        "movements": movements,
    }


def run() -> Path:
    """Genera top_movements_30d.json."""
    data = build()
    OUTPUT_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str),
                           encoding="utf-8")
    print(f"[top_movements] {data['count']} movimientos -> {OUTPUT_PATH}")
    for m in data["movements"][:5]:
        print(f"  #{m['rank']} [{m['importance_score']}] {m['title']}")
    return OUTPUT_PATH


if __name__ == "__main__":
    run()
