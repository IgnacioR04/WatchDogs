"""Motor de backfill historico de WATCHDOG (Fase A v3).

Reconstruye el historico de cada fuente y lo archiva particionado por fecha en
WATCHDOG_HISTORY (carpeta local que Drive Desktop sincroniza, o configurable).
Es robusto a interrupciones: guarda un checkpoint y reanuda desde donde quedo.

Fuentes:
- sec_insiders: datasets bulk trimestrales de la SEC (rapido, una descarga/quarter).
- sec_13d_13g: recorre el full-index de EDGAR y parsea cada primary_doc.xml.

Layout de archivo:
    WATCHDOG_HISTORY/normalized/{source}/year=YYYY/quarter=QX/{source}.jsonl.gz
    WATCHDOG_HISTORY/indexes/checkpoint.json
    WATCHDOG_HISTORY/indexes/dataset_index.json

Uso:
    python -m pipelines.backfill --source sec_insiders --from 2024 --to 2026
"""

from __future__ import annotations

import argparse
import gzip
import json
import os
import time
from pathlib import Path
from typing import Any, Iterable

from scrapers._edgar_index import FORMS_BY_SOURCE, fetch_quarter_index, iter_quarters
from scrapers._http import Client, UA_SEC
from scrapers._sec_bulk import fetch_insider_quarter

# Carpeta raiz del historico. Por defecto en Drive (sincronizada por Drive
# Desktop). Configurable con WATCHDOG_HISTORY_DIR.
HISTORY_DIR = Path(os.environ.get("WATCHDOG_HISTORY_DIR", r"G:/Mi unidad/WATCHDOG_HISTORY"))
NORMALIZED = HISTORY_DIR / "normalized"
INDEXES = HISTORY_DIR / "indexes"
CHECKPOINT = INDEXES / "checkpoint.json"


def _load_checkpoint() -> dict[str, Any]:
    """Carga el checkpoint de progreso, o {} si no existe."""
    if CHECKPOINT.exists():
        try:
            return json.loads(CHECKPOINT.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def _save_checkpoint(cp: dict[str, Any]) -> None:
    """Guarda el checkpoint de progreso."""
    INDEXES.mkdir(parents=True, exist_ok=True)
    CHECKPOINT.write_text(json.dumps(cp, indent=2, ensure_ascii=False), encoding="utf-8")


def write_jsonl_gz(records: Iterable[dict], path: Path) -> int:
    """Escribe registros como jsonl.gz (una linea JSON por registro). Devuelve nº."""
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False, default=str))
            f.write("\n")
            n += 1
    return n


def _quarter_partition(source: str, year: int, quarter: int) -> Path:
    """Ruta de archivo particionado de un (source, year, quarter)."""
    return NORMALIZED / source / f"year={year}" / f"quarter=Q{quarter}" / f"{source}.jsonl.gz"


# --- Backfill por fuente ---------------------------------------------------

def backfill_insiders(from_year: int, to_year: int, client: Client,
                      checkpoint: dict) -> None:
    """Backfill de insiders via datasets bulk trimestrales (rapido)."""
    done = set(checkpoint.setdefault("sec_insiders", []))
    for year, q in iter_quarters(from_year, to_year):
        key = f"{year}Q{q}"
        if key in done:
            print(f"  [insiders] {key} ya hecho (checkpoint), salto")
            continue
        t0 = time.time()
        recs = fetch_insider_quarter(year, q, client=client)
        if not recs:
            print(f"  [insiders] {key}: sin datos (quarter no publicado aun?), salto")
            done.add(key); checkpoint["sec_insiders"] = sorted(done); _save_checkpoint(checkpoint)
            continue
        path = _quarter_partition("sec_insiders", year, q)
        n = write_jsonl_gz(recs, path)
        done.add(key)
        checkpoint["sec_insiders"] = sorted(done)
        _save_checkpoint(checkpoint)
        print(f"  [insiders] {key}: {n:,} tx -> {path.name} ({time.time()-t0:.1f}s)")


def backfill_13d_13g(from_year: int, to_year: int, client: Client,
                     checkpoint: dict, max_docs_per_q: int = 800) -> None:
    """Backfill de 13D/13G recorriendo el full-index + parseando primary_doc.xml.

    Mas lento (descarga cada XML). Cap por quarter para acotar. Reanudable.
    """
    from scrapers.sec_13d_13g import hit_to_record

    done = set(checkpoint.setdefault("sec_13d_13g", []))
    forms = FORMS_BY_SOURCE["sec_13d_13g"]
    for year, q in iter_quarters(from_year, to_year):
        key = f"{year}Q{q}"
        if key in done:
            print(f"  [13d13g] {key} ya hecho, salto")
            continue
        t0 = time.time()
        idx = fetch_quarter_index(year, q, forms=forms, client=client)
        # El index da el filing; reconstruimos el hit minimo para hit_to_record.
        records: list[dict] = []
        for entry in idx[:max_docs_per_q]:
            # primary_doc.xml dentro del directorio del filing
            acc = entry["accession"]
            cik = entry["cik"]
            hit = {
                "_id": f"{acc}:primary_doc.xml",
                "_source": {
                    "display_names": [f"{entry['company']} (CIK {cik})"],
                    "ciks": [cik],
                    "file_date": entry["date_filed"],
                    "file_type": entry["form_type"],
                },
            }
            rec = hit_to_record(client, hit)
            if rec:
                records.append(rec)
        if records:
            path = _quarter_partition("sec_13d_13g", year, q)
            write_jsonl_gz(records, path)
        done.add(key)
        checkpoint["sec_13d_13g"] = sorted(done)
        _save_checkpoint(checkpoint)
        print(f"  [13d13g] {key}: {len(records)} filings ({time.time()-t0:.0f}s)")


