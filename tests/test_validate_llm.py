"""Tests del validador de respuestas del LLM (Fase H-validate)."""

from __future__ import annotations

import json

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
