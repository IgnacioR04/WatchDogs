"""Precios de mercado via yfinance (Fase B v3).

Descarga OHLCV diario de:
- Los tickers que aparecen en las señales (signals_30d.json).
- Un universo CORE de indices/ETFs/bonos/VIX/oro/cripto, necesario para el
  motor de regimen (Fase E) y el backtesting (Fase J).

Archiva el historico en WATCHDOG_HISTORY particionado por simbolo/año en parquet
(eficiente para series temporales). Tambien publica un snapshot reciente en
data/public para el dashboard.

yfinance no necesita API key. Para precios, `date` es la fecha de trading (no
aplica known_date: el precio de cierre es publico ese mismo dia).
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any

import pandas as pd
import yfinance as yf

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
HISTORY_DIR = Path(os.environ.get("WATCHDOG_HISTORY_DIR", r"G:/Mi unidad/WATCHDOG_HISTORY"))
PRICES_DIR = HISTORY_DIR / "normalized" / "prices"
OUTPUT_SNAPSHOT = PUBLIC_DIR / "market_prices_latest.json"

# Universo CORE para regimen y benchmarks (siempre se descargan).
CORE_UNIVERSE = [
    # Indices / mercado amplio
    "SPY", "QQQ", "IWM", "DIA", "VTI",
    # Sectores (SPDR)
    "XLK", "XLF", "XLE", "XLV", "XLY", "XLP", "XLI", "XLU", "XLB", "XLRE", "XLC",
    # Bonos / credito / tipos
    "TLT", "IEF", "SHY", "HYG", "LQD", "AGG",
    # Volatilidad / refugio / commodities / dolar / cripto
    "^VIX", "GLD", "SLV", "USO", "UUP", "BTC-USD", "ETH-USD",
]


def tickers_from_signals(limit: int = 80) -> list[str]:
    """Lee los tickers mas relevantes de signals_30d.json (por importancia)."""
    p = PUBLIC_DIR / "signals_30d.json"
    if not p.exists():
        return []
    try:
        signals = json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    score: dict[str, float] = {}
    for s in signals:
        tk = (s.get("ticker") or "").strip().upper()
        if tk and tk.isalpha() and 1 <= len(tk) <= 5:
            score[tk] = score.get(tk, 0) + (s.get("importance_score") or 0)
    return [t for t, _ in sorted(score.items(), key=lambda kv: kv[1], reverse=True)[:limit]]


def _safe_symbol(symbol: str) -> str:
    """Nombre de fichero seguro para un simbolo (quita ^, reemplaza - y /)."""
    return symbol.replace("^", "IDX_").replace("-", "_").replace("/", "_")


def archive_symbol(symbol: str, df: pd.DataFrame) -> int:
    """Archiva el OHLCV de un simbolo particionado por año en parquet.

    Devuelve el numero de filas archivadas. Idempotente: reescribe el parquet
    del año con los datos disponibles.
    """
    if df is None or df.empty:
        return 0
    df = df.copy()
    df.index = pd.to_datetime(df.index)
    total = 0
    safe = _safe_symbol(symbol)
    for year, group in df.groupby(df.index.year):
        out = PRICES_DIR / f"symbol={safe}" / f"timeframe=1d" / f"year={year}" / f"{safe}_{year}.parquet"
        out.parent.mkdir(parents=True, exist_ok=True)
        group.to_parquet(out)
        total += len(group)
    return total


def fetch_and_archive(symbols: list[str], period: str = "5y") -> dict[str, int]:
    """Descarga OHLCV de cada simbolo y lo archiva. Devuelve {symbol: filas}."""
    archived: dict[str, int] = {}
    for i, sym in enumerate(symbols):
        try:
            df = yf.download(sym, period=period, interval="1d", auto_adjust=True,
                             progress=False, threads=False)
            # yfinance puede devolver columnas MultiIndex; aplanar.
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            n = archive_symbol(sym, df)
            archived[sym] = n
        except Exception as e:
            print(f"  [prices] {sym}: fallo ({e})")
            archived[sym] = 0
        if (i + 1) % 10 == 0:
            print(f"  [prices] {i + 1}/{len(symbols)} simbolos")
        time.sleep(0.2)  # cortesia con yfinance
    return archived


def build_snapshot(symbols: list[str]) -> list[dict[str, Any]]:
    """Construye un snapshot reciente (ultimo precio + retornos) para el dashboard."""
    snap: list[dict[str, Any]] = []
    for sym in symbols:
        safe = _safe_symbol(sym)
        # Los dos parquets mas recientes (el del año actual puede tener pocas
        # filas en enero y romper ret_5d/ret_20d).
        files = sorted((PRICES_DIR / f"symbol={safe}" / "timeframe=1d").rglob("*.parquet"))
        if not files:
            continue
        frames = []
        for f in files[-2:]:
            try:
                df = pd.read_parquet(f)
                if not df.empty and "Close" in df.columns:
                    frames.append(df["Close"])
            except Exception:
                continue
        if not frames:
            continue
        close = pd.concat(frames).dropna()
        close.index = pd.to_datetime(close.index)
        close = close.sort_index()
        if len(close) < 2:
            continue
        last = float(close.iloc[-1])
        def ret(n):
            return round((last / float(close.iloc[-n - 1]) - 1) * 100, 2) if len(close) > n else None
        snap.append({
            "symbol": sym,
            "close": round(last, 2),
            "date": str(close.index[-1].date()),
            "ret_1d": ret(1),
            "ret_5d": ret(5),
            "ret_20d": ret(20),
        })
    return snap


def run(period: str = "5y", include_signals: bool = True) -> Path:
    """Descarga + archiva el universo CORE (+ tickers de señales) y publica snapshot."""
    symbols = list(dict.fromkeys(CORE_UNIVERSE + (tickers_from_signals() if include_signals else [])))
    print(f"[market_prices] {len(symbols)} simbolos, periodo {period} -> {PRICES_DIR}")
    archived = fetch_and_archive(symbols, period=period)
    ok = sum(1 for v in archived.values() if v > 0)
    snap = build_snapshot(symbols)
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_SNAPSHOT.write_text(json.dumps(snap, indent=2, ensure_ascii=False), encoding="utf-8")
    total = sum(archived.values())
    print(f"[market_prices] {ok}/{len(symbols)} simbolos OK, {total:,} filas archivadas, "
          f"snapshot {len(snap)} -> {OUTPUT_SNAPSHOT}")
    return OUTPUT_SNAPSHOT


if __name__ == "__main__":
    run()
