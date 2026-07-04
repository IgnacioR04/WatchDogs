"""Genera el briefing diario para el LLM (Fase H, modo manual).

Este pipeline NO llama a ninguna API. Empaqueta todo el estado del sistema v3
en un unico documento markdown pegable en un chat con un LLM:

  regimen + presupuesto de riesgo -> cartera CANDIDATA construida por el codigo
  -> metricas de riesgo y veredicto del gate -> mejores señales WATCHDOG
  -> snapshot de mercado y macro -> calidad de datos
  -> instrucciones para el LLM (rol de analista, restricciones DURAS y esquema
     JSON de respuesta que luego validara validate_llm_output.py).

Filosofia: "la IA propone, el codigo decide". El codigo ya propone una cartera;
el LLM actua como analista que la revisa y sugiere AJUSTES dentro de las
restricciones. El codigo tendra la ultima palabra (risk gate) sobre lo que
proponga el LLM.

Salida: data/public/daily_context.md
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from portfolio.constraints import get_profile
from scrapers._dates import now_utc, rolling_window

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
OUTPUT_PATH = PUBLIC_DIR / "daily_context.md"

# Simbolos macro/mercado que resumimos en el briefing (los mas informativos).
_MARKET_KEYS = ["SPY", "QQQ", "IWM", "TLT", "IEF", "GLD", "^VIX", "BTC-USD"]
_MACRO_KEYS = ["DGS2", "DGS10", "T10Y2Y", "FEDFUNDS", "BAMLH0A0HYM2"]


def _load(name: str, default=None):
    p = PUBLIC_DIR / name
    if not p.exists():
        return default if default is not None else []
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default if default is not None else []


def _pct(x: float | None, dec: int = 1) -> str:
    return "n/d" if x is None else f"{x * 100:.{dec}f}%"


# --------------------------------------------------------------------------- #
# Secciones del briefing
# --------------------------------------------------------------------------- #

def _sec_regime(regime: dict) -> list[str]:
    st = regime.get("states", {})
    vol = st.get("volatility", {})
    tr = st.get("trend", {})
    cr = st.get("credit", {})
    ra = st.get("rates", {})
    lines = [
        "## 1. Regimen de mercado",
        "",
        f"- **Estado de riesgo**: `{regime.get('risk_state', 'n/d')}`  "
        f"→ **presupuesto de riesgo recomendado: {_pct(regime.get('recommended_risk_budget'))}** "
        "(exposicion maxima a activos; el resto en cash)",
        f"- Volatilidad: `{vol.get('state', 'n/d')}` (VIX {vol.get('vix', 'n/d')})",
        f"- Tendencia: `{tr.get('state', 'n/d')}` "
        f"(SPY vs MA200: {tr.get('pct_vs_ma200', 'n/d')}%)",
        f"- Credito: `{cr.get('state', 'n/d')}` (HY spread {cr.get('hy_spread', 'n/d')})",
        f"- Tipos: `{ra.get('state', 'n/d')}` (curva 10y-2y {ra.get('curve_10y2y', 'n/d')})",
    ]
    reasons = regime.get("reasons") or []
    if reasons:
        lines.append(f"- Motivos: {'; '.join(reasons)}")
    lines.append("")
    return lines


def _sec_portfolio(prop: dict) -> list[str]:
    lines = [
        "## 2. Cartera CANDIDATA (propuesta por el codigo)",
        "",
        f"Perfil **{prop.get('profile', 'n/d')}** · exposicion total "
        f"**{_pct(prop.get('total_equity'))}** · cash **{_pct(prop.get('cash'))}** · "
        f"gate **{'PASS' if prop.get('risk_gate', {}).get('passed') else 'REJECT'}**",
        "",
        "| Ticker | Peso | Bloque |",
        "|--------|-----:|--------|",
    ]
    core = set(prop.get("core", {}))
    for tk, w in prop.get("weights", {}).items():
        bloque = "core" if tk in core else "satellite"
        lines.append(f"| {tk} | {_pct(w)} | {bloque} |")
    lines.append("")

    m = prop.get("metrics", {})
    lines += [
        "**Metricas de riesgo de esta cartera:**",
        "",
        f"- Volatilidad anualizada: {_pct(m.get('ann_vol'))}",
        f"- VaR 95% 1d: {_pct(m.get('var_95_1d'))} · CVaR 95% 1d: {_pct(m.get('cvar_95_1d'))}",
        f"- Max drawdown historico: {_pct(m.get('max_drawdown'))}",
        f"- Beta vs SPY: {m.get('beta_spy', 'n/d')} · posiciones efectivas: "
        f"{m.get('effective_positions', 'n/d')} · HHI: {m.get('hhi', 'n/d')}",
        "",
    ]
    rats = prop.get("satellite_rationale") or []
    if rats:
        lines.append("**Por que estos satellite (señales WATCHDOG):**")
        lines.append("")
        for r in rats:
            lines.append(
                f"- **{r['ticker']}** · score {r.get('score')} · "
                f"{r.get('n_signals')} señales · fuentes: {', '.join(r.get('sources', []))}")
        lines.append("")
    return lines


def _sec_signals(signals: list[dict], limit: int = 12) -> list[str]:
    buys = [s for s in signals
            if s.get("direction") in ("buy", "stake") and s.get("ticker")]
    buys.sort(key=lambda s: s.get("signal_score") or s.get("importance_score") or 0,
              reverse=True)
    lines = [
        "## 3. Mejores señales de smart money (compra, 30d)",
        "",
        "| Ticker | Score | Fuente | Actor | Cluster | Flags |",
        "|--------|------:|--------|-------|--------:|-------|",
    ]
    for s in buys[:limit]:
        flags = ",".join(s.get("risk_flags", [])) or "-"
        cluster = s.get("cluster_size", "")
        lines.append(
            f"| {s['ticker']} | {s.get('signal_score', s.get('importance_score', 0))} | "
            f"{s.get('source_type', '')} | {(s.get('actor_name') or '')[:22]} | "
            f"{cluster} | {flags} |")
    lines.append("")
    lines.append("> Cluster = nº de insiders distintos comprando el mismo ticker "
                 "(señal de conviccion). Flags = avisos de calidad de la señal.")
    lines.append("")
    return lines


def _sec_market(market: list[dict], macro: list[dict]) -> list[str]:
    mkt = {m["symbol"]: m for m in market if isinstance(m, dict)}
    mac = {m["series_id"]: m for m in macro if isinstance(m, dict)}
    lines = ["## 4. Snapshot de mercado y macro", "", "**Precios (ret 1d / 5d / 20d):**", ""]
    for sym in _MARKET_KEYS:
        r = mkt.get(sym)
        if not r:
            continue
        lines.append(
            f"- {sym}: {r.get('close')} "
            f"({r.get('ret_1d')}% / {r.get('ret_5d')}% / {r.get('ret_20d')}%)")
    lines += ["", "**Macro (valor · cambio 1m):**", ""]
    for sid in _MACRO_KEYS:
        r = mac.get(sid)
        if not r:
            continue
        lines.append(f"- {r.get('name', sid)}: {r.get('value')} "
                     f"(Δ1m {r.get('change_1m')})")
    lines.append("")
    return lines


def _sec_quality(health: dict) -> list[str]:
    lines = ["## 5. Calidad de los datos", ""]
    lines.append(f"- Estado global: `{health.get('overall_status', 'unknown')}`")
    ds = health.get("datasets", {})
    bad = [k for k, v in ds.items() if v.get("status") not in ("ok", "healthy", None)]
    if bad:
        lines.append(f"- Fuentes con problemas: {', '.join(bad)}")
    lines += [
        "- Congreso/13F tienen retraso legal de hasta ~45 dias.",
        "- Senate no disponible en vivo (portal eFD bloqueado); House si.",
        "",
    ]
    return lines


def _sec_instructions(prop: dict, regime: dict) -> list[str]:
    profile = get_profile(prop.get("profile", "moderado"))
    budget = regime.get("recommended_risk_budget", 0.6)
    universe = sorted(prop.get("weights", {}).keys())
    return [
        "## 6. Instrucciones para ti (LLM)",
        "",
        "Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha "
        "construido la cartera candidata de la seccion 2 a partir de reglas "
        "deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. "
        "El codigo tendra la ultima palabra: validara tu propuesta contra el risk "
        "gate y rechazara cualquier cosa que viole las restricciones.",
        "",
        "### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)",
        "",
        f"1. **Universo permitido**: solo puedes usar tickers ya presentes en la "
        f"cartera candidata: `{', '.join(universe)}`. No inventes tickers nuevos "
        "ni uses ninguno sin datos de precio.",
        f"2. **Presupuesto de riesgo**: la suma de todos los pesos ≤ **{_pct(budget)}** "
        f"(el resto es cash). Estamos en regimen `{regime.get('risk_state', 'n/d')}`.",
        f"3. **Peso maximo por posicion**: ≤ **{_pct(profile.max_position)}**.",
        "4. **Sin apalancamiento y sin cortos**: todos los pesos ≥ 0, suma ≤ 1.",
        "5. **Justifica cada cambio** con una razon concreta basada en los datos de "
        "este briefing (señal, regimen, riesgo). Nada de datos externos.",
        "",
        "### Que quiero de ti",
        "",
        "- Un veredicto: aceptar la cartera tal cual (`accept`) o ajustarla (`adjust`).",
        "- Si ajustas: la lista de cambios (subir/bajar/quitar/añadir peso) con su razon.",
        "- Una tesis breve (2-4 frases) y los riesgos clave.",
        "- Tu nivel de confianza (0 a 1).",
        "",
        "### Formato de respuesta OBLIGATORIO",
        "",
        "Responde **solo con este JSON** (sin texto alrededor), para que el codigo "
        "lo pueda validar:",
        "",
        "```json",
        "{",
        '  "verdict": "accept | adjust",',
        '  "adjustments": [',
        '    {"ticker": "XXX", "action": "increase|decrease|remove|add",',
        '     "target_weight": 0.05, "reason": "..."}',
        "  ],",
        '  "final_weights": {"SPY": 0.12, "QQQ": 0.10, "...": 0.0},',
        '  "thesis": "...",',
        '  "key_risks": ["...", "..."],',
        '  "confidence": 0.0',
        "}",
        "```",
        "",
        "- `final_weights` debe contener la cartera COMPLETA que propones (la que el "
        "codigo validara). Si tu veredicto es `accept`, copia los pesos de la seccion 2.",
        "- Si no propones cambios, `adjustments` puede ir vacio.",
        "",
        "**Recuerda**: esto no es asesoramiento financiero; solo hipotesis sobre datos "
        "publicos con retraso legal. Cuantifica la incertidumbre, no afirmes certezas.",
        "",
    ]


# --------------------------------------------------------------------------- #

def build() -> str:
    """Ensambla el briefing markdown completo."""
    regime = _load("regime.json", default={})
    prop = _load("portfolio_proposal.json", default={})
    signals = _load("signals_30d.json")
    market = _load("market_prices_latest.json")
    macro = _load("macro_latest.json")
    health = _load("health_report.json", default={})

    f, t = rolling_window(30)
    head = [
        "# WATCHDOG — Briefing diario para el LLM",
        "",
        f"_Generado {now_utc().isoformat(timespec='seconds')} · "
        f"ventana señales {f} → {t}_",
        "",
        "Este documento contiene todo lo que necesitas para revisar la cartera. "
        "Lee de arriba abajo: regimen → cartera propuesta → señales → mercado → "
        "calidad → instrucciones. Responde segun la seccion 6.",
        "",
        "---",
        "",
    ]

    parts: list[str] = head
    parts += _sec_regime(regime)
    parts += _sec_portfolio(prop)
    parts += _sec_signals(signals)
    parts += _sec_market(market, macro)
    parts += _sec_quality(health)
    parts += _sec_instructions(prop, regime)
    return "\n".join(parts)


def run() -> Path:
    """Genera daily_context.md."""
    md = build()
    OUTPUT_PATH.write_text(md, encoding="utf-8")
    size_kb = OUTPUT_PATH.stat().st_size / 1024
    print(f"[daily_context] briefing generado ({size_kb:.0f} KB, "
          f"{md.count(chr(10)) + 1} lineas) -> {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == "__main__":
    run()
