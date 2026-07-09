"""Motor de metricas del paper trading (Fase I).

Valora la cartera del bot dia a dia a partir del ledger de carteras aprobadas
(paper_ledger.json) y el historico de precios (parquet en WATCHDOG_HISTORY):

  1. Para cada dia de mercado desde la primera aprobacion, aplica los pesos de
     la ultima cartera aprobada antes de ese dia (rebalanceo al cierre del dia
     de aprobacion; el cash rinde 0).
  2. Construye la equity curve (base 100 EUR) y un benchmark SPY rebasado.
  3. Calcula las metricas: retorno total, vol anualizada, Sharpe, Sortino,
     max drawdown realizado, win rate diario, y el P&L por posicion desde su
     primera entrada en cartera.

Salida: data/public/paper_trading.json (lo pinta la pestaña Paper del dashboard).

Nota: con pocos dias de historia las metricas anualizadas (Sharpe, vol) son
poco significativas; el JSON incluye n_days para que el dashboard lo avise.
"""

from __future__ import annotations

import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
HISTORY_DIR = Path(os.environ.get("WATCHDOG_HISTORY_DIR", r"G:/Mi unidad/WATCHDOG_HISTORY"))
PRICES_DIR = HISTORY_DIR / "normalized" / "prices"
LEDGER_PATH = PUBLIC_DIR / "paper_ledger.json"
OUTPUT_PATH = PUBLIC_DIR / "paper_trading.json"

BUDGET_EUR = 100.0
TRADING_DAYS = 252


def _safe_symbol(symbol: str) -> str:
    """Nombre de fichero de un simbolo (igual que market_prices)."""
    return symbol.replace("^", "IDX_").replace("-", "_").replace("/", "_")


def load_closes(symbol: str) -> pd.Series:
    """Serie de cierres diarios de un simbolo desde los parquet del history."""
    base = PRICES_DIR / f"symbol={_safe_symbol(symbol)}" / "timeframe=1d"
    if not base.exists():
        return pd.Series(dtype=float)
    frames = []
    for f in sorted(base.rglob("*.parquet"))[-3:]:
        try:
            df = pd.read_parquet(f)
            if "Close" in df.columns:
                frames.append(df["Close"])
        except Exception:
            continue
    if not frames:
        return pd.Series(dtype=float)
    s = pd.concat(frames)
    s.index = pd.to_datetime(s.index).tz_localize(None)
    return s[~s.index.duplicated(keep="last")].sort_index().dropna()


def _weights_for_day(ledger: list[dict], day: pd.Timestamp) -> dict[str, float] | None:
    """Pesos vigentes en un dia: la ultima cartera aprobada ANTES del fin de ese dia."""
    current = None
    for entry in ledger:
        approved = pd.Timestamp(entry["approved_at"]).tz_localize(None)
        if approved.normalize() <= day.normalize():
            current = entry["weights"]
        else:
            break
    return current


def build_equity_curve(ledger: list[dict]) -> tuple[pd.DataFrame, dict[str, dict]]:
    """Equity curve diaria (base 100) + P&L por posicion desde su entrada.

    Devuelve (df con columnas equity/spy/daily_ret indexado por fecha,
    {ticker: {entry_date, ret_since_entry, weight}}).
    """
    if not ledger:
        return pd.DataFrame(), {}

    all_tickers = sorted({t for e in ledger for t in e["weights"]})
    closes = {t: load_closes(t) for t in all_tickers}
    closes = {t: s for t, s in closes.items() if len(s)}
    spy = load_closes("SPY")

    start = pd.Timestamp(ledger[0]["approved_at"]).tz_localize(None).normalize()
    # Dias de mercado: los del SPY desde la primera aprobacion (excluido el
    # propio dia de aprobacion: se compra a ese cierre, el retorno empieza al
    # dia siguiente).
    days = [d for d in spy.index if d > start]

    entry_dates: dict[str, pd.Timestamp] = {}
    entry_prices: dict[str, float] = {}
    equity = BUDGET_EUR
    rows = []
    for day in days:
        w = _weights_for_day(ledger, day) or {}
        # registrar entradas nuevas (primer dia en cartera)
        for t in w:
            if t not in entry_dates and t in closes:
                prev = closes[t][closes[t].index < day]
                if len(prev):
                    entry_dates[t] = day
                    entry_prices[t] = float(prev.iloc[-1])
        # retorno del dia = suma ponderada de los retornos de cada posicion
        day_ret = 0.0
        for t, weight in w.items():
            s = closes.get(t)
            if s is None or day not in s.index:
                continue
            prev = s[s.index < day]
            if not len(prev):
                continue
            day_ret += weight * (float(s[day]) / float(prev.iloc[-1]) - 1)
        equity *= 1 + day_ret
        rows.append({"date": day, "daily_ret": day_ret, "equity": equity})

    df = pd.DataFrame(rows).set_index("date") if rows else pd.DataFrame()
    if len(df) and len(spy):
        spy_win = spy[spy.index.isin(df.index)]
        # Base = cierre del SPY en el dia de aprobacion (o el previo), igual que
        # la cartera: asi el benchmark captura tambien el primer dia de mercado.
        spy_base = spy[spy.index <= start]
        base_val = float(spy_base.iloc[-1]) if len(spy_base) else (float(spy_win.iloc[0]) if len(spy_win) else None)
        if len(spy_win) and base_val:
            df["spy"] = (spy_win / base_val) * BUDGET_EUR

    positions: dict[str, dict] = {}
    current_w = ledger[-1]["weights"]
    for t, weight in current_w.items():
        s = closes.get(t)
        info: dict[str, Any] = {"weight": weight}
        if t in entry_dates and s is not None and len(s):
            info["entry_date"] = entry_dates[t].date().isoformat()
            info["ret_since_entry"] = round(float(s.iloc[-1]) / entry_prices[t] - 1, 4)
            info["value_eur"] = round(BUDGET_EUR * weight * (1 + info["ret_since_entry"]), 2)
        positions[t] = info
    return df, positions


