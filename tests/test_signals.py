"""Tests de la capa unificada de senales (pipelines/build_signals.py)."""

from __future__ import annotations

import json

import pipelines.build_signals as bs


def _seed(public, **datasets):
    public.mkdir(parents=True, exist_ok=True)
    for name, data in datasets.items():
        (public / name).write_text(json.dumps(data), encoding="utf-8")


def test_unifica_y_puntua(tmp_path, monkeypatch):
    """Fusiona fuentes al schema unificado con importance_score 0-100."""
    public = tmp_path / "public"
    monkeypatch.setattr(bs, "PUBLIC_DIR", public)
    _seed(public,
          **{"sec_insiders_30d.json": [
              {"id": "i1", "insider_name": "Jane CEO", "insider_title": "President and CEO",
               "company": "NVIDIA CORP", "ticker": "NVDA", "tx_code": "P",
               "value_usd": 2_000_000, "tx_date": "2026-06-20", "source_url": "u"}],
             "congress_trades_30d.json": [
              {"id": "c1", "source": "house_pdf_parsed", "politician": "Nancy Pelosi",
               "actor_type": "house_rep", "ticker": "NVDA", "asset_name": "NVIDIA",
               "tx_type": "purchase", "direction": "buy", "amount_estimated": 3_000_000,
               "tx_date": "2026-06-18", "disclosure_date": "2026-06-22", "source_url": "u"}],
             "sec_13d_13g_30d.json": [],
             "institutional_changes_latest.json": []})
    signals = bs.build()
    assert len(signals) == 2
    for s in signals:
        assert "importance_score" in s and 0 <= s["importance_score"] <= 100
        assert s["ticker"] == "NVDA"


def test_cross_source_sube_score(tmp_path, monkeypatch):
    """Un ticker en 2 fuentes recibe cross_source_score > 0."""
    public = tmp_path / "public"
    monkeypatch.setattr(bs, "PUBLIC_DIR", public)
    _seed(public,
          **{"sec_insiders_30d.json": [
              {"id": "i1", "insider_name": "X", "insider_title": "CEO", "company": "Dell",
               "ticker": "DELL", "tx_code": "P", "value_usd": 100000, "tx_date": "2026-06-20"}],
             "congress_trades_30d.json": [
              {"id": "c1", "source": "house_pdf_parsed", "politician": "Rep Y",
               "actor_type": "house_rep", "ticker": "DELL", "tx_type": "purchase",
               "direction": "buy", "amount_estimated": 50000, "tx_date": "2026-06-19"}],
             "sec_13d_13g_30d.json": [], "institutional_changes_latest.json": []})
    signals = bs.build()
    # Ambas senales DELL deben tener cross_source_score > 0
    for s in signals:
        assert s["cross_source_score"] > 0


def test_insider_actor_type():
    """Infiere el actor_type del cargo del insider."""
    assert bs._insider_actor_type("President and CEO") == "ceo"
    assert bs._insider_actor_type("Chief Financial Officer") == "cfo"
    assert bs._insider_actor_type("Director") == "director"
    assert bs._insider_actor_type("10% Owner") == "ten_percent_owner"
    assert bs._insider_actor_type("") == "insider"


def test_insider_direccion_por_codigo(tmp_path, monkeypatch):
    """P/M -> buy, S/D -> sell."""
    public = tmp_path / "public"
    monkeypatch.setattr(bs, "PUBLIC_DIR", public)
    _seed(public, **{"sec_insiders_30d.json": [
        {"id": "p", "insider_name": "A", "insider_title": "CEO", "ticker": "AAA",
         "tx_code": "P", "value_usd": 1, "tx_date": "2026-06-20"},
        {"id": "s", "insider_name": "B", "insider_title": "CEO", "ticker": "BBB",
         "tx_code": "S", "value_usd": 1, "tx_date": "2026-06-20"}],
        "congress_trades_30d.json": [], "sec_13d_13g_30d.json": [],
        "institutional_changes_latest.json": []})
    sig = {s["ticker"]: s for s in bs.build()}
    assert sig["AAA"]["direction"] == "buy"
    assert sig["BBB"]["direction"] == "sell"
