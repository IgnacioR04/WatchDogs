"""Genera la capa publica de 30 dias en data/public/.

Lee los datasets normalizados que producen los scrapers en data/public/ y:
- En datasets de tipo "eventos" (insiders, congress, 13d/13g, news) recorta a
  los ultimos 30 dias por fecha.
- En datasets de tipo "snapshot" (13F holdings, polymarket) los deja completos.
- Genera manifest_public.json (metadata de cada dataset) y latest.json
  (resumen del ultimo run + salud).

Esta es la API publica que sirve GitHub Pages. NO incluye historico profundo
(eso ira a Drive via OAuth mas adelante).

Uso:
    python -m pipelines.publish_public_30d
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from scrapers._dates import now_utc, parse_date, rolling_window, within_last_days

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
WINDOW_DAYS = 30

# Configuracion por dataset: como tratarlo al publicar.
#   type "events"   -> recortar a 30 dias usando la primera date_key valida.
#   type "snapshot" -> dejar completo (es una foto del estado actual).
DATASETS: dict[str, dict[str, Any]] = {
    "congress_trades_30d.json": {"type": "events", "date_keys": ["disclosure_date", "tx_date"]},
    "sec_insiders_30d.json": {"type": "events", "date_keys": ["tx_date", "filing_date"]},
    "sec_13d_13g_30d.json": {"type": "events", "date_keys": ["filing_date", "event_date"]},
    "news_context_30d.json": {"type": "events", "date_keys": ["published_at"]},
    "institutional_holdings_latest.json": {"type": "snapshot"},
    "institutional_changes_latest.json": {"type": "snapshot"},
    "polymarket_smart_traders.json": {"type": "snapshot"},
    "polymarket_whales.json": {"type": "snapshot"},
    "signals_30d.json": {"type": "events", "date_keys": ["event_date", "disclosure_date"]},
    "top_movements_30d.json": {"type": "snapshot"},
}


def _load(path: Path) -> Any:
    """Carga JSON o None si no existe/falla."""
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _filter_events(records: list[dict], date_keys: list[str], days: int) -> list[dict]:
    """Conserva registros cuya fecha (primera date_key valida) este en los ultimos N dias."""
    out = []
    for r in records:
        for k in date_keys:
            if r.get(k):
                if within_last_days(r.get(k), days):
                    out.append(r)
                break
    return out


def _date_range(records: list[dict], date_keys: list[str]) -> tuple[str | None, str | None]:
    """Devuelve (from, to) ISO de las fechas presentes en los registros."""
    dates = []
    for r in records:
        for k in date_keys:
            d = parse_date(r.get(k))
            if d:
                dates.append(d)
                break
    if not dates:
        return None, None
    return min(dates).date().isoformat(), max(dates).date().isoformat()


def publish() -> dict[str, Any]:
    """Aplica la ventana de 30d donde toca y construye el manifest publico."""
    manifest_datasets = []
    from_win, to_win = rolling_window(WINDOW_DAYS)

    for filename, cfg in DATASETS.items():
        path = PUBLIC_DIR / filename
        data = _load(path)
        if data is None:
            continue  # dataset aun no generado (ej 13d/13g, news en fases futuras)

        if cfg["type"] == "events" and isinstance(data, list):
            date_keys = cfg["date_keys"]
            filtered = _filter_events(data, date_keys, WINDOW_DAYS)
            # Reescribe el fichero ya recortado a 30 dias.
            path.write_text(json.dumps(filtered, indent=2, ensure_ascii=False, default=str),
                            encoding="utf-8")
            d_from, d_to = _date_range(filtered, date_keys)
            records = len(filtered)
        else:
            records = len(data) if isinstance(data, list) else 1
            d_from, d_to = None, None

        manifest_datasets.append({
            "name": filename.replace(".json", ""),
            "path": f"data/public/{filename}",
            "type": cfg["type"],
            "records": records,
            "from_date": d_from,
            "to_date": d_to,
            "updated_at": now_utc().isoformat(),
        })

    manifest = {
        "project": "WATCHDOG",
        "generated_at": now_utc().isoformat(),
        "public_window_days": WINDOW_DAYS,
        "window": {"from": from_win, "to": to_win},
        "datasets": manifest_datasets,
    }
    (PUBLIC_DIR / "manifest_public.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    # latest.json: resumen compacto del ultimo run + salud (si existe).
    health = _load(PUBLIC_DIR / "health_report.json") or {}
    latest = {
        "generated_at": now_utc().isoformat(),
        "overall_status": health.get("overall_status", "unknown"),
        "datasets": {d["name"]: d["records"] for d in manifest_datasets},
    }
    (PUBLIC_DIR / "latest.json").write_text(
        json.dumps(latest, indent=2, ensure_ascii=False), encoding="utf-8")

    return manifest


def run() -> Path:
    """Ejecuta la publicacion y devuelve la ruta del manifest."""
    manifest = publish()
    out = PUBLIC_DIR / "manifest_public.json"
    print(f"[publish_public_30d] {len(manifest['datasets'])} datasets publicados:")
    for d in manifest["datasets"]:
        rng = f" [{d['from_date']}..{d['to_date']}]" if d["from_date"] else ""
        print(f"  {d['name']}: {d['records']} records ({d['type']}){rng}")
    return out


if __name__ == "__main__":
    run()
