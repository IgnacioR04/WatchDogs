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

# Simbolos indices/macro que resumimos en la seccion de mercado.
_MARKET_KEYS = ["SPY", "QQQ", "IWM", "DIA", "TLT", "IEF", "GLD", "^VIX", "BTC-USD"]
# Series FRED clave.
_MACRO_KEYS = ["DGS2", "DGS10", "T10Y2Y", "FEDFUNDS", "BAMLH0A0HYM2",
               "UNRATE", "T10YIE", "DTWEXBGS"]


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
        f"-> **presupuesto de riesgo recomendado: {_pct(regime.get('recommended_risk_budget'))}** "
        "(exposicion maxima a activos; el resto en cash)",
        f"- Volatilidad: `{vol.get('state', 'n/d')}` (VIX {vol.get('vix', 'n/d')})",
        f"- Tendencia: `{tr.get('state', 'n/d')}` "
        f"(SPY {tr.get('close', 'n/d')} · MA50 {tr.get('ma50', 'n/d')} · "
        f"MA200 {tr.get('ma200', 'n/d')} · dist MA200: {tr.get('pct_vs_ma200', 'n/d')}%)",
        f"- Credito: `{cr.get('state', 'n/d')}` (HY spread {cr.get('hy_spread', 'n/d')})",
        f"- Tipos: `{ra.get('state', 'n/d')}` (curva 10y-2y {ra.get('curve_10y2y', 'n/d')})",
    ]
    ctx = regime.get("context", {})
    if ctx.get("fed_funds") is not None:
        lines.append(f"- Fed Funds: {ctx['fed_funds']}%")
    reasons = regime.get("reasons") or []
    if reasons:
        lines.append(f"- Motivos: {'; '.join(reasons)}")
    # Warning si faltan datos macro
    unknowns = [k for k in ["credit", "rates"] if st.get(k, {}).get("state") == "unknown"]
    if unknowns:
        lines.append(f"- **AVISO**: sin datos de {', '.join(unknowns)} (FRED API key no configurada). "
                     "El presupuesto de riesgo puede ser impreciso.")
    lines.append("")
    return lines


def _sec_portfolio(prop: dict, market: dict[str, dict]) -> list[str]:
    lines = [
        "## 2. Cartera CANDIDATA (propuesta por el codigo)",
        "",
        f"Perfil **{prop.get('profile', 'n/d')}** · exposicion total "
        f"**{_pct(prop.get('total_equity'))}** · cash **{_pct(prop.get('cash'))}** · "
        f"gate **{'PASS' if prop.get('risk_gate', {}).get('passed') else 'REJECT'}**",
        "",
        "| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |",
        "|--------|-----:|--------|-------:|-------:|-------:|--------:|",
    ]
    core = set(prop.get("core", {}))
    for tk, w in prop.get("weights", {}).items():
        bloque = "core" if tk in core else "satellite"
        r = market.get(tk, {})
        close = r.get("close", "?")
        r1 = f"{r.get('ret_1d')}%" if r.get("ret_1d") is not None else "?"
        r5 = f"{r.get('ret_5d')}%" if r.get("ret_5d") is not None else "?"
        r20 = f"{r.get('ret_20d')}%" if r.get("ret_20d") is not None else "?"
        lines.append(f"| {tk} | {_pct(w)} | {bloque} | {close} | {r1} | {r5} | {r20} |")
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
            sources = ", ".join(r.get("sources", []))
            lines.append(
                f"- **{r['ticker']}** · score agregado {r.get('score')} · "
                f"{r.get('n_signals')} señales · fuentes: {sources}")
        lines.append("")
    return lines


