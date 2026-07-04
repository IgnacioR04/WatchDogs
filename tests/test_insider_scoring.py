"""Tests del scoring fino de insiders y cluster (normalize/insider_scoring.py)."""

from __future__ import annotations

import json

import pipelines.build_signals as bs
from normalize.insider_scoring import (
    confidence,
    detect_clusters,
    insider_signal_score,
    risk_flags,
)


def _ins(ticker, actor, code="P", value=100000):
    return {"ticker": ticker, "actor_name": actor, "tx_code": code,
            "direction": "buy" if code == "P" else "sell",
            "amount_estimated": value, "actor_type": "director"}


def test_detect_clusters_cuenta_insiders_distintos():
    """Cluster = >=2 insiders distintos comprando (P) el mismo ticker."""
    sigs = [
        _ins("DPC", "Ann"), _ins("DPC", "Bob"), _ins("DPC", "Cid"),
        _ins("DPC", "Ann"),  # mismo insider, no cuenta doble
        _ins("XYZ", "Solo"),                    # solo 1 -> no cluster
        _ins("SEL", "Ann", code="S"),           # venta -> no cuenta
    ]
    clusters = detect_clusters(sigs)
    assert clusters.get("DPC") == 3
    assert "XYZ" not in clusters
    assert "SEL" not in clusters


def test_insider_signal_score_cluster_sube():
    """Una compra P con cluster puntua mas que sin cluster."""
    sig = _ins("DPC", "Ann")
    with_cluster = insider_signal_score(sig, {"DPC": 5})
    without = insider_signal_score(sig, {})
    assert with_cluster > without


def test_signal_score_compra_mayor_que_grant():
    """Codigo P (compra abierta) puntua mas que A (grant)."""
    buy = insider_signal_score(_ins("X", "A", code="P"), {})
    grant = insider_signal_score(_ins("X", "A", code="A"), {})
    assert buy > grant


def test_risk_flags_detecta_problemas():
    """risk_flags marca stale, low confidence, small amount, non-discretionary."""
    assert "stale_disclosure" in risk_flags({"delay_days": 90})
    assert "low_ticker_confidence" in risk_flags({"ticker_confidence": 0.3, "ticker": "X"})
    assert "small_amount" in risk_flags({"amount_estimated": 5000, "ticker": "X"})
    assert "non_discretionary" in risk_flags({"tx_code": "F", "ticker": "X"})
    assert "no_ticker" in risk_flags({"ticker": ""})


def test_confidence_baja_con_flags():
    """confidence baja al haber risk_flags."""
    high = confidence({"ticker_confidence": 0.98, "risk_flags": []})
    low = confidence({"ticker_confidence": 0.98, "risk_flags": ["a", "b"]})
    assert high > low


def test_build_health_gating(tmp_path, monkeypatch):
    """build() descarta señales de una fuente en estado 'error'."""
    public = tmp_path / "public"
    public.mkdir()
    monkeypatch.setattr(bs, "PUBLIC_DIR", public)

    def w(name, data): (public / name).write_text(json.dumps(data), encoding="utf-8")
    w("sec_insiders_30d.json", [
        {"id": "i1", "insider_name": "X", "insider_title": "CEO", "ticker": "NVDA",
         "tx_code": "P", "value_usd": 1e6, "tx_date": "2026-06-20"}])
    w("congress_trades_30d.json", [
        {"id": "c1", "source": "house_pdf_parsed", "politician": "Y", "actor_type": "house_rep",
         "ticker": "AAPL", "tx_type": "purchase", "direction": "buy",
         "amount_estimated": 50000, "tx_date": "2026-06-19"}])
    w("sec_13d_13g_30d.json", [])
    w("institutional_changes_latest.json", [])
    # health: congress en error -> se descarta
    w("health_report.json", {"datasets": {"congress": {"status": "error"},
                                          "sec_insiders": {"status": "ok"}}})
    sigs = bs.build()
    srcs = {s["source_type"] for s in sigs}
    assert "corporate_insider" in srcs
    assert "congress" not in srcs  # gated por error
    # las señales tienen el schema v3
    for s in sigs:
        assert "signal_score" in s and "risk_flags" in s and "confidence" in s
