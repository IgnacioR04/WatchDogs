"""Tests del validador de respuestas del LLM (Fase H-validate)."""

from __future__ import annotations

import json

import pipelines.validate_llm_output as vlo
from pipelines.validate_llm_output import (
    check_hard_constraints,
    parse_llm_response,
)


def test_parse_json_puro():
    p = parse_llm_response('{"verdict":"accept","final_weights":{"SPY":0.1}}')
    assert p["verdict"] == "accept"


def test_parse_json_en_bloque_markdown():
    txt = 'Claro, aqui tienes:\n```json\n{"verdict":"adjust","final_weights":{"SPY":0.2}}\n```\nEspero que ayude.'
    p = parse_llm_response(txt)
    assert p["verdict"] == "adjust"
    assert p["final_weights"]["SPY"] == 0.2


def test_constraints_ok():
    w = {"SPY": 0.12, "QQQ": 0.10}
    v = check_hard_constraints(w, allowed={"SPY", "QQQ", "TLT"}, budget=0.9, max_position=0.12)
    assert v == []


def test_constraints_ticker_fuera_universo():
    w = {"SPY": 0.1, "TSLA": 0.1}
    v = check_hard_constraints(w, allowed={"SPY"}, budget=0.9, max_position=0.15)
    assert any("universo" in x for x in v)


def test_constraints_excede_peso_maximo():
    w = {"SPY": 0.30}
    v = check_hard_constraints(w, allowed={"SPY"}, budget=0.9, max_position=0.12)
    assert any("maximo" in x for x in v)


def test_constraints_excede_presupuesto():
    w = {"SPY": 0.5, "QQQ": 0.5}
    v = check_hard_constraints(w, allowed={"SPY", "QQQ"}, budget=0.6, max_position=0.6)
    assert any("presupuesto" in x for x in v)


def test_constraints_pesos_negativos():
    w = {"SPY": 0.1, "QQQ": -0.05}
    v = check_hard_constraints(w, allowed={"SPY", "QQQ"}, budget=0.9, max_position=0.5)
    assert any("negativos" in x for x in v)


def test_held_tickers_incluye_cartera_aprobada(tmp_path, monkeypatch):
    """Las posiciones de la ultima cartera aprobada forman parte del universo."""
    monkeypatch.setattr(vlo, "PUBLIC_DIR", tmp_path)
    (tmp_path / "llm_portfolio.json").write_text(json.dumps(
        {"approved": True, "final_weights": {"HPE": 0.011, "PSBD": 0.031}}),
        encoding="utf-8")
    assert vlo._held_tickers() == {"HPE", "PSBD"}


def test_held_tickers_ignora_rechazadas(tmp_path, monkeypatch):
    """Una cartera rechazada no aporta posiciones al universo."""
    monkeypatch.setattr(vlo, "PUBLIC_DIR", tmp_path)
    (tmp_path / "llm_portfolio.json").write_text(json.dumps(
        {"approved": False, "final_weights": {"ZZZZ": 0.5}}), encoding="utf-8")
    assert vlo._held_tickers() == set()


def test_rechazo_no_pisa_cartera_aprobada(tmp_path, monkeypatch):
    """Un rechazo se escribe aparte; llm_portfolio.json (aprobada) queda intacta."""
    monkeypatch.setattr(vlo, "PUBLIC_DIR", tmp_path)
    monkeypatch.setattr(vlo, "OUTPUT_PATH", tmp_path / "llm_portfolio.json")
    monkeypatch.setattr(vlo, "DEFAULT_INPUT", tmp_path / "llm_response.txt")
    # estado aprobado previo
    approved = {"approved": True, "final_weights": {"SPY": 0.5}}
    (tmp_path / "llm_portfolio.json").write_text(json.dumps(approved), encoding="utf-8")
    # una propuesta que sera rechazada (ticker inventado)
    (tmp_path / "portfolio_proposal.json").write_text(json.dumps(
        {"profile": "moderado", "weights": {"SPY": 0.5}}), encoding="utf-8")
    (tmp_path / "regime.json").write_text(json.dumps(
        {"recommended_risk_budget": 0.9}), encoding="utf-8")
    (tmp_path / "signals_30d.json").write_text("[]", encoding="utf-8")
    (tmp_path / "llm_response.txt").write_text(json.dumps(
        {"verdict": "adjust", "final_weights": {"ZZZZFAKE": 0.5}}), encoding="utf-8")
    out = vlo.run()
    assert out.name == "llm_validation_rejected.json"
    rejected = json.loads(out.read_text(encoding="utf-8"))
    assert rejected["approved"] is False
    # la cartera aprobada sigue intacta
    kept = json.loads((tmp_path / "llm_portfolio.json").read_text(encoding="utf-8"))
    assert kept == approved
