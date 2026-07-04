"""Orquestador de la pipeline COMPLETA de WATCHDOG v3.

Encadena todas las fases en orden de dependencia y escribe en data/public/:

  1. SMART MONEY   scrapers (SEC, Congreso, Polymarket)
  2. DERIVADOS     recorte 30d, señales unificadas, noticias, movimientos,
                   contexto LLM legacy, health report
  3. MERCADO       precios (yfinance) + macro (FRED)
  4. DECISION      regimen -> cartera candidata -> informe de riesgo
  5. BRIEFING      daily_context.md (el .md que se pega en el chat con el LLM)

A diferencia de run_all.py (que solo lanza scrapers), este orquestador corre
TODA la cadena, incluidas las capas v3. Es resiliente: si un paso falla, lo
registra y continua con los demas reusando lo que ya hay en data/public/.

Uso:
    python run_pipeline.py                 # pipeline completa
    python run_pipeline.py --from market   # arranca desde 'market' (reusa scrapers previos)
    python run_pipeline.py --only regime,portfolio,risk,context
    python run_pipeline.py --profile agresivo

Notas:
- FRED: si FRED_API_KEY no esta en el entorno, se intenta leer de
  C:/Users/ignac/watchdog-secrets/fred_api_key.txt (fuera del repo).
- El paso 'risk' lee los pesos de portfolio_proposal.json (lo genera 'portfolio').
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

PUBLIC_DIR = Path(__file__).resolve().parent / "data" / "public"
FRED_KEY_FILE = Path(r"C:/Users/ignac/watchdog-secrets/fred_api_key.txt")


def _ensure_fred_key() -> bool:
    """Carga FRED_API_KEY del fichero de secretos si no esta en el entorno."""
    if os.environ.get("FRED_API_KEY", "").strip():
        return True
    if FRED_KEY_FILE.exists():
        os.environ["FRED_API_KEY"] = FRED_KEY_FILE.read_text(encoding="utf-8").strip()
        return True
    return False


# --------------------------------------------------------------------------- #
# Runners de cada paso (import perezoso para que un fallo de deps no tumbe todo)
# --------------------------------------------------------------------------- #

def _step_scrapers():
    import run_all
    run_all.main("all")


def _step_publish():
    from pipelines import publish_public_30d
    publish_public_30d.run()


def _step_signals():
    from pipelines import build_signals
    build_signals.run()


def _step_news():
    from scrapers import news_gdelt
    news_gdelt.run()


def _step_movements():
    from pipelines import build_top_movements
    build_top_movements.run()


def _step_llm_legacy():
    from pipelines import build_llm_context
    build_llm_context.run()


def _step_health():
    from pipelines import build_health_report
    build_health_report.run()


def _step_market():
    from scrapers import market_prices
    market_prices.run()


def _step_macro():
    if not _ensure_fred_key():
        raise RuntimeError(
            "Falta FRED_API_KEY (ni en entorno ni en watchdog-secrets/fred_api_key.txt)")
    from scrapers import macro_fred
    macro_fred.run()


def _step_regime():
    from regime import market_regime
    market_regime.run()


def _step_portfolio(profile: str):
    from portfolio import allocator
    allocator.run(profile)


def _step_risk():
    prop_path = PUBLIC_DIR / "portfolio_proposal.json"
    if not prop_path.exists():
        raise RuntimeError("no hay portfolio_proposal.json (corre antes el paso 'portfolio')")
    weights = json.loads(prop_path.read_text(encoding="utf-8")).get("weights", {})
    if not weights:
        raise RuntimeError("portfolio_proposal.json sin pesos")
    from risk import risk_engine
    risk_engine.run(weights)


def _step_context():
    from pipelines import build_daily_context
    build_daily_context.run()


# Orden canonico de la pipeline. Cada entrada: (nombre, funcion, fase).
def _steps(profile: str):
    return [
        ("scrapers",  _step_scrapers,   "1-SMART MONEY"),
        ("publish",   _step_publish,    "2-DERIVADOS"),
        ("signals",   _step_signals,    "2-DERIVADOS"),
        ("news",      _step_news,       "2-DERIVADOS"),
        ("movements", _step_movements,  "2-DERIVADOS"),
        ("llm_legacy", _step_llm_legacy, "2-DERIVADOS"),
        ("health",    _step_health,     "2-DERIVADOS"),
        ("market",    _step_market,     "3-MERCADO"),
        ("macro",     _step_macro,      "3-MERCADO"),
        ("regime",    _step_regime,     "4-DECISION"),
        ("portfolio", lambda: _step_portfolio(profile), "4-DECISION"),
        ("risk",      _step_risk,       "4-DECISION"),
        ("context",   _step_context,    "5-BRIEFING"),
    ]


def main() -> int:
    ap = argparse.ArgumentParser(description="Pipeline completa WATCHDOG v3")
    ap.add_argument("--from", dest="start", help="arrancar desde este paso")
    ap.add_argument("--only", help="ejecutar solo estos pasos (coma-separados)")
    ap.add_argument("--profile", default="moderado", help="perfil de cartera")
    args = ap.parse_args()

    steps = _steps(args.profile)
    names = [n for n, _, _ in steps]

    if args.only:
        wanted = {s.strip() for s in args.only.split(",")}
        steps = [s for s in steps if s[0] in wanted]
    elif args.start:
        if args.start not in names:
            raise SystemExit(f"paso desconocido: {args.start} (validos: {', '.join(names)})")
        idx = names.index(args.start)
        steps = steps[idx:]

    print(f"Pipeline WATCHDOG v3 — {len(steps)} pasos — perfil {args.profile}\n")
    failed: list[str] = []
    t_all = time.time()
    phase = None
    for name, fn, ph in steps:
        if ph != phase:
            phase = ph
            print(f"\n############ FASE {phase} ############")
        t0 = time.time()
        print(f"\n---------- {name} ----------")
        try:
            fn()
            print(f"[{name}] OK en {time.time() - t0:.1f}s")
        except Exception as e:
            failed.append(name)
            print(f"[{name}] FALLO: {e}")

    dt = time.time() - t_all
    print(f"\n==================================================")
    print(f"Pipeline terminada en {dt:.1f}s — {len(steps) - len(failed)}/{len(steps)} OK")
    if failed:
        print(f"Fallaron: {', '.join(failed)}")
    else:
        print("Todos los pasos OK")
    print(f"Artefactos en: {PUBLIC_DIR}")
    print(f"Briefing LLM:  {PUBLIC_DIR / 'daily_context.md'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