def _sec_signals(signals: list[dict], limit_buy: int = 15, limit_sell: int = 8) -> list[str]:
    buys = [s for s in signals
            if s.get("direction") in ("buy", "stake") and s.get("ticker")]
    sells = [s for s in signals
             if s.get("direction") == "sell" and s.get("ticker")]

    buys.sort(key=lambda s: s.get("signal_score") or s.get("importance_score") or 0,
              reverse=True)
    sells.sort(key=lambda s: s.get("signal_score") or s.get("importance_score") or 0,
               reverse=True)

    def _score(s: dict) -> str:
        v = s.get("signal_score") or s.get("importance_score") or 0
        return f"{v:.0f}" if isinstance(v, float) else str(v)

    lines = [
        "## 3. Señales de smart money (30d)",
        "",
        "### 3a. Compras (buy signals)",
        "",
        "| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |",
        "|--------|------:|--------|-------|--------:|--------:|-------|",
    ]
    for s in buys[:limit_buy]:
        flags = ",".join(s.get("risk_flags", [])) or "-"
        cluster = s.get("cluster_size", "")
        amt = s.get("amount_estimated")
        amt_str = f"${amt:,.0f}" if amt and amt > 0 else "-"
        lines.append(
            f"| {s['ticker']} | {_score(s)} | "
            f"{s.get('source_type', '')} | {(s.get('actor_name') or '')[:25]} | "
            f"{cluster} | {amt_str} | {flags} |")
    lines.append("")

    if sells:
        lines += [
            "### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes",
            "",
            "| Ticker | Score | Fuente | Actor | Importe | Flags |",
            "|--------|------:|--------|-------|--------:|-------|",
        ]
        for s in sells[:limit_sell]:
            flags = ",".join(s.get("risk_flags", [])) or "-"
            amt = s.get("amount_estimated")
            amt_str = f"${amt:,.0f}" if amt and amt > 0 else "-"
            lines.append(
                f"| {s['ticker']} | {_score(s)} | "
                f"{s.get('source_type', '')} | {(s.get('actor_name') or '')[:25]} | "
                f"{amt_str} | {flags} |")
        lines.append("")

    lines += [
        "> **Cluster** = n de insiders distintos comprando el mismo ticker "
        "(señal de conviccion). **Score** = importancia individual de la señal.",
        "> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en "
        "la seccion 2 (satellite rationale). Un ticker con score agregado alto y "
        "multiples fuentes distintas tiene mayor conviccion.",
        "",
    ]
    return lines


def _sec_market(market_list: list[dict], macro: list[dict]) -> list[str]:
    mkt = {m["symbol"]: m for m in market_list if isinstance(m, dict)}
    mac = {m["series_id"]: m for m in macro if isinstance(m, dict)}
    lines = ["## 4. Snapshot de mercado y macro", "", "**Indices y activos de referencia:**", ""]
    for sym in _MARKET_KEYS:
        r = mkt.get(sym)
        if not r:
            continue
        lines.append(
            f"- {sym}: {r.get('close')} "
            f"({r.get('ret_1d')}% / {r.get('ret_5d')}% / {r.get('ret_20d')}%) "
            f"[{r.get('date', '?')}]")
    lines += ["", "**Macro (valor · cambio 1m):**", ""]
    any_macro = False
    for sid in _MACRO_KEYS:
        r = mac.get(sid)
        if not r:
            continue
        any_macro = True
        lines.append(f"- {r.get('name', sid)}: {r.get('value')} "
                     f"(delta 1m: {r.get('change_1m')}) [{r.get('date', '?')}]")
    if not any_macro:
        lines.append("- _(sin datos macro — FRED API key no configurada en CI)_")
    lines.append("")
    return lines


def _sec_world(news: list[dict], movements: list[dict],
               smart: list[dict], limit_news: int = 10) -> list[str]:
    """Seccion 5: noticias, temas dominantes y apuestas de Polymarket.

    Da al LLM el 'como va el mundo': titulares del periodo, los movimientos de
    actores mas importantes ya resumidos en lenguaje natural, y hacia donde
    apuesta el smart money de Polymarket.
    """
    lines = ["## 5. Noticias y contexto del mundo (30d)", ""]

    # Temas dominantes en titulares.
    theme_counts: dict[str, int] = {}
    for a in news:
        for th in a.get("themes", []):
            theme_counts[th] = theme_counts.get(th, 0) + 1
    if theme_counts:
        top = sorted(theme_counts.items(), key=lambda kv: kv[1], reverse=True)[:6]
        lines.append("**Temas dominantes**: " + ", ".join(f"{t} ({n})" for t, n in top))
        lines.append("")

    # Titulares recientes de los tickers mas activos.
    if news:
        lines.append("**Titulares recientes (GDELT, tickers con mas señales):**")
        lines.append("")
        for a in news[:limit_news]:
            tk = (a.get("tickers_detected") or [""])[0]
            date = (a.get("published_at") or "")[:10]
            title = (a.get("title") or "").strip()
            lines.append(f"- [{tk}] {title} ({date})")
        lines.append("")
    else:
        lines.append("_(sin noticias este ciclo — GDELT no disponible)_")
        lines.append("")

    # Actores que han generado cambio (resumen legible de top movements).
    if movements:
        lines.append("**Actores que han movido ficha este mes (top movimientos):**")
        lines.append("")
        for m in movements[:8]:
            lines.append(f"- {m.get('summary', m.get('title', ''))}")
        lines.append("")

    # Polymarket: donde apuesta el smart money (contexto de eventos del mundo).
    if smart:
        lines.append("**Polymarket — smart money (traders con mejor track record):**")
        lines.append("")
        for t in smart[:5]:
            cats = ", ".join(t.get("categories", [])) or "n/d"
            wr = t.get("win_rate")
            wr_s = f"{wr:.0%}" if isinstance(wr, (int, float)) else "n/d"
            pnl = t.get("pnl")
            pnl_s = f"${pnl:,.0f}" if isinstance(pnl, (int, float)) else "n/d"
            lines.append(f"- {t.get('username') or t.get('wallet', '')[:10]} · "
                         f"PnL {pnl_s} · win rate {wr_s} · categorias: {cats}")
        lines.append("")
        lines.append("> Polymarket refleja en que eventos del mundo (politica, macro, "
                     "deportes) esta apostando el dinero con mejor historial. Usalo como "
                     "termometro de contexto, no como señal directa de cartera.")
        lines.append("")
    return lines


