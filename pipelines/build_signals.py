"""Construye signals_30d.json: capa unificada de senales.

Fusiona las distintas fuentes (insiders SEC, Congress House, 13D/13G, cambios
13F) en un unico schema de senal, aplica el scoring de importancia y calcula
el cross-source score (si un mismo ticker aparece en varias fuentes, su
importancia sube: es una senal mas robusta).

Salida: data/public/signals_30d.json

Schema de senal unificado:
    id, source, source_type, actor_name, actor_type, ticker, asset_name,
    direction, amount_estimated, event_date, disclosure_date, delay_days,
    importance_score + sub-scores, source_url
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from normalize.scoring import score_signal

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
OUTPUT_PATH = PUBLIC_DIR / "signals_30d.json"


# Valores que no son tickers validos (contaminan rankings y cross-source).
_INVALID_TICKERS = {"", "NONE", "N", "A", "PDF", "NA", "N/A", "--"}


def _clean_ticker(t: str | None) -> str:
    """Normaliza un ticker; devuelve '' si no es valido."""
    tk = (t or "").strip().upper()
    return "" if tk in _INVALID_TICKERS else tk


def _load(name: str) -> list[dict]:
    """Carga un dataset publico o devuelve []."""
    p = PUBLIC_DIR / name
    if not p.exists():
        return []
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        return d if isinstance(d, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def _insider_actor_type(title: str) -> str:
    """Infiere el actor_type de un insider a partir de su cargo."""
    t = (title or "").lower()
    if "ceo" in t or "chief executive" in t or "president" in t:
        return "ceo"
    if "cfo" in t or "chief financial" in t:
        return "cfo"
    if "10%" in t or "ten percent" in t:
        return "ten_percent_owner"
    if "director" in t:
        return "director"
    if "officer" in t or "chief" in t or "vp" in t or "vice president" in t:
        return "officer"
    return "insider"


def _from_insiders() -> list[dict[str, Any]]:
    """Mapea Forms 3/4/5 al schema de senal."""
    out = []
    for r in _load("sec_insiders_30d.json"):
        code = (r.get("tx_code") or "").upper()
        direction = "buy" if code in {"P", "M"} else ("sell" if code in {"S", "D"} else "other")
        out.append({
            "id": r.get("id"),
            "source": "sec_form_4",
            "source_type": "corporate_insider",
            "actor_name": r.get("insider_name", ""),
            "actor_type": _insider_actor_type(r.get("insider_title")),
            "ticker": _clean_ticker(r.get("ticker")),
            "asset_name": r.get("company", ""),
            "direction": direction,
            "amount_estimated": r.get("value_usd"),
            "tx_code": code,
            "event_date": r.get("event_date") or r.get("tx_date", ""),
            "known_date": r.get("known_date") or r.get("filing_date") or r.get("tx_date", ""),
            "delay_days": r.get("delay_days"),
            "disclosure_date": r.get("filing_date") or r.get("tx_date", ""),
            "source_url": r.get("source_url", ""),
        })
    return out


def _from_congress() -> list[dict[str, Any]]:
    """Mapea trades de Congress (House parsed ya viene casi en schema)."""
    out = []
    for r in _load("congress_trades_30d.json"):
        # Solo House parsed tiene ticker y scoring; el Senate mirror (si quedara)
        # no aporta ticker fiable -> lo incluimos solo si tiene ticker.
        if not r.get("ticker"):
            continue
        out.append({
            "id": r.get("id"),
            "source": r.get("source", "congress"),
            "source_type": "congress",
            "actor_name": r.get("politician") or r.get("actor_name", ""),
            "actor_type": r.get("actor_type", "house_rep"),
            "ticker": _clean_ticker(r.get("ticker")),
            "asset_name": r.get("asset_name", ""),
            "direction": r.get("direction") or ("buy" if r.get("tx_type") == "purchase" else "sell"),
            "amount_estimated": r.get("amount_estimated") or r.get("amount_max"),
            "event_date": r.get("event_date") or r.get("tx_date", ""),
            "known_date": r.get("known_date") or r.get("disclosure_date", ""),
            "delay_days": r.get("delay_days"),
            "disclosure_date": r.get("disclosure_date", ""),
            "source_url": r.get("source_url", ""),
        })
    return out


def _from_13d_13g() -> list[dict[str, Any]]:
    """Mapea 13D/13G (grandes accionistas)."""
    out = []
    for r in _load("sec_13d_13g_30d.json"):
        # amount_estimated aproximado: shares * (no hay precio) -> usamos None,
        # pero ownership_pct alto es senal fuerte por si misma.
        out.append({
            "id": r.get("id"),
            "source": r.get("source", "sec_13d"),
            "source_type": "large_holder",
            "actor_name": r.get("filer_name", ""),
            "actor_type": "large_holder",
            "ticker": _clean_ticker(r.get("ticker")),
            "asset_name": r.get("company", ""),
            "direction": "stake",
            "amount_estimated": None,
            "ownership_pct": r.get("ownership_pct"),
            "event_date": r.get("event_date", ""),
            "known_date": r.get("known_date") or r.get("filing_date", ""),
            "delay_days": r.get("delay_days"),
            "disclosure_date": r.get("filing_date", ""),
            "source_url": r.get("source_url", ""),
        })
    return out


def _from_13f_changes() -> list[dict[str, Any]]:
    """Mapea cambios 13F (Q vs Q). Suelen no traer ticker (solo cusip/nombre)."""
    out = []
    for r in _load("institutional_changes_latest.json"):
        direction = {"new": "buy", "increased": "buy",
                     "decreased": "sell", "exited": "sell"}.get(r.get("direction"), "hold")
        out.append({
            "id": f"13f_{r.get('manager','')}_{r.get('cusip','')}_{r.get('quarter','')}".replace(" ", "_"),
            "source": "sec_13f",
            "source_type": "institutional",
            "actor_name": r.get("manager", ""),
            "actor_type": "top_institutional_manager",
            "ticker": _clean_ticker(r.get("ticker")),
            "asset_name": r.get("asset_name", ""),
            "direction": direction,
            "amount_estimated": abs(r.get("change_value_usd", 0)) or None,
            "event_date": "",
            "known_date": "",
            "delay_days": None,
            "disclosure_date": "",
            "change_pct": r.get("change_pct"),
            "quarter": r.get("quarter"),
            "source_url": "",
        })
    return out


def _apply_cross_source(signals: list[dict[str, Any]]) -> None:
    """Calcula cross_source_score por ticker (in-place) y re-puntua.

    Si un ticker aparece en N tipos de fuente distintos, su cross_source sube:
    (N-1)/4 acotado a 1.0. Luego se recalcula el importance_score.
    """
    by_ticker: dict[str, set[str]] = {}
    for s in signals:
        tk = s.get("ticker")
        if tk:
            by_ticker.setdefault(tk, set()).add(s.get("source_type", ""))
    for s in signals:
        tk = s.get("ticker")
        n = len(by_ticker.get(tk, set())) if tk else 1
        s["cross_source_score"] = min((n - 1) / 4.0, 1.0)  # 0..1, lo normaliza el scorer
        score_signal(s)  # recalcula importance con el cross-source ya puesto


# Mapeo source_type -> nombre de dataset en el health_report (para gating).
_HEALTH_DATASET = {
    "corporate_insider": "sec_insiders",
    "congress": "congress",
    "large_holder": "sec_13d_13g",
    "institutional": "institutional_13f",
}


def _blocked_source_types() -> set[str]:
    """Devuelve los source_type cuyo dataset esta en estado 'error' (no usar).

    Regla v3: no construir señales con datos health_status != ok. 'warning' se
    permite (se usa pero puede llevar risk_flags); solo 'error' se bloquea.
    """
    # health_report es un dict (no lista), asi que no usamos _load (coacciona a lista).
    p = PUBLIC_DIR / "health_report.json"
    if not p.exists():
        return set()
    try:
        health = json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return set()
    if not isinstance(health, dict):
        return set()
    datasets = health.get("datasets", {})
    blocked = set()
    for st, ds_name in _HEALTH_DATASET.items():
        ds = datasets.get(ds_name, {}) if isinstance(datasets, dict) else {}
        if isinstance(ds, dict) and ds.get("status") == "error":
            blocked.add(st)
    return blocked


def build() -> list[dict[str, Any]]:
    """Construye la lista unificada de senales con scoring, cluster y risk_flags."""
    from normalize.insider_scoring import (
        confidence, detect_clusters, insider_signal_score, risk_flags,
    )

    signals: list[dict[str, Any]] = []
    signals += _from_insiders()
    signals += _from_congress()
    signals += _from_13d_13g()
    signals += _from_13f_changes()

    # Health gating: descartar señales de fuentes en estado 'error'.
    blocked = _blocked_source_types()
    if blocked:
        signals = [s for s in signals if s.get("source_type") not in blocked]

    # Scoring de importancia (con cross-source).
    for s in signals:
        score_signal(s)
    _apply_cross_source(signals)

    # Detectar cluster buying entre las señales de insiders.
    insider_sigs = [s for s in signals if s.get("source_type") == "corporate_insider"]
    clusters = detect_clusters(insider_sigs)

    # Enriquecer cada señal: signal_score, risk_flags, confidence, cluster.
    for s in signals:
        if s.get("source_type") == "corporate_insider":
            s["signal_score"] = insider_signal_score(s, clusters)
            cl = clusters.get((s.get("ticker") or "").upper(), 0)
            s["cluster_size"] = cl
            if cl >= 2:
                s.setdefault("_flags", []).append("cluster_buy")
        else:
            s["signal_score"] = s.get("importance_score", 0)
        rf = risk_flags(s)
        if s.pop("_flags", None):
            rf = ["cluster_buy"] + rf
        s["risk_flags"] = rf
        s["confidence"] = confidence(s)

    # Ordenar por signal_score (la conviccion de la señal) desc.
    signals.sort(key=lambda s: s.get("signal_score", 0), reverse=True)
    return signals


def run() -> Path:
    """Genera signals_30d.json."""
    signals = build()
    OUTPUT_PATH.write_text(json.dumps(signals, indent=2, ensure_ascii=False, default=str),
                           encoding="utf-8")
    by_src: dict[str, int] = {}
    for s in signals:
        by_src[s["source_type"]] = by_src.get(s["source_type"], 0) + 1
    print(f"[build_signals] {len(signals)} senales -> {OUTPUT_PATH}")
    print(f"  por fuente: {by_src}")
    return OUTPUT_PATH


if __name__ == "__main__":
    run()
