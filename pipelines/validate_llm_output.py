"""Valida la respuesta del LLM sobre la cartera (Fase H, cierre del bucle).

Flujo manual: pegas `daily_context.md` en un chat con un LLM, el LLM te
devuelve un JSON con su propuesta, lo guardas en un fichero y lo pasas por aqui.
Este script es el "codigo decide" de "la IA propone, el codigo decide":

  1. Parsea la respuesta del LLM (acepta JSON puro o texto con un bloque ```json).
  2. Comprueba las RESTRICCIONES DURAS contra la cartera candidata y el regimen:
     - universo cerrado (solo tickers de la cartera candidata),
     - sin pesos negativos (ni cortos), suma <= presupuesto de riesgo,
     - peso maximo por posicion segun el perfil.
  3. Pasa `final_weights` por el risk engine (validate).
  4. Si todo OK -> escribe data/public/llm_portfolio.json (cartera APROBADA).
     Si algo falla -> la RECHAZA y explica por que (no se aprueba nada a medias).

Uso:
    python -m pipelines.validate_llm_output ruta/a/respuesta_llm.txt
    python -m pipelines.validate_llm_output            # lee data/public/llm_response.txt
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from portfolio.constraints import get_profile
from risk.risk_engine import RiskLimits, compute_metrics, load_returns_matrix, validate

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
DEFAULT_INPUT = PUBLIC_DIR / "llm_response.txt"
OUTPUT_PATH = PUBLIC_DIR / "llm_portfolio.json"

TOL = 1e-3  # tolerancia de redondeo, coherente con el risk engine


def _load_json(name: str, default=None):
    p = PUBLIC_DIR / name
    if not p.exists():
        return default
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default


def parse_llm_response(text: str) -> dict[str, Any]:
    """Extrae el JSON de la respuesta del LLM (puro o dentro de un bloque ```json)."""
    text = text.strip()
    # Bloque markdown ```json ... ```
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if m:
        return json.loads(m.group(1))
    # Primer objeto {...} que aparezca
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if m:
        return json.loads(m.group(0))
    raise ValueError("no se encontro ningun objeto JSON en la respuesta del LLM")


def _signal_tickers() -> set[str]:
    """Tickers presentes en las señales del briefing (universo ampliado).

    El system prompt permite operar tickers de la cartera candidata O de las
    señales, siempre que tengan datos de precio. Esta funcion da la segunda
    mitad de ese universo; la disponibilidad de precio se comprueba aparte.
    """
    signals = _load_json("signals_30d.json", default=[]) or []
    return {(s.get("ticker") or "").upper() for s in signals if s.get("ticker")}


def _held_tickers() -> set[str]:
    """Posiciones de la ultima cartera APROBADA.

    Mantener una posicion ya abierta siempre es legal, aunque su señal haya
    salido de la ventana de 30 dias: si no, el validador forzaria una venta
    implicita, contradiciendo el sesgo "mantener por defecto" del system prompt.
    """
    st = _load_json("llm_portfolio.json", default=None)
    if st and st.get("approved") and st.get("final_weights"):
        return {str(t).upper() for t in st["final_weights"]}
    return set()


def check_hard_constraints(weights: dict[str, float], allowed: set[str],
                           budget: float, max_position: float) -> list[str]:
    """Comprueba las restricciones duras. Devuelve la lista de violaciones."""
    v: list[str] = []
    unknown = [t for t in weights if t not in allowed]
    if unknown:
        v.append(f"tickers fuera del universo permitido: {', '.join(sorted(unknown))}")
    neg = [t for t, w in weights.items() if w < -TOL]
    if neg:
        v.append(f"pesos negativos (cortos no permitidos): {', '.join(neg)}")
    over = [f"{t} {w:.1%}" for t, w in weights.items() if w > max_position + TOL]
    if over:
        v.append(f"exceden el peso maximo {max_position:.0%}: {', '.join(over)}")
    total = sum(weights.values())
    if total > budget + TOL:
        v.append(f"exposicion {total:.2%} > presupuesto de riesgo {budget:.2%}")
    if total > 1 + TOL:
        v.append(f"apalancamiento: suma de pesos {total:.2%} > 100%")
    return v


def validate_response(text: str) -> dict[str, Any]:
    """Valida la respuesta del LLM contra la cartera candidata y el regimen."""
    prop = _load_json("portfolio_proposal.json", default={})
    regime = _load_json("regime.json", default={})
    if not prop:
        raise RuntimeError("no hay portfolio_proposal.json (corre antes la pipeline v3)")

    profile = get_profile(prop.get("profile", "moderado"))
    budget = regime.get("recommended_risk_budget", 0.6)
    # Universo permitido = cartera candidata + tickers de las señales (igual
    # que el system prompt) + posiciones ya abiertas (mantener siempre es
    # legal). La existencia de datos de precio se exige despues.
    allowed = set(prop.get("weights", {}).keys()) | _signal_tickers() | _held_tickers()

    parsed = parse_llm_response(text)
    weights = {str(k).upper(): float(v) for k, v in (parsed.get("final_weights") or {}).items()
               if v is not None and float(v) > 0}

    result: dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "verdict_llm": parsed.get("verdict"),
        "thesis": parsed.get("thesis"),
        "key_risks": parsed.get("key_risks"),
        "confidence": parsed.get("confidence"),
        "adjustments": parsed.get("adjustments"),
        "final_weights": weights,
    }

    if not weights:
        result["approved"] = False
        result["violations"] = ["la respuesta no trae 'final_weights' con pesos > 0"]
        return result

    hard = check_hard_constraints(weights, allowed, budget, profile.max_position)

    # Risk gate (mismas reglas que el allocator)
    returns = load_returns_matrix(list(weights.keys()))
    # Regla dura: todo ticker propuesto debe tener historico de precio (sin el
    # no se puede medir su riesgo). Coherente con el system prompt.
    no_price = sorted(t for t in weights if t not in returns.columns)
    if no_price:
        hard.append(f"sin datos de precio (imposible medir riesgo): {', '.join(no_price)}")
    # Regla dura de liquidez para posiciones NUEVAS (las ya abiertas se pueden
    # mantener): precio >= $5 y volumen medio >= $2M. En papel se ejecuta al
    # cierre oficial; sin liquidez real ese precio es una ficcion.
    from portfolio.allocator import liquidity_ok
    held = _held_tickers()
    illiquid = sorted(t for t in weights
                      if t not in held and t in returns.columns and not liquidity_ok(t))
    if illiquid:
        hard.append("liquidez insuficiente para abrir posicion "
                    f"(precio < $5 o volumen medio < $2M/dia): {', '.join(illiquid)}")
    metrics = compute_metrics(weights, returns)
    limits = RiskLimits(max_position=profile.max_position, max_gross_exposure=1.0)
    gate = validate(weights, limits, regime_budget=budget, metrics=metrics)

    violations = hard + [f"risk gate: {x}" for x in gate.get("violations", [])]
    result["metrics"] = metrics
    result["risk_gate"] = gate
    result["violations"] = violations
    result["approved"] = len(violations) == 0
    return result


def _append_to_ledger(res: dict[str, Any]) -> None:
    """Añade la cartera aprobada al ledger historico (data/public/paper_ledger.json).

    El ledger es la fuente de verdad del paper trading: cada rebalanceo aprobado
    queda registrado con su fecha, y build_paper_metrics lo usa para valorar la
    cartera dia a dia (equity curve, Sharpe, win rate...).
    """
    ledger_path = PUBLIC_DIR / "paper_ledger.json"
    ledger = _load_json("paper_ledger.json", default=[]) or []
    entry = {
        "approved_at": res["generated_at"],
        "weights": res["final_weights"],
        "verdict_llm": res.get("verdict_llm"),
        "thesis": res.get("thesis"),
        "confidence": res.get("confidence"),
        "n_adjustments": len(res.get("adjustments") or []),
    }
    # Idempotencia: si se re-valida la misma respuesta, no duplicar el ciclo.
    if ledger and ledger[-1].get("weights") == entry["weights"]:
        ledger[-1] = entry
    else:
        ledger.append(entry)
    ledger_path.write_text(json.dumps(ledger, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  ledger: ciclo #{len(ledger)} registrado en {ledger_path.name}")


def run(input_path: Path | None = None) -> Path:
    """Valida la respuesta del LLM. Solo una cartera APROBADA pisa llm_portfolio.json.

    Un rechazo se escribe en llm_validation_rejected.json: si machacara
    llm_portfolio.json, el siguiente trader_prompt perderia la cartera viva
    y volveria a arranque en frio.
    """
    src = input_path or DEFAULT_INPUT
    if not src.exists():
        raise SystemExit(
            f"No existe {src}. Guarda la respuesta del LLM en ese fichero (o pasa la ruta como argumento).")
    res = validate_response(src.read_text(encoding="utf-8"))
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_PATH if res.get("approved") else PUBLIC_DIR / "llm_validation_rejected.json"
    out.write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    if res.get("approved"):
        _append_to_ledger(res)

    estado = "APROBADA (OK)" if res.get("approved") else "RECHAZADA"
    print(f"[validate_llm] cartera {estado} (veredicto LLM: {res.get('verdict_llm')}) -> {out}")
    if res.get("approved"):
        m = res.get("metrics", {})
        print(f"  posiciones: {len(res['final_weights'])} · vol {m.get('ann_vol')} · maxDD {m.get('max_drawdown')}")
    else:
        print("  (la ultima cartera aprobada en llm_portfolio.json queda intacta)")
    for v in res.get("violations", []):
        print(f"  VIOLACION: {v}")
    return out


if __name__ == "__main__":
    run(Path(sys.argv[1]) if len(sys.argv) > 1 else None)
