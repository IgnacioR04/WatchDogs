"""Tests del sistema de scoring (normalize/scoring.py)."""

from __future__ import annotations

from normalize.scoring import (
    actor_score,
    amount_score,
    freshness_score,
    rarity_score,
    score_signal,
)


def test_score_signal_devuelve_scores_en_rango():
    """score_signal añade importance_score y sub-scores, todos 0-100."""
    sig = {
        "actor_type": "ceo",
        "source": "sec_form_4",
        "value_usd": 15_660_000,
        "event_date": "2026-06-18",
        "disclosure_date": "2026-06-20",
        "tx_code": "S",
    }
    out = score_signal(dict(sig))
    for key in ("actor_score", "amount_score", "source_quality_score",
                "freshness_score", "rarity_score", "importance_score"):
        assert key in out, f"falta {key}"
        assert 0 <= out[key] <= 100, f"{key}={out[key]} fuera de rango"
    assert out["delay_days"] == 2


def test_amount_score_escala_logaritmica():
    """amount_score crece con el tamaño, saturando en 100."""
    assert amount_score(10_000) < amount_score(1_000_000) < amount_score(100_000_000)
    assert amount_score(100_000_000) == 100.0
    assert amount_score(None) == 40.0  # neutro-bajo sin importe
    assert amount_score(0) == 40.0


def test_freshness_score_por_tramos():
    """freshness_score respeta los tramos del informe."""
    assert freshness_score(0) == 100.0
    assert freshness_score(1) == 100.0
    assert freshness_score(5) == 90.0
    assert freshness_score(20) == 70.0
    assert freshness_score(40) == 55.0
    assert freshness_score(100) == 25.0
    assert freshness_score(None) == 60.0


def test_actor_score_tabla():
    """actor_score usa la tabla y cae a 50 para desconocidos."""
    assert actor_score("ceo") == 95.0
    assert actor_score("senator") == 85.0
    assert actor_score("director") == 75.0
    assert actor_score("algo_raro") == 50.0
    assert actor_score(None) == 50.0


def test_rarity_premia_compra_abierta():
    """Una compra en mercado abierto (P) es mas rara que un grant (A)."""
    assert rarity_score({"tx_code": "P"}) > rarity_score({"tx_code": "A"})
    assert rarity_score({"tx_code": "P"}) == 90.0
    assert rarity_score({}) == 60.0


def test_cross_source_normaliza_0_1():
    """cross_source_score que viene en 0-1 se escala a 0-100."""
    out = score_signal({"actor_type": "ceo", "source": "sec_form_4",
                        "cross_source_score": 0.4, "value_usd": 1000})
    assert out["cross_source_score"] == 40.0
