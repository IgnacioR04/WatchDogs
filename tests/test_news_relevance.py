"""Tests del filtro de relevancia de noticias GDELT."""

from __future__ import annotations

from scrapers.news_gdelt import _clean_company_query, _is_relevant


def test_titular_de_la_empresa_pasa():
    q = _clean_company_query("CROWDSTRIKE HOLDINGS INC", "CRWD")
    assert _is_relevant("CrowdStrike stock rises after earnings beat", "CRWD", q)


def test_titular_con_ticker_pasa():
    q = _clean_company_query("CROWDSTRIKE HOLDINGS INC", "CRWD")
    assert _is_relevant("Analysts upgrade CRWD to buy", "CRWD", q)


def test_titular_sin_relacion_se_descarta():
    q = _clean_company_query("CROWDSTRIKE HOLDINGS INC", "CRWD")
    assert not _is_relevant(
        "Universal Technical Institute CEO Sold Company Shares", "CRWD", q)


def test_nombre_multi_palabra_no_matchea_por_palabra_generica():
    # 'Super' a secas no debe bastar: exigimos 'super micro' (2 palabras).
    q = _clean_company_query("SUPER MICRO COMPUTER INC", "SMCI")
    assert not _is_relevant("Super Bowl ads break records", "SMCI", q)
    assert _is_relevant("Super Micro raided by Taiwan authorities", "SMCI", q)
