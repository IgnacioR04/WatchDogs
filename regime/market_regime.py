"""Motor de regimen de mercado (Fase E v3).

Entiende el entorno de mercado con REGLAS SIMPLES Y AUDITABLES: cada estado
lleva los valores que lo justifican (evidencia), para poder revisarlo a mano.
Modelos mas sofisticados (HMM/clustering) vendran despues.

Estados que calcula:
- volatility_state: nivel de VIX.
- trend_state: SPY vs sus medias moviles 50/200.
- credit_state: high yield spread (FRED) — estres de credito.
- rates_state: curva 10Y-2Y (invertida = senal de recesion).
- risk_state: compuesto risk_on / neutral / risk_off.
- recommended_risk_budget: 0-1, cuanto riesgo asumir dado el entorno.

Lee el historico de precios (parquet) y macro (jsonl.gz) de WATCHDOG_HISTORY.
Salida: data/public/regime.json.
"""

from __future__ import annotations

import gzip
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
HISTORY_DIR = Path(os.environ.get("WATCHDOG_HISTORY_DIR", r"G:/Mi unidad/WATCHDOG_HISTORY"))
PRICES_DIR = HISTORY_DIR / "normalized" / "prices"
MACRO_DIR = HISTORY_DIR / "normalized" / "macro"
OUTPUT_PATH = PUBLIC_DIR / "regime.json"


def _safe_symbol(symbol: str) -> str:
    """Nombre de fichero de un simbolo (igual que market_prices)."""
    return symbol.replace("^", "IDX_").replace("-", "_").replace("/", "_")


def load_closes(symbol: str, years: int = 2) -> pd.Series:
    """Carga la serie de cierres diarios de un simbolo (ultimos `years` anos)."""
    safe = _safe_symbol(symbol)
    base = PRICES_DIR / f"symbol={safe}" / "timeframe=1d"
    if not base.exists():
        return pd.Series(dtype=float)
    files = sorted(base.rglob("*.parquet"))[-(years + 1):]
    frames = []
    for f in files:
        try:
            df = pd.read_parquet(f)
            if "Close" in df.columns:
                frames.append(df["Close"])
        except Exception:
            continue
    if not frames:
        return pd.Series(dtype=float)
    s = pd.concat(frames)
    s.index = pd.to_datetime(s.index)
    return s.sort_index().dropna()


def _fallback_macro_from_snapshot(series_id: str) -> dict[str, Any] | None:
    """Fallback: lee de macro_latest.json cuando no hay jsonl.gz en el history."""
    snapshot = PUBLIC_DIR / "macro_latest.json"
    if not snapshot.exists():
        return None
    try:
        data = json.loads(snapshot.read_text(encoding="utf-8"))
        for entry in data:
            if entry.get("series_id") == series_id:
                return {"value": entry.get("value"), "date": entry.get("date")}
    except (json.JSONDecodeError, OSError):
        pass
    return None


