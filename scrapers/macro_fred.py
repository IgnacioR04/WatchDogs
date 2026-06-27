"""Series macro de FRED (Federal Reserve, St. Louis) — Fase B v3.

Descarga las series macroeconomicas clave que alimentan el motor de regimen
(Fase E) y el backtesting: tipos, curva, inflacion, paro, dolar, credito.

API REST (sin dependencia extra): necesita una API key gratuita en la env var
FRED_API_KEY (https://fredaccount.stlouisfed.org/apikeys).

Archiva el historico en WATCHDOG_HISTORY (jsonl.gz por serie) y publica un
snapshot reciente en data/public para el dashboard / regimen.

Nota temporal: la fecha de observacion de FRED es el periodo de referencia. La
publicacion real tiene retraso (ej. CPI del mes M sale a mediados de M+1). Para
no introducir lookahead en backtesting marcamos known_date_estimated y aplicamos
un retraso tipico por serie.
"""

from __future__ import annotations

import gzip
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
HISTORY_DIR = Path(os.environ.get("WATCHDOG_HISTORY_DIR", r"G:/Mi unidad/WATCHDOG_HISTORY"))
MACRO_DIR = HISTORY_DIR / "normalized" / "macro"
OUTPUT_SNAPSHOT = PUBLIC_DIR / "macro_latest.json"

FRED_URL = "https://api.stlouisfed.org/fred/series/observations"

# Series FRED con su descripcion y retraso tipico de publicacion (dias).
# El retraso aproxima la known_date para evitar lookahead en backtesting.
SERIES = {
    "DGS2":        {"name": "Treasury 2Y yield", "group": "rates", "lag": 1},
    "DGS10":       {"name": "Treasury 10Y yield", "group": "rates", "lag": 1},
    "T10Y2Y":      {"name": "Curva 10Y-2Y", "group": "rates", "lag": 1},
    "FEDFUNDS":    {"name": "Fed Funds Rate", "group": "rates", "lag": 1},
    "T10YIE":      {"name": "Breakeven inflacion 10Y", "group": "inflation", "lag": 1},
    "CPIAUCSL":    {"name": "CPI", "group": "inflation", "lag": 14},
    "PCEPI":       {"name": "PCE price index", "group": "inflation", "lag": 30},
    "UNRATE":      {"name": "Tasa de paro", "group": "labor", "lag": 7},
    "ICSA":        {"name": "Initial jobless claims", "group": "labor", "lag": 5},
    "INDPRO":      {"name": "Produccion industrial", "group": "activity", "lag": 16},
    "UMCSENT":     {"name": "Confianza consumidor (Michigan)", "group": "activity", "lag": 1},
    "BAMLH0A0HYM2": {"name": "High yield spread (OAS)", "group": "credit", "lag": 1},
    "DTWEXBGS":    {"name": "Dolar broad index", "group": "fx", "lag": 1},
    "M2SL":        {"name": "M2 money supply", "group": "money", "lag": 30},
}


def _api_key() -> str:
    """Devuelve la API key de FRED o lanza si no esta configurada."""
    key = os.environ.get("FRED_API_KEY", "").strip()
    if not key:
        raise RuntimeError("Falta FRED_API_KEY (https://fredaccount.stlouisfed.org/apikeys)")
    return key


def fetch_series(series_id: str, start: str = "2010-01-01",
                 session: requests.Session | None = None) -> list[dict[str, Any]]:
    """Descarga las observaciones de una serie FRED desde `start`.

    Devuelve registros con bloque temporal (event=fecha obs, known=event+lag).
    """
    session = session or requests.Session()
    meta = SERIES.get(series_id, {})
    lag = meta.get("lag", 1)
    params = {
        "series_id": series_id, "api_key": _api_key(), "file_type": "json",
        "observation_start": start,
    }
    r = session.get(FRED_URL, params=params, timeout=30)
    r.raise_for_status()
    obs = r.json().get("observations", [])
    out: list[dict[str, Any]] = []
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for o in obs:
        val = o.get("value")
        if val in (".", "", None):  # FRED usa '.' para missing
            continue
        try:
            value = float(val)
        except ValueError:
            continue
        event_date = o.get("date", "")
        try:
            known = (datetime.strptime(event_date, "%Y-%m-%d") + timedelta(days=lag)).date().isoformat()
        except ValueError:
            known = event_date
        out.append({
            "series_id": series_id,
            "name": meta.get("name", series_id),
            "group": meta.get("group", "macro"),
            "value": value,
            "source": "fred",
            "event_date": event_date,
            "known_date": known,
            "scrape_date": now,
            "delay_days": lag,
            "known_date_estimated": True,
        })
    return out


def _write_jsonl_gz(records: list[dict], path: Path) -> int:
    """Escribe registros como jsonl.gz."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False))
            f.write("\n")
    return len(records)


def run(start: str = "2010-01-01") -> Path:
    """Descarga todas las series, archiva en Drive y publica snapshot reciente."""
    session = requests.Session()
    session.headers["User-Agent"] = "Watchdog/1.0"
    snapshot: list[dict[str, Any]] = []
    total = 0
    for sid in SERIES:
        try:
            recs = fetch_series(sid, start=start, session=session)
        except Exception as e:
            print(f"  [fred] {sid}: fallo ({e})")
            continue
        if not recs:
            continue
        path = MACRO_DIR / f"series={sid}" / f"{sid}.jsonl.gz"
        total += _write_jsonl_gz(recs, path)
        last = recs[-1]
        # Variacion vs hace ~21 obs (aprox 1 mes) para el snapshot.
        prev = recs[-22] if len(recs) > 22 else recs[0]
        snapshot.append({
            "series_id": sid, "name": last["name"], "group": last["group"],
            "value": last["value"], "date": last["event_date"],
            "change_1m": round(last["value"] - prev["value"], 3),
        })
        print(f"  [fred] {sid}: {len(recs):,} obs, ultimo {last['value']} ({last['event_date']})")
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_SNAPSHOT.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[macro_fred] {len(snapshot)} series, {total:,} observaciones -> {OUTPUT_SNAPSHOT}")
    return OUTPUT_SNAPSHOT


if __name__ == "__main__":
    run()
