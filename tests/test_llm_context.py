"""Tests del contexto LLM (pipelines/build_llm_context.py)."""

from __future__ import annotations

import json

import pipelines.build_llm_context as lc


def _seed(public, **datasets):
    public.mkdir(parents=True, exist_ok=True)
    for name, data in datasets.items():
        (public / name).write_text(json.dumps(data), encoding="utf-8")


def test_estructura_completa(tmp_path, monkeypatch):
    """El contexto tiene todas las secciones requeridas + instrucciones anti-alucinacion."""
    public = tmp_path / "public"
    monkeypatch.setattr(lc, "PUBLIC_DIR", public)
    _seed(public,
          **{"signals_30d.json": [
              {"ticker": "NVDA", "asset_name": "NVIDIA", "source_type": "corporate_insider",
               "direction": "buy", "actor_name": "CEO X", "actor_type": "ceo",
               "amount_estimated": 1e6, "importance_score": 80, "event_date": "2026-06-20"}],
             "news_context_30d.json": [
              {"title": "NVIDIA earnings beat", "url": "http://x", "tickers_detected": ["NVDA"],
               "themes": ["earnings", "ai"], "published_at": "2026-06-24T00:00:00Z"}],
             "top_movements_30d.json": {"movements": [{"rank": 1, "title": "CEO compro NVDA"}]},
             "health_report.json": {"overall_status": "ok", "datasets": {"congress": {"status": "ok"}}},
             "institutional_changes_latest.json": [],
             "sec_13d_13g_30d.json": [],
             "polymarket_smart_traders.json": [], "polymarket_whales.json": []})
    ctx = lc.build()
    # Secciones obligatorias
    for key in ["window", "data_quality", "market_context", "top_movements",
                "top_tickers", "insider_buying", "institutional_changes",
                "congress_activity", "large_holders", "polymarket", "news",
                "llm_instructions"]:
        assert key in ctx, f"falta seccion {key}"
    # Instrucciones anti-alucinacion
    instr = ctx["llm_instructions"]
    assert "must_not" in instr and "must_include" in instr
    assert any("asesoramiento" in x.lower() or "certeza" in x.lower() for x in instr["must_not"])
    # top_tickers separa buy/sell
    assert "buy_pressure" in ctx["top_tickers"]
    assert "sell_pressure" in ctx["top_tickers"]


def test_top_tickers_presion(tmp_path, monkeypatch):
    """La presion compradora agrega el importance_score de las senales buy."""
    public = tmp_path / "public"
    monkeypatch.setattr(lc, "PUBLIC_DIR", public)
    _seed(public, **{
        "signals_30d.json": [
            {"ticker": "AAA", "asset_name": "Alpha", "source_type": "corporate_insider",
             "direction": "buy", "importance_score": 50},
            {"ticker": "AAA", "asset_name": "Alpha", "source_type": "congress",
             "direction": "buy", "importance_score": 30},
            {"ticker": "BBB", "asset_name": "Beta", "source_type": "corporate_insider",
             "direction": "sell", "importance_score": 70}],
        "news_context_30d.json": [], "top_movements_30d.json": {},
        "health_report.json": {}, "institutional_changes_latest.json": [],
        "sec_13d_13g_30d.json": [], "polymarket_smart_traders.json": [],
        "polymarket_whales.json": []})
    ctx = lc.build()
    buy = {e["ticker"]: e for e in ctx["top_tickers"]["buy_pressure"]}
    sell = {e["ticker"]: e for e in ctx["top_tickers"]["sell_pressure"]}
    assert buy["AAA"]["pressure_score"] == 80  # 50 + 30
    assert "BBB" in sell