def compute_metrics(df: pd.DataFrame) -> dict[str, Any]:
    """Metricas de la equity curve. Con pocos dias, las anualizadas son orientativas."""
    if df.empty:
        return {"n_days": 0}
    rets = df["daily_ret"]
    n = len(rets)
    equity = float(df["equity"].iloc[-1])
    total_ret = equity / BUDGET_EUR - 1
    out: dict[str, Any] = {
        "n_days": n,
        "equity_eur": round(equity, 2),
        "total_return": round(total_ret, 4),
        "win_rate_days": round(float((rets > 0).mean()), 4) if n else None,
        "best_day": round(float(rets.max()), 4),
        "worst_day": round(float(rets.min()), 4),
    }
    if n >= 2 and float(rets.std()) > 0:
        std = float(rets.std())
        out["ann_vol"] = round(std * math.sqrt(TRADING_DAYS), 4)
        out["sharpe"] = round(float(rets.mean()) / std * math.sqrt(TRADING_DAYS), 2)
        downside = rets[rets < 0]
        if len(downside) and float(downside.std()) > 0:
            out["sortino"] = round(float(rets.mean()) / float(downside.std()) * math.sqrt(TRADING_DAYS), 2)
    peak = df["equity"].cummax()
    out["max_drawdown"] = round(float((df["equity"] / peak - 1).min()), 4)
    if "spy" in df.columns and len(df["spy"].dropna()):
        spy_ret = float(df["spy"].dropna().iloc[-1]) / BUDGET_EUR - 1
        out["spy_return"] = round(spy_ret, 4)
        out["excess_return"] = round(total_ret - spy_ret, 4)
    return out


def build() -> dict[str, Any]:
    """Construye el objeto paper_trading completo."""
    try:
        ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        ledger = []

    df, positions = build_equity_curve(ledger)
    metrics = compute_metrics(df)

    curve = [
        {"date": d.date().isoformat(), "equity": round(float(r["equity"]), 2),
         "spy": round(float(r["spy"]), 2) if "spy" in df.columns and pd.notna(r.get("spy")) else None,
         "daily_ret": round(float(r["daily_ret"]), 5)}
        for d, r in df.iterrows()
    ]
    cycles = [
        {"cycle": i + 1, "approved_at": e["approved_at"],
         "n_positions": len(e["weights"]),
         "invested": round(sum(e["weights"].values()), 4),
         "verdict_llm": e.get("verdict_llm"), "thesis": e.get("thesis"),
         "confidence": e.get("confidence"), "n_adjustments": e.get("n_adjustments")}
        for i, e in enumerate(ledger)
    ]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "budget_eur": BUDGET_EUR,
        "n_cycles": len(ledger),
        "metrics": metrics,
        "equity_curve": curve,
        "positions": positions,
        "cycles": cycles,
    }


def run() -> Path:
    """Genera paper_trading.json."""
    data = build()
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    m = data["metrics"]
    print(f"[paper_metrics] {data['n_cycles']} ciclos, {m.get('n_days', 0)} dias de mercado -> {OUTPUT_PATH}")
    if m.get("n_days"):
        print(f"  equity {m.get('equity_eur')} EUR ({m.get('total_return', 0):+.2%}) · "
              f"sharpe {m.get('sharpe', 'n/d')} · maxDD {m.get('max_drawdown', 0):.2%} · "
              f"win rate {m.get('win_rate_days', 0):.0%}")
    return OUTPUT_PATH


if __name__ == "__main__":
    run()
