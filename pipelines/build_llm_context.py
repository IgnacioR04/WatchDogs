"""Construye llm_context_30d.json: contexto compacto para un LLM gestor.

Este es el artefacto final del pipeline: un JSON razonablemente compacto que se
le pasa a un LLM para que genere HIPOTESIS de inversion (no consejos) a partir
de datos publicos del ultimo mes. No incluye el raw completo, solo lo relevante:

  metadata, data_quality, market_context, top_movements, top_tickers
  (presion compradora/vendedora), insider_buying, institutional_changes,
  congress_activity, large_holders (13D/13G), polymarket (smart+whales),
  news, y llm_instructions con reglas anti-alucinacion.

Salida: data/public/llm_context_30d.json
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from scrapers._dates import now_utc, rolling_window

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
OUTPUT_PATH = PUBLIC_DIR / "llm_context_30d.json"


def _load(name: str, default=None):
    p = PUBLIC_DIR / name
    if not p.exists():
        return default if default is not None else []
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default if default is not None else []


def _top_tickers(signals: list[dict], limit: int = 15) -> dict[str, list]:
    """Calcula presion compradora y vendedora agregada por ticker."""
    buy = defaultdict(float)
    sell = defaultdict(float)
    meta = {}
    for s in signals:
        tk = s.get("ticker")
        if not tk or tk in {"NONE", "N", "A"}:
            continue
        score = s.get("importance_score", 0)
        meta.setdefault(tk, {"company": s.get("asset_name", ""), "sources": set()})
        meta[tk]["sources"].add(s.get("source_type", ""))
        if s.get("direction") in {"buy", "stake"}:
            buy[tk] += score
        elif s.get("direction") == "sell":
            sell[tk] += score

    def _entry(tk, pressure):
        return {"ticker": tk, "company": meta[tk]["company"],
                "pressure_score": round(pressure, 1),
                "sources": sorted(meta[tk]["sources"])}

    top_buy = sorted(buy.items(), key=lambda kv: kv[1], reverse=True)[:limit]
    top_sell = sorted(sell.items(), key=lambda kv: kv[1], reverse=True)[:limit]
    return {
        "buy_pressure": [_entry(tk, v) for tk, v in top_buy],
        "sell_pressure": [_entry(tk, v) for tk, v in top_sell],
    }


def _insider_buying(signals: list[dict], limit: int = 15) -> list[dict]:
    """Compras de insiders (las mas valiosas: codigo P)."""
    buys = [s for s in signals
            if s.get("source_type") == "corporate_insider"
            and s.get("direction") == "buy" and s.get("ticker")]
    buys.sort(key=lambda s: s.get("importance_score", 0), reverse=True)
    return [{
        "ticker": s["ticker"], "company": s.get("asset_name", ""),
        "actor": s.get("actor_name", ""), "actor_type": s.get("actor_type"),
        "amount": s.get("amount_estimated"), "date": s.get("event_date"),
        "score": s.get("importance_score"),
    } for s in buys[:limit]]


def _congress_activity(signals: list[dict], limit: int = 15) -> list[dict]:
    """Actividad reciente del Congreso (House) con ticker."""
    cong = [s for s in signals if s.get("source_type") == "congress" and s.get("ticker")]
    cong.sort(key=lambda s: s.get("importance_score", 0), reverse=True)
    return [{
        "politician": s.get("actor_name", ""), "ticker": s["ticker"],
        "direction": s.get("direction"), "amount": s.get("amount_estimated"),
        "date": s.get("event_date"), "score": s.get("importance_score"),
    } for s in cong[:limit]]


def _institutional_changes(limit: int = 20) -> list[dict]:
    """Mayores cambios 13F del quarter (por magnitud)."""
    changes = _load("institutional_changes_latest.json")
    changes.sort(key=lambda c: abs(c.get("change_value_usd", 0)), reverse=True)
    return [{
        "manager": c.get("manager"), "asset": c.get("asset_name"),
        "ticker": c.get("ticker", ""), "direction": c.get("direction"),
        "change_usd": c.get("change_value_usd"), "change_pct": c.get("change_pct"),
        "quarter": c.get("quarter"),
    } for c in changes[:limit]]


def _large_holders(limit: int = 15) -> list[dict]:
    """13D/13G recientes con mayor % de propiedad."""
    data = _load("sec_13d_13g_30d.json")
    data = [r for r in data if r.get("ownership_pct")]
    data.sort(key=lambda r: r.get("ownership_pct", 0), reverse=True)
    return [{
        "filer": r.get("filer_name"), "company": r.get("company"),
        "ticker": r.get("ticker", ""), "ownership_pct": r.get("ownership_pct"),
        "shares": r.get("shares_owned"), "filing_type": r.get("filing_type"),
        "date": r.get("filing_date"),
    } for r in data[:limit]]


def _polymarket(limit: int = 10) -> dict:
    """Resumen de smart traders y whales de Polymarket."""
    smart = _load("polymarket_smart_traders.json")[:limit]
    whales = _load("polymarket_whales.json")[:limit]
    def _s(t):
        return {"wallet": t.get("wallet", "")[:12], "username": t.get("username", ""),
                "pnl": t.get("pnl"), "win_rate": t.get("win_rate"),
                "volume": t.get("volume"), "categories": t.get("categories", [])}
    return {"smart_traders": [_s(t) for t in smart], "whales": [_s(t) for t in whales]}


def _market_themes(news: list[dict]) -> list[str]:
    """Temas dominantes en las noticias del periodo."""
    counts = defaultdict(int)
    for a in news:
        for th in a.get("themes", []):
            counts[th] += 1
    return [t for t, _ in sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:6]]


def build() -> dict[str, Any]:
    """Ensambla el contexto LLM completo."""
    signals = _load("signals_30d.json")
    news = _load("news_context_30d.json")
    top_moves = _load("top_movements_30d.json", default={})
    health = _load("health_report.json", default={})

    f, t = rolling_window(30)
    return {
        "project": "WATCHDOG",
        "generated_at": now_utc().isoformat(),
        "window": {"from": f, "to": t, "days": 30},
        "data_quality": {
            "overall_status": health.get("overall_status", "unknown"),
            "notes": [
                "Senate no disponible en vivo (portal eFD bloqueado); House si.",
                "13F lleva retraso legal de ~45 dias; refleja el quarter de consenso.",
                "Congressional disclosures tienen retraso legal de hasta 45 dias.",
            ],
            "datasets": {k: v.get("status") for k, v in health.get("datasets", {}).items()},
        },
        "market_context": {
            "top_themes": _market_themes(news),
            "summary": "Contexto derivado de titulares GDELT de los tickers mas activos.",
        },
        "top_movements": (top_moves.get("movements", []) if isinstance(top_moves, dict) else [])[:20],
        "top_tickers": _top_tickers(signals),
        "insider_buying": _insider_buying(signals),
        "institutional_changes": _institutional_changes(),
        "congress_activity": _congress_activity(signals),
        "large_holders": _large_holders(),
        "polymarket": _polymarket(),
        "news": [{
            "title": a.get("title"), "url": a.get("url"),
            "ticker": (a.get("tickers_detected") or [""])[0],
            "themes": a.get("themes", []), "date": a.get("published_at", "")[:10],
        } for a in news[:30]],
        "signals_count": len(signals),
        "llm_instructions": {
            "role": "Eres un analista que genera HIPOTESIS de inversion, no consejos financieros.",
            "style": "Da hipotesis razonadas, no certezas. Cuantifica la incertidumbre.",
            "must_include": [
                "Limitaciones de los datos y su frescura (delay legal).",
                "Riesgos de cada hipotesis.",
                "Que esto NO es asesoramiento financiero.",
            ],
            "must_not": [
                "Afirmar certezas sobre el precio futuro.",
                "Usar datos privados o no incluidos en este contexto.",
                "Recomendar operaciones concretas como consejo cerrado.",
            ],
            "how_to_use": (
                "Prioriza senales con importance_score alto y cross_source (varias "
                "fuentes apuntando al mismo ticker). El insider buying (codigo P) y "
                "los 13D/13G con alto % suelen ser las senales mas informativas."
            ),
        },
    }


def run() -> Path:
    """Genera llm_context_30d.json."""
    ctx = build()
    OUTPUT_PATH.write_text(json.dumps(ctx, indent=2, ensure_ascii=False, default=str),
                           encoding="utf-8")
    size_kb = OUTPUT_PATH.stat().st_size / 1024
    print(f"[llm_context] generado ({size_kb:.0f} KB) -> {OUTPUT_PATH}")
    print(f"  movimientos: {len(ctx['top_movements'])}, insider_buys: {len(ctx['insider_buying'])}, "
          f"13f_changes: {len(ctx['institutional_changes'])}, large_holders: {len(ctx['large_holders'])}, "
          f"news: {len(ctx['news'])}")
    return OUTPUT_PATH


if __name__ == "__main__":
    run()
