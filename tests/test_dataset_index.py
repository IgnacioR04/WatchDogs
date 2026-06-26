"""Tests del backfill/indices historicos (pipelines/build_indexes.py) — Fase A."""

from __future__ import annotations

import gzip
import json

from normalize.schema import temporal_block
from pipelines.backfill import write_jsonl_gz
from pipelines.build_indexes import rebuild_indexes


def _make_record(ticker, actor, event, known):
    r = {"ticker": ticker, "insider_name": actor}
    r.update(temporal_block(event, known))
    return r


def test_write_jsonl_gz_y_lectura(tmp_path):
    """write_jsonl_gz escribe un jsonl.gz legible con todos los registros."""
    recs = [_make_record("NVDA", "X", "2024-04-01", "2024-04-03"),
            _make_record("AAPL", "Y", "2024-05-01", "2024-05-02")]
    path = tmp_path / "out.jsonl.gz"
    n = write_jsonl_gz(recs, path)
    assert n == 2
    with gzip.open(path, "rt", encoding="utf-8") as f:
        lines = [json.loads(l) for l in f if l.strip()]
    assert len(lines) == 2
    assert lines[0]["ticker"] == "NVDA"


def test_dataset_index_refleja_cobertura(tmp_path):
    """dataset_index muestra from/to, nº registros y delay medio reales."""
    hist = tmp_path / "HIST"
    # Particion 2024 Q2 de insiders
    p1 = hist / "normalized" / "sec_insiders" / "year=2024" / "quarter=Q2" / "sec_insiders.jsonl.gz"
    write_jsonl_gz([
        _make_record("NVDA", "Huang", "2024-04-10", "2024-04-12"),
        _make_record("AAPL", "Cook", "2024-06-20", "2024-06-22"),
    ], p1)
    # Particion 2024 Q3
    p2 = hist / "normalized" / "sec_insiders" / "year=2024" / "quarter=Q3" / "sec_insiders.jsonl.gz"
    write_jsonl_gz([_make_record("NVDA", "Huang", "2024-07-01", "2024-07-05")], p2)

    di = rebuild_indexes(hist)
    ds = {d["dataset"]: d for d in di["datasets"]}
    assert "sec_insiders" in ds
    si = ds["sec_insiders"]
    assert si["records"] == 3
    assert si["from_date"] == "2024-04-12"   # min known_date
    assert si["to_date"] == "2024-07-05"     # max known_date
    assert si["delay_days_avg"] == round((2 + 2 + 4) / 3, 1)
    assert si["files"] == 2

    # ticker_index y actor_index generados
    ti = json.loads((hist / "indexes" / "ticker_index.json").read_text(encoding="utf-8"))
    assert "NVDA" in ti and len(ti["NVDA"]) == 2  # aparece en 2 particiones
    ai = json.loads((hist / "indexes" / "actor_index.json").read_text(encoding="utf-8"))
    assert "Huang" in ai


def test_no_lookahead_en_historico(tmp_path):
    """Ningun registro archivado tiene known_date < event_date (anti-lookahead)."""
    hist = tmp_path / "HIST"
    p = hist / "normalized" / "sec_insiders" / "year=2024" / "quarter=Q1" / "sec_insiders.jsonl.gz"
    write_jsonl_gz([
        _make_record("NVDA", "X", "2024-01-10", "2024-01-12"),
        _make_record("AAPL", "Y", "2024-02-01", "2024-02-01"),
    ], p)
    with gzip.open(p, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rec = json.loads(line)
                assert rec["known_date"] >= rec["event_date"]
