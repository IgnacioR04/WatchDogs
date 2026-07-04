"""Allocator core-satellite (Fase G v3).

Construye una cartera CANDIDATA:
- CORE: base estable (indices/bonos/oro) segun el perfil.
- SATELLITE: las mejores señales WATCHDOG (mayor signal_score, compra), con
  datos de precio disponibles, ponderadas por inverse-vol.
- CASH: el resto, para respetar el presupuesto de riesgo del regimen.

La exposicion total = min(cap del perfil, presupuesto de riesgo del regimen).
El resultado pasa por el risk engine (validate). Esta es la cartera que luego
el LLM ajusta (Fase H) y el risk engine vuelve a validar.

Salida: data/public/portfolio_proposal.json.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from portfolio.constraints import Profile, get_profile
from portfolio.optimizer import cap_weights, inverse_vol
from risk.risk_engine import RiskLimits, compute_metrics, load_returns_matrix, validate

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
OUTPUT_PATH = PUBLIC_DIR / "portfolio_proposal.json"

# Flags de señal que descalifican un ticker como satellite (baja calidad).
_BAD_FLAGS = {"no_ticker", "low_ticker_confidence", "small_amount"}


def _load(name: str) -> Any:
    p = PUBLIC_DIR / name
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def select_satellite(max_n: int, available: set[str]) -> list[dict[str, Any]]:
    """Selecciona los tickers satellite: mejores señales de compra con precio.

    Agrega por ticker el signal_score de las señales alcistas, penaliza flags
    malos y exige que exista historico de precio (para poder gestionar riesgo).
    Devuelve [{ticker, score, sources, n_signals}].
    """
    signals = _load("signals_30d.json") or []
    agg: dict[str, dict[str, Any]] = {}
    for s in signals:
        tk = (s.get("ticker") or "").upper()
        if not tk or tk not in available:
            continue
        if s.get("direction") not in ("buy", "stake"):
            continue
        flags = set(s.get("risk_flags", []))
        if flags & _BAD_FLAGS:
            continue
        e = agg.setdefault(tk, {"ticker": tk, "score": 0.0, "sources": set(), "n": 0})
        e["score"] += s.get("signal_score") or s.get("importance_score") or 0
        e["sources"].add(s.get("source_type", ""))
        e["n"] += 1
    ranked = sorted(agg.values(), key=lambda x: x["score"], reverse=True)[:max_n]
    return [{"ticker": e["ticker"], "score": round(e["score"], 1),
             "sources": sorted(e["sources"]), "n_signals": e["n"]} for e in ranked]


def build_proposal(profile_name: str = "moderado") -> dict[str, Any]:
    """Construye la cartera candidata para un perfil."""
    profile: Profile = get_profile(profile_name)

    # Presupuesto de riesgo del regimen (si no hay, asumimos neutro 0.6).
    regime = _load("regime.json") or {}
    regime_budget = regime.get("recommended_risk_budget", 0.6)
    total_equity = round(min(profile.max_equity, regime_budget), 4)
    cash = round(1 - total_equity, 4)

    # Necesitamos precios de core + candidatos satellite para inverse-vol y riesgo.
    core_tickers = list(profile.core_weights.keys())
    # Primero cargamos retornos del core + un universo amplio de posibles satellite.
    signals = _load("signals_30d.json") or []
    candidate_tickers = list({(s.get("ticker") or "").upper() for s in signals
                              if s.get("ticker")})
    returns = load_returns_matrix(core_tickers + candidate_tickers)
    available = set(returns.columns)

    # --- CORE ---
    core_norm_total = sum(w for t, w in profile.core_weights.items() if t in available) or 1.0
    core_budget = total_equity * profile.core_fraction
    core = {t: round(w / core_norm_total * core_budget, 4)
            for t, w in profile.core_weights.items() if t in available}

    # --- SATELLITE ---
    picks = select_satellite(profile.max_satellite_positions, available)
    sat_tickers = [p["ticker"] for p in picks]
    sat_budget = total_equity * profile.satellite_fraction
    if sat_tickers:
        sat_w = inverse_vol(sat_tickers, returns)          # suma 1
        satellite = {t: round(w * sat_budget, 4) for t, w in sat_w.items()}
    else:
        satellite = {}
        # sin satellite, el presupuesto satellite va a core proporcionalmente
        if core:
            extra = sat_budget / len(core)
            core = {t: round(w + extra, 4) for t, w in core.items()}

    # --- Combinar y cap por posicion ---
    combined: dict[str, float] = {}
    for d in (core, satellite):
        for t, w in d.items():
            combined[t] = round(combined.get(t, 0) + w, 4)
    combined = cap_weights(combined, profile.max_position)
    # Reescalar exactamente al presupuesto objetivo (el cap+redondeo puede desviar
    # unas milesimas y disparar falsos positivos en el gate de regimen).
    s = sum(combined.values())
    if s > 0:
        combined = {t: round(w * total_equity / s, 4) for t, w in combined.items()}

    # --- Risk gate ---
    limits = RiskLimits(max_position=profile.max_position, max_gross_exposure=1.0)
    metrics = compute_metrics(combined, returns) if combined else {}
    gate = validate(combined, limits, regime_budget=regime_budget, metrics=metrics)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "profile": profile.name,
        "regime_budget": regime_budget,
        "total_equity": round(sum(combined.values()), 4),
        "cash": round(1 - sum(combined.values()), 4),
        "weights": dict(sorted(combined.items(), key=lambda kv: kv[1], reverse=True)),
        "core": core,
        "satellite": satellite,
        "satellite_rationale": picks,
        "metrics": metrics,
        "risk_gate": gate,
    }


def run(profile_name: str = "moderado") -> Path:
    """Genera portfolio_proposal.json para un perfil."""
    prop = build_proposal(profile_name)
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(prop, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[allocator] perfil={prop['profile']} equity={prop['total_equity']} cash={prop['cash']} "
          f"gate={'PASS' if prop['risk_gate']['passed'] else 'REJECT'} -> {OUTPUT_PATH}")
    print(f"  core: {list(prop['core'].keys())}")
    print(f"  satellite: {[p['ticker'] for p in prop['satellite_rationale']]}")
    for v in prop["risk_gate"]["violations"]:
        print(f"  VIOLACION: {v}")
    return OUTPUT_PATH


if __name__ == "__main__":
    import sys
    run(sys.argv[1] if len(sys.argv) > 1 else "moderado")
