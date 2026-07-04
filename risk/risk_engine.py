"""Risk engine: el CONTROLADOR de WATCHDOG (Fase F v3).

Calcula las metricas de riesgo de una cartera y, sobre todo, ACEPTA o RECHAZA
las propuestas (del LLM o del allocator) contra reglas duras. La IA propone;
este modulo decide. Va ANTES que el LLM a proposito.

Metricas (con precios historicos reales de WATCHDOG_HISTORY):
- Volatilidad anualizada de la cartera.
- VaR y CVaR historicos (95%, 1 dia).
- Max drawdown historico de la cartera.
- Beta vs SPY.
- Concentracion: HHI, peso maximo, nº posiciones efectivas.

Reglas duras (validate): peso maximo por posicion, no apalancar (suma<=1), en
risk-off la exposicion no supera el presupuesto de riesgo del regimen, limite
de volatilidad. Devuelve las violaciones concretas (auditable).

Salida: data/public/risk_report.json.
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
HISTORY_DIR = Path(os.environ.get("WATCHDOG_HISTORY_DIR", r"G:/Mi unidad/WATCHDOG_HISTORY"))
PRICES_DIR = HISTORY_DIR / "normalized" / "prices"
OUTPUT_PATH = PUBLIC_DIR / "risk_report.json"

TRADING_DAYS = 252


@dataclass
class RiskLimits:
    """Reglas duras del risk engine. Auditables y editables."""
    max_position: float = 0.15        # peso maximo por posicion
    max_sector: float = 0.40          # peso maximo por sector (si hay mapa)
    max_ann_vol: float = 0.25         # volatilidad anualizada maxima de la cartera
    max_gross_exposure: float = 1.0   # no apalancar: suma de pesos <= 1
    respect_regime_budget: bool = True  # en risk-off, exposicion <= risk_budget


def _safe_symbol(symbol: str) -> str:
    return symbol.replace("^", "IDX_").replace("-", "_").replace("/", "_")


def load_returns_matrix(tickers: list[str], lookback_days: int = 504) -> pd.DataFrame:
    """Carga los retornos diarios de los tickers desde parquet, alineados.

    Devuelve un DataFrame (fechas x tickers) de retornos diarios. Descarta
    tickers sin datos suficientes.
    """
    series = {}
    for tk in tickers:
        safe = _safe_symbol(tk)
        base = PRICES_DIR / f"symbol={safe}" / "timeframe=1d"
        if not base.exists():
            continue
        files = sorted(base.rglob("*.parquet"))[-3:]
        frames = []
        for f in files:
            try:
                df = pd.read_parquet(f)
                if "Close" in df.columns:
                    frames.append(df["Close"])
            except Exception:
                continue
        if not frames:
            continue
        s = pd.concat(frames)
        s.index = pd.to_datetime(s.index)
        s = s.sort_index().dropna()
        if len(s) > 30:
            series[tk] = s.pct_change().dropna()
    if not series:
        return pd.DataFrame()
    mat = pd.DataFrame(series).dropna()
    return mat.tail(lookback_days)


def portfolio_returns(weights: dict[str, float], returns: pd.DataFrame) -> pd.Series:
    """Serie de retornos diarios de la cartera (solo tickers con datos)."""
    cols = [t for t in weights if t in returns.columns]
    if not cols:
        return pd.Series(dtype=float)
    w = np.array([weights[t] for t in cols])
    return returns[cols].dot(w)


def compute_metrics(weights: dict[str, float], returns: pd.DataFrame) -> dict[str, Any]:
    """Calcula las metricas de riesgo de la cartera."""
    pr = portfolio_returns(weights, returns)
    if pr.empty:
        return {"error": "sin datos de precios para la cartera"}

    ann_vol = float(pr.std() * np.sqrt(TRADING_DAYS))
    var95 = float(-np.percentile(pr, 5))            # perdida en el peor 5% (1 dia)
    tail = pr[pr <= -var95]
    cvar95 = float(-tail.mean()) if len(tail) else var95
    # max drawdown de la cartera
    curve = (1 + pr).cumprod()
    dd = float((curve / curve.cummax() - 1).min())
    # beta vs SPY
    beta = None
    if "SPY" in returns.columns:
        common = pd.concat([pr, returns["SPY"]], axis=1).dropna()
        if len(common) > 30 and common.iloc[:, 1].var() > 0:
            beta = float(common.iloc[:, 0].cov(common.iloc[:, 1]) / common.iloc[:, 1].var())
    # concentracion
    w = np.array(list(weights.values()))
    hhi = float((w ** 2).sum())
    eff_positions = float(1 / hhi) if hhi > 0 else 0
    return {
        "ann_vol": round(ann_vol, 4),
        "var_95_1d": round(var95, 4),
        "cvar_95_1d": round(cvar95, 4),
        "max_drawdown": round(dd, 4),
        "beta_spy": round(beta, 3) if beta is not None else None,
        "hhi": round(hhi, 4),
        "max_position": round(float(w.max()), 4),
        "n_positions": len(weights),
        "effective_positions": round(eff_positions, 1),
        "gross_exposure": round(float(w.sum()), 4),
        "days_used": len(pr),
    }


def validate(weights: dict[str, float], limits: RiskLimits,
             regime_budget: float | None = None,
             metrics: dict[str, Any] | None = None,
             sectors: dict[str, str] | None = None) -> dict[str, Any]:
    """Aplica las reglas duras. Devuelve {passed, violations, adjustments_suggested}.

    El risk engine RECHAZA la propuesta si hay violaciones. La IA propone; esto
    decide.
    """
    violations: list[str] = []
    gross = sum(weights.values())
    # Tolerancia para el redondeo a 4 decimales acumulado sobre decenas de pesos.
    TOL = 1e-3

    # 1. No apalancar
    if gross > limits.max_gross_exposure + TOL:
        violations.append(f"apalancamiento: exposicion bruta {gross:.2f} > {limits.max_gross_exposure}")

    # 2. Peso maximo por posicion
    for tk, w in weights.items():
        if w > limits.max_position + TOL:
            violations.append(f"concentracion: {tk} {w:.1%} > max {limits.max_position:.0%}")

    # 3. En risk-off, exposicion <= presupuesto de riesgo del regimen
    if limits.respect_regime_budget and regime_budget is not None:
        if gross > regime_budget + TOL:
            violations.append(
                f"regimen: exposicion {gross:.2f} > presupuesto de riesgo {regime_budget:.2f} "
                f"(hay que subir cash)")

    # 4. Limite de volatilidad
    if metrics and isinstance(metrics.get("ann_vol"), (int, float)):
        if metrics["ann_vol"] > limits.max_ann_vol + 1e-6:
            violations.append(
                f"volatilidad: {metrics['ann_vol']:.1%} anual > max {limits.max_ann_vol:.0%}")

    # 5. Concentracion sectorial (si hay mapa de sectores)
    if sectors:
        sector_w: dict[str, float] = {}
        for tk, w in weights.items():
            sec = sectors.get(tk, "unknown")
            sector_w[sec] = sector_w.get(sec, 0) + w
        for sec, w in sector_w.items():
            if sec != "unknown" and w > limits.max_sector + 1e-6:
                violations.append(f"sector: {sec} {w:.1%} > max {limits.max_sector:.0%}")

    return {
        "passed": len(violations) == 0,
        "violations": violations,
        "n_violations": len(violations),
    }


def _load_regime_budget() -> float | None:
    """Lee el recommended_risk_budget del regime.json si existe."""
    p = PUBLIC_DIR / "regime.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8")).get("recommended_risk_budget")
    except (json.JSONDecodeError, OSError):
        return None


def build_risk_report(weights: dict[str, float], limits: RiskLimits | None = None,
                      run_mc: bool = True) -> dict[str, Any]:
    """Construye el informe de riesgo completo de una cartera."""
    limits = limits or RiskLimits()
    returns = load_returns_matrix(list(weights.keys()))
    metrics = compute_metrics(weights, returns)
    regime_budget = _load_regime_budget()
    gate = validate(weights, limits, regime_budget=regime_budget, metrics=metrics)

    report: dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "portfolio": weights,
        "metrics": metrics,
        "limits": asdict(limits),
        "regime_budget": regime_budget,
        "gate": gate,
    }
    if run_mc and not metrics.get("error"):
        from risk.monte_carlo import bootstrap_report
        report["monte_carlo"] = bootstrap_report(weights, returns)
    return report


def run(weights: dict[str, float]) -> Path:
    """Genera risk_report.json para una cartera."""
    report = build_risk_report(weights)
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    m = report["metrics"]
    print(f"[risk] gate={'PASS' if report['gate']['passed'] else 'REJECT'} "
          f"vol={m.get('ann_vol')} VaR95={m.get('var_95_1d')} maxDD={m.get('max_drawdown')} "
          f"beta={m.get('beta_spy')} -> {OUTPUT_PATH}")
    for v in report["gate"]["violations"]:
        print(f"  VIOLACION: {v}")
    return OUTPUT_PATH


if __name__ == "__main__":
    # Cartera demo core-satellite para probar el engine.
    demo = {"SPY": 0.35, "QQQ": 0.15, "TLT": 0.15, "GLD": 0.10, "NVDA": 0.10, "AAPL": 0.15}
    run(demo)
