"""Tests de la publicacion publica de 30 dias (pipelines/publish_public_30d.py)."""

from __future__ import annotations

import json

import pipelines.publish_public_30d as pub
from scrapers._dates import days_ago_iso, today_iso


def _write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


def test_recorta_eventos_a_30_dias(tmp_path, monkeypatch):
    """Un dataset de eventos pierde los registros mas viejos de 30 dias."""
    public = tmp_path / "public"
    monkeypatch.setattr(pub, "PUBLIC_DIR", public)

    _write(public / "sec_insiders_30d.json", [
        {"insider_name": "FRESH", "tx_date": today_iso()},
        {"insider_name": "FRESH2", "tx_date": days_ago_iso(10)},
        {"insider_name": "OLD", "tx_date": days_ago_iso(120)},      # fuera de 30d
        {"insider_name": "OLD2", "tx_date": "2020-01-01"},          # fuera de 30d
    ])
    manifest = pub.publish()

    # El fichero recortado solo tiene los 2 frescos.
    remaining = json.loads((public / "sec_insiders_30d.json").read_text(encoding="utf-8"))
    assert len(remaining) == 2
    assert {r["insider_name"] for r in remaining} == {"FRESH", "FRESH2"}

    # El manifest refleja el conteo.
    ds = {d["name"]: d for d in manifest["datasets"]}
    assert ds["sec_insiders_30d"]["records"] == 2
    assert ds["sec_insiders_30d"]["type"] == "events"


def test_snapshot_no_se_recorta(tmp_path, monkeypatch):
    """Un dataset snapshot (polymarket) se publica completo sin filtrar fechas."""
    public = tmp_path / "public"
    monkeypatch.setattr(pub, "PUBLIC_DIR", public)

    traders = [{"wallet": f"0x{i}", "pnl": i} for i in range(25)]
    _write(public / "polymarket_smart_traders.json", traders)
    manifest = pub.publish()

    remaining = json.loads((public / "polymarket_smart_traders.json").read_text(encoding="utf-8"))
    assert len(remaining) == 25  # intacto
    ds = {d["name"]: d for d in manifest["datasets"]}
    assert ds["polymarket_smart_traders"]["records"] == 25
    assert ds["polymarket_smart_traders"]["type"] == "snapshot"


def test_genera_manifest_y_latest(tmp_path, monkeypatch):
    """publish genera manifest_public.json y latest.json con estructura correcta."""
    public = tmp_path / "public"
    monkeypatch.setattr(pub, "PUBLIC_DIR", public)
    _write(public / "sec_insiders_30d.json", [{"insider_name": "X", "tx_date": today_iso()}])
    _write(public / "health_report.json", {"overall_status": "warning"})

    pub.publish()
    manifest = json.loads((public / "manifest_public.json").read_text(encoding="utf-8"))
    latest = json.loads((public / "latest.json").read_text(encoding="utf-8"))

    assert manifest["project"] == "WATCHDOG"
    assert manifest["public_window_days"] == 30
    assert "window" in manifest
    assert latest["overall_status"] == "warning"
    assert latest["datasets"]["sec_insiders_30d"] == 1