def load_macro_latest(series_id: str) -> dict[str, Any] | None:
    """Devuelve la ultima observacion de una serie macro (jsonl.gz, fallback a snapshot)."""
    path = MACRO_DIR / f"series={series_id}" / f"{series_id}.jsonl.gz"
    if not path.exists():
        return _fallback_macro_from_snapshot(series_id)
    last = None
    try:
        with gzip.open(path, "rt", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        last = json.loads(line)
                    except json.JSONDecodeError:
                        continue
    except OSError:
        return _fallback_macro_from_snapshot(series_id)
    return last if last is not None else _fallback_macro_from_snapshot(series_id)


# --- Reglas de estado (cada una devuelve (estado, evidencia)) --------------

def volatility_rule(vix: float | None) -> tuple[str, dict]:
    """VIX: <15 calm, 15-20 normal, 20-28 elevated, >28 stress."""
    if vix is None:
        return "unknown", {"vix": None}
    if vix < 15:
        state = "calm"
    elif vix < 20:
        state = "normal"
    elif vix < 28:
        state = "elevated"
    else:
        state = "stress"
    return state, {"vix": round(vix, 2)}


def trend_rule(closes: pd.Series) -> tuple[str, dict]:
    """SPY vs MA50/MA200: bull si close>MA50>MA200, bear si close<MA50<MA200."""
    if len(closes) < 200:
        return "unknown", {}
    close = float(closes.iloc[-1])
    ma50 = float(closes.rolling(50).mean().iloc[-1])
    ma200 = float(closes.rolling(200).mean().iloc[-1])
    if close > ma50 > ma200:
        state = "bull"
    elif close < ma50 < ma200:
        state = "bear"
    else:
        state = "neutral"
    ev = {"close": round(close, 2), "ma50": round(ma50, 2), "ma200": round(ma200, 2),
          "pct_vs_ma200": round((close / ma200 - 1) * 100, 2)}
    return state, ev


def credit_rule(hy_spread: float | None) -> tuple[str, dict]:
    """High yield spread (OAS): <3 tight (risk-on), 3-4.5 normal, 4.5-6 widening, >6 stress."""
    if hy_spread is None:
        return "unknown", {"hy_spread": None}
    if hy_spread < 3.0:
        state = "tight"
    elif hy_spread < 4.5:
        state = "normal"
    elif hy_spread < 6.0:
        state = "widening"
    else:
        state = "stress"
    return state, {"hy_spread": round(hy_spread, 2)}


def rates_rule(curve: float | None) -> tuple[str, dict]:
    """Curva 10Y-2Y: <0 invertida (recesion), 0-0.5 flat, >0.5 steep."""
    if curve is None:
        return "unknown", {"curve_10y2y": None}
    if curve < 0:
        state = "inverted"
    elif curve < 0.5:
        state = "flat"
    else:
        state = "steep"
    return state, {"curve_10y2y": round(curve, 2)}


# --- Composicion -----------------------------------------------------------

def compose_risk(volatility: str, trend: str, credit: str, rates: str) -> tuple[str, float, list[str]]:
    """Combina los estados en risk_state + recommended_risk_budget (0-1) + razones.

    Reglas auditables:
      base 0.60. bull +0.20 / bear -0.25. VIX stress -0.30 / elevated -0.15.
      credit stress -0.30 / widening -0.15 / tight +0.10. curva invertida -0.15.
    """
    budget = 0.60
    reasons: list[str] = []

    if trend == "bull":
        budget += 0.20; reasons.append("tendencia alcista (+)")
    elif trend == "bear":
        budget -= 0.25; reasons.append("tendencia bajista (-)")

    if volatility == "stress":
        budget -= 0.30; reasons.append("VIX en estres (--)")
    elif volatility == "elevated":
        budget -= 0.15; reasons.append("VIX elevado (-)")
    elif volatility == "calm":
        budget += 0.05; reasons.append("VIX calmado (+)")

    if credit == "stress":
        budget -= 0.30; reasons.append("credito en estres (--)")
    elif credit == "widening":
        budget -= 0.15; reasons.append("spreads ampliando (-)")
    elif credit == "tight":
        budget += 0.10; reasons.append("credito tenso/risk-on (+)")

    if rates == "inverted":
        budget -= 0.15; reasons.append("curva invertida (-)")

    budget = round(max(0.10, min(1.0, budget)), 2)

    # risk_state segun budget
    if budget >= 0.70:
        risk = "risk_on"
    elif budget >= 0.45:
        risk = "neutral"
    else:
        risk = "risk_off"
    return risk, budget, reasons


def build_regime() -> dict[str, Any]:
    """Calcula el regimen completo con evidencia."""
    spy = load_closes("SPY")
    vix_s = load_closes("^VIX")
    vix = float(vix_s.iloc[-1]) if len(vix_s) else None
    hy = load_macro_latest("BAMLH0A0HYM2")
    curve = load_macro_latest("T10Y2Y")
    fed = load_macro_latest("FEDFUNDS")

    vol_state, vol_ev = volatility_rule(vix)
    trend_state, trend_ev = trend_rule(spy)
    credit_state, credit_ev = credit_rule(hy.get("value") if hy else None)
    rates_state, rates_ev = rates_rule(curve.get("value") if curve else None)

    risk_state, budget, reasons = compose_risk(vol_state, trend_state, credit_state, rates_state)

    summary = (f"Mercado {risk_state.replace('_', '-')}: tendencia {trend_state}, "
               f"volatilidad {vol_state}, credito {credit_state}, curva {rates_state}. "
               f"Presupuesto de riesgo recomendado {int(budget*100)}%.")

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "risk_state": risk_state,
        "recommended_risk_budget": budget,
        "summary": summary,
        "reasons": reasons,
        "states": {
            "volatility": {"state": vol_state, **vol_ev},
            "trend": {"state": trend_state, **trend_ev},
            "credit": {"state": credit_state, **credit_ev},
            "rates": {"state": rates_state, **rates_ev},
        },
        "context": {
            "fed_funds": fed.get("value") if fed else None,
            "spy": trend_ev.get("close"),
            "vix": vix_ev if (vix_ev := vol_ev.get("vix")) else None,
        },
    }


def run() -> Path:
    """Genera regime.json en data/public."""
    regime = build_regime()
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(regime, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[regime] {regime['risk_state']} (budget {regime['recommended_risk_budget']}) -> {OUTPUT_PATH}")
    print(f"  {regime['summary']}")
    for k, v in regime["states"].items():
        print(f"  {k}: {v}")
    return OUTPUT_PATH


if __name__ == "__main__":
    run()
