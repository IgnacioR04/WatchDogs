"""Indices de consulta del historico de WATCHDOG (Fase A v3).

Escanea los ficheros particionados de WATCHDOG_HISTORY/normalized y construye:
- dataset_index.json: cobertura temporal real por dataset (from/to, nº registros,
  delay medio). ESENCIAL — responde "hasta donde llega mi historico".
- ticker_index.json: ticker -> [{dataset, year, quarter, file, records}].
- actor_index.json: actor -> [{dataset, year, quarter, file, records}].

No carga todo en memoria: itera linea a linea cada jsonl.gz.
"""

from __future__ import annotations

import gzip
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

# Campo que identifica al actor segun la fuente.
ACTOR_FIELDS = ("insider_name", "filer_name", "manager", "politician", "actor_name")


def _iter_jsonl_gz(path: Path) -> Iterator[dict]:
    """Itera registros de un jsonl.gz linea a linea."""
    try:
        with gzip.open(path, "rt", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        yield json.loads(line)
                    except json.JSONDecodeError:
                        continue
    except OSError:
        return


def _partition_of(path: Path) -> tuple[str, str, str]:
    """Extrae (source, year, quarter) de la ruta particionada."""
    parts = {p.split("=")[0]: p.split("=")[1] for p in path.parts if "=" in p}
    # source = carpeta bajo 'normalized'
    source = ""
    pp = path.parts
    if "normalized" in pp:
        i = pp.index("normalized")
        if i + 1 < len(pp):
            source = pp[i + 1]
    return source, parts.get("year", ""), parts.get("quarter", "")


def rebuild_indexes(history_dir: Path) -> dict[str, Any]:
    """Reconstruye dataset_index, ticker_index y actor_index. Devuelve dataset_index."""
    history_dir = Path(history_dir)
    normalized = history_dir / "normalized"
    indexes = history_dir / "indexes"
    indexes.mkdir(parents=True, exist_ok=True)

    # Acumuladores
    ds: dict[str, dict[str, Any]] = {}
    ticker_idx: dict[str, list[dict]] = defaultdict(list)
    actor_idx: dict[str, list[dict]] = defaultdict(list)

    files = sorted(normalized.rglob("*.jsonl.gz")) if normalized.exists() else []
    for path in files:
        source, year, quarter = _partition_of(path)
        if not source:
            continue
        n = 0
        dates: list[str] = []
        delays: list[int] = []
        file_tickers: set[str] = set()
        file_actors: set[str] = set()
        # Cutoff anti-typos: las fechas futuras (> hoy) son errores de tecleo en
        # algun filing de la SEC y no deben definir la cobertura del dataset.
        today = datetime.now(timezone.utc).date().isoformat()
        for rec in _iter_jsonl_gz(path):
            n += 1
            kd = rec.get("known_date") or rec.get("event_date")
            if kd and kd <= today:
                dates.append(kd)
            # delay_days razonable (excluye outliers por typos de fecha)
            dd = rec.get("delay_days")
            if isinstance(dd, int) and 0 <= dd <= 365:
                delays.append(dd)
            tk = (rec.get("ticker") or "").strip().upper()
            if tk:
                file_tickers.add(tk)
            for af in ACTOR_FIELDS:
                if rec.get(af):
                    file_actors.add(str(rec[af])); break

        # dataset_index
        d = ds.setdefault(source, {"dataset": source, "records": 0,
                                   "from_date": None, "to_date": None,
                                   "delay_days_avg": None, "_delays": [], "files": 0,
                                   "partitions": []})
        d["records"] += n
        d["files"] += 1
        d["partitions"].append(f"{year}/{quarter}" if quarter else year)
        d["_delays"].extend(delays)
        if dates:
            mn, mx = min(dates), max(dates)
            d["from_date"] = mn if not d["from_date"] else min(d["from_date"], mn)
            d["to_date"] = mx if not d["to_date"] else max(d["to_date"], mx)

        rel = str(path.relative_to(history_dir))
        for tk in file_tickers:
            ticker_idx[tk].append({"dataset": source, "year": year, "quarter": quarter, "file": rel, "records": n})
        # actor_index puede crecer mucho; guardamos solo presencia por fichero
        for ac in file_actors:
            actor_idx[ac].append({"dataset": source, "year": year, "quarter": quarter, "file": rel})

    # Finalizar dataset_index (media de delays, limpiar internos)
    for d in ds.values():
        delays = d.pop("_delays", [])
        d["delay_days_avg"] = round(sum(delays) / len(delays), 1) if delays else None
        d["partitions"] = sorted(set(d["partitions"]))

    dataset_index = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "history_dir": str(history_dir),
        "datasets": sorted(ds.values(), key=lambda x: x["dataset"]),
    }
    (indexes / "dataset_index.json").write_text(
        json.dumps(dataset_index, indent=2, ensure_ascii=False), encoding="utf-8")
    (indexes / "ticker_index.json").write_text(
        json.dumps(ticker_idx, ensure_ascii=False), encoding="utf-8")
    (indexes / "actor_index.json").write_text(
        json.dumps(actor_idx, ensure_ascii=False), encoding="utf-8")

    print(f"[indexes] {len(files)} ficheros, {len(ticker_idx)} tickers, {len(actor_idx)} actores")
    for d in dataset_index["datasets"]:
        print(f"  {d['dataset']}: {d['records']:,} registros [{d['from_date']}..{d['to_date']}] "
              f"delay medio {d['delay_days_avg']}d, {d['files']} ficheros")
    return dataset_index


if __name__ == "__main__":
    import os
    rebuild_indexes(Path(os.environ.get("WATCHDOG_HISTORY_DIR", r"G:/Mi unidad/WATCHDOG_HISTORY")))