def backfill_congress(from_year: int, to_year: int, client: Client,
                      checkpoint: dict) -> None:
    """Backfill de Congress: Senate via mirror historico (2012-2020, con tickers).

    El mirror de timothycarambat es la unica fuente con tickers/montos para anos
    viejos del Senado (el eFD oficial bloquea bots). Se marca source=senate_mirror.
    House antiguo solo tiene metadata (sin ticker) y se omite del backfill aqui.
    """
    from normalize.schema import stable_id, temporal_block
    from scrapers.congress import URL_SENATE, _norm_tx_type
    from scrapers.congress_house_pdf_parser import ROW_RE  # noqa: F401 (no usado)

    if "congress" in checkpoint and "senate_mirror" in checkpoint["congress"]:
        print("  [congress] senate_mirror ya hecho, salto")
        return

    try:
        raw = client.get_json(URL_SENATE, timeout=120)
    except Exception as e:
        print(f"  [congress] fallo mirror senate ({e})")
        return

    by_year: dict[int, list[dict]] = {}
    for x in raw:
        tx_date = x.get("transaction_date") or ""
        disc = x.get("disclosure_date") or x.get("date_received") or tx_date
        # Normalizar fecha para particionar por ano del evento.
        from scrapers._dates import parse_date
        d = parse_date(tx_date)
        if not d:
            continue
        year = d.year
        if year < from_year or year > to_year:
            continue
        ticker = (x.get("ticker") or "").strip().upper()
        if ticker in {"", "--", "N/A", "NONE"}:
            ticker = ""
        politician = (x.get("senator") or "").strip()
        rec = {
            "id": stable_id("senate_mirror", politician, ticker, tx_date, x.get("amount", "")),
            "source": "senate_mirror",
            "source_type": "congress",
            "politician": politician,
            "actor_name": politician,
            "actor_type": "senator",
            "chamber": "senate",
            "ticker": ticker,
            "asset_name": (x.get("asset_description") or "").strip(),
            "tx_type": _norm_tx_type(x.get("type")),
            "amount_range": x.get("amount", ""),
            "tx_date": tx_date,
            "disclosure_date": disc,
            "source_url": x.get("ptr_link", ""),
        }
        # event=transaccion, known=disclosure. Datos viejos: known estimado si falta.
        estimated = not (x.get("disclosure_date") or x.get("date_received"))
        rec.update(temporal_block(tx_date, disc, estimated=estimated))
        by_year.setdefault(year, []).append(rec)

    total = 0
    for year, recs in sorted(by_year.items()):
        path = NORMALIZED / "congress" / f"year={year}" / "congress.jsonl.gz"
        n = write_jsonl_gz(recs, path)
        total += n
        print(f"  [congress] {year}: {n:,} trades senate -> {path.name}")
    checkpoint.setdefault("congress", []).append("senate_mirror")
    _save_checkpoint(checkpoint)
    print(f"  [congress] total {total:,} trades senate ({from_year}-{to_year})")


SOURCES = {
    "sec_insiders": backfill_insiders,
    "sec_13d_13g": backfill_13d_13g,
    "congress": backfill_congress,
}


def run(source: str, from_year: int, to_year: int) -> None:
    """Lanza el backfill de una fuente para el rango de anos dado."""
    print(f"[backfill] {source} {from_year}-{to_year} -> {HISTORY_DIR}")
    client = Client(user_agent=UA_SEC, max_per_sec=8)
    checkpoint = _load_checkpoint()
    fn = SOURCES.get(source)
    if not fn:
        raise SystemExit(f"fuente desconocida: {source} (opciones: {list(SOURCES)})")
    fn(from_year, to_year, client, checkpoint)
    # Reconstruir dataset_index tras el backfill.
    from pipelines.build_indexes import rebuild_indexes
    rebuild_indexes(HISTORY_DIR)
    print(f"[backfill] {source} completado.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, choices=list(SOURCES))
    ap.add_argument("--from", dest="from_year", type=int, required=True)
    ap.add_argument("--to", dest="to_year", type=int, required=True)
    args = ap.parse_args()
    run(args.source, args.from_year, args.to_year)