def _sec_quality(health: dict) -> list[str]:
    lines = ["## 6. Calidad de los datos", ""]
    lines.append(f"- Estado global: `{health.get('overall_status', 'unknown')}`")
    ds = health.get("datasets", {})
    for name, v in ds.items():
        st = v.get("status", "?")
        recs = v.get("records_30d", v.get("records_total", "?"))
        latest = v.get("latest_tx_date") or v.get("latest_filing_date") or "?"
        issues = v.get("issues", [])
        issue_str = f" — {', '.join(issues)}" if issues else ""
        lines.append(f"- **{name}**: `{st}` · {recs} registros 30d · ultimo dato {latest}{issue_str}")
    bad = [k for k, v in ds.items() if v.get("status") not in ("ok", "healthy", None)]
    if bad:
        lines.append(f"- **Fuentes con problemas**: {', '.join(bad)}")
    lines += [
        "",
        "> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. "
        "Insiders (Form 4) llegan en 1-2 dias.",
        "",
    ]
    return lines


def _sec_instructions(prop: dict, regime: dict) -> list[str]:
    profile = get_profile(prop.get("profile", "moderado"))
    budget = regime.get("recommended_risk_budget", 0.6)
    universe = sorted(prop.get("weights", {}).keys())
    return [
        "## 7. Instrucciones para ti (LLM)",
        "",
        "Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha "
        "construido la cartera candidata de la seccion 2 a partir de reglas "
        "deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. "
        "El codigo tendra la ultima palabra: validara tu propuesta contra el risk "
        "gate y rechazara cualquier cosa que viole las restricciones.",
        "",
        "### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)",
        "",
        f"1. **Universo permitido**: tickers de la cartera candidata "
        f"(`{', '.join(universe)}`) o de las señales de la seccion 3, siempre "
        "que tengan datos de precio. No inventes tickers que no aparezcan en "
        "este briefing.",
        f"2. **Presupuesto de riesgo**: la suma de todos los pesos <= **{_pct(budget)}** "
        f"(el resto es cash). Estamos en regimen `{regime.get('risk_state', 'n/d')}`.",
        f"3. **Peso maximo por posicion**: <= **{_pct(profile.max_position)}**.",
        "4. **Sin apalancamiento y sin cortos**: todos los pesos >= 0, suma <= 1.",
        "5. **Justifica cada cambio** con una razon concreta basada en los datos de "
        "este briefing (señal, regimen, riesgo, precio). Nada de datos externos.",
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
        "- `final_weights` = cartera COMPLETA que propones. Es lo unico que el codigo "
        "ejecuta. El cash es lo que sobra hasta 1.0 (no lo pongas en final_weights).",
        "- Si tu veredicto es `accept`, copia los pesos exactos de la seccion 2.",
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
    market_list = _load("market_prices_latest.json")
    macro = _load("macro_latest.json")
    health = _load("health_report.json", default={})
    news = _load("news_context_30d.json")
    top_moves = _load("top_movements_30d.json", default={})
    movements = top_moves.get("movements", []) if isinstance(top_moves, dict) else []
    smart = _load("polymarket_smart_traders.json")

    # Indexar precios por simbolo para las tablas de cartera.
    market = {m["symbol"]: m for m in market_list if isinstance(m, dict)}

    f, t = rolling_window(30)
    head = [
        "# WATCHDOG — Briefing diario para el LLM",
        "",
        f"_Generado {now_utc().isoformat(timespec='seconds')} · "
        f"ventana señales {f} -> {t}_",
        "",
        "Este documento contiene todo lo que necesitas para revisar la cartera. "
        "Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> "
        "noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.",
        "",
        "---",
        "",
    ]

    parts: list[str] = head
    parts += _sec_regime(regime)
    parts += _sec_portfolio(prop, market)
    parts += _sec_signals(signals)
    parts += _sec_market(market_list, macro)
    parts += _sec_world(news, movements, smart)
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
