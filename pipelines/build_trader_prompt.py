"""Ensambla el prompt COMPLETO del gestor de cartera (paper trading).

Junta en un unico fichero pegable a un LLM, en orden:

  1. prompts/paper_trader_system_prompt.md  -> las reglas (fijo)
  2. Estado actual de la cartera             -> lo que el LLM gestiona ahora
  3. data/public/daily_context.md            -> los datos frescos de los scrapers

Asi el usuario solo tiene que leer/copiar UN archivo (data/public/trader_prompt.md)
y pegarlo en el chat con el LLM. La respuesta del LLM se valida con
validate_llm_output.py.

El estado de la cartera sale de data/public/llm_portfolio.json (ultima cartera
APROBADA); si no existe todavia, es arranque en frio (100% efectivo).

Salida: data/public/trader_prompt.md
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PUBLIC_DIR = REPO / "data" / "public"
SYSTEM_PROMPT = REPO / "prompts" / "paper_trader_system_prompt.md"
DAILY_CONTEXT = PUBLIC_DIR / "daily_context.md"
PORTFOLIO_STATE = PUBLIC_DIR / "llm_portfolio.json"
OUTPUT_PATH = PUBLIC_DIR / "trader_prompt.md"

BUDGET_EUR = 100.0


def _portfolio_state_md() -> str:
    """Bloque markdown con el estado actual de la cartera que gestiona el LLM."""
    lines = ["## Estado actual de tu cartera (lo que gestionas AHORA)", ""]
    if PORTFOLIO_STATE.exists():
        try:
            st = json.loads(PORTFOLIO_STATE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            st = None
        if st and st.get("approved") and st.get("final_weights"):
            w = st["final_weights"]
            invested = sum(w.values())
            cash = round(1 - invested, 4)
            lines.append(f"_Ultima cartera aprobada: {st.get('generated_at', 'n/d')}_")
            lines.append("")
            lines.append("| Ticker | Peso | Valor (de 100 €) |")
            lines.append("|--------|-----:|-----------------:|")
            for t, wt in sorted(w.items(), key=lambda kv: kv[1], reverse=True):
                lines.append(f"| {t} | {wt*100:.1f}% | {wt*BUDGET_EUR:.2f} € |")
            lines.append(f"| **EFECTIVO** | **{cash*100:.1f}%** | **{cash*BUDGET_EUR:.2f} €** |")
            lines.append("")
            lines.append("Decide sobre ESTA cartera: mantener, vender, reducir, "
                         "comprar o añadir, respetando las reglas de la seccion de arriba.")
            lines.append("")
            return "\n".join(lines)
    # Arranque en frio
    lines += [
        "**Arranque en frio**: aun no hay cartera. Tienes **100,00 € en efectivo "
        "(100%)**, sin posiciones.",
        "",
        "Construye la cartera inicial partiendo de la cartera candidata del "
        "briefing y las señales de mayor conviccion, dentro del presupuesto de "
        "riesgo del regimen. Es valido dejar parte en efectivo si el regimen es defensivo.",
        "",
    ]
    return "\n".join(lines)


def build() -> str:
    system = SYSTEM_PROMPT.read_text(encoding="utf-8") if SYSTEM_PROMPT.exists() else \
        "# (falta prompts/paper_trader_system_prompt.md)"
    daily = DAILY_CONTEXT.read_text(encoding="utf-8") if DAILY_CONTEXT.exists() else \
        "## (falta daily_context.md — corre la pipeline v3)"
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")

    return (
        f"<!-- trader_prompt.md generado {stamp} -->\n\n"
        f"{system}\n\n"
        "---\n\n"
        f"{_portfolio_state_md()}\n"
        "---\n\n"
        "# DATOS DE ESTE CICLO\n\n"
        f"{daily}\n"
    )


def run() -> Path:
    md = build()
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(md, encoding="utf-8")
    size_kb = OUTPUT_PATH.stat().st_size / 1024
    print(f"[trader_prompt] prompt completo generado ({size_kb:.0f} KB) -> {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == "__main__":
    run()
