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


def test_option_exercise_no_es_compra():
    """Codigo M (ejercicio de opciones) no debe clasificarse como buy ni formar cluster."""
    recs = [
        {"id": "m1", "insider_name": "Ann", "insider_title": "CEO", "ticker": "MIAX",
         "tx_code": "M", "value_usd": 5e5, "tx_date": "2026-07-07"},
        {"id": "m2", "insider_name": "Bob", "insider_title": "CFO", "ticker": "MIAX",
         "tx_code": "M", "value_usd": 3e5, "tx_date": "2026-07-07"},
    ]
    import json as _json
    from unittest.mock import patch
    with patch.object(bs, "_load", lambda name: recs if "insiders" in name else []):
        sigs = bs._from_insiders()
    assert all(s["direction"] == "other" for s in sigs)
    # y no cuentan para cluster buying
    assert detect_clusters(sigs) == {}


def test_cluster_no_infla_ventas():
    """El componente cluster del score no debe aplicarse a las ventas."""
    sell = _ins("MIAX", "Ann", code="S")
    with_cluster = insider_signal_score(sell, {"MIAX": 7})
    without = insider_signal_score(sell, {})
    assert with_cluster == without


def test_cluster_buy_flag_solo_en_compras(tmp_path, monkeypatch):
    """El flag cluster_buy no debe aparecer en señales de venta."""
    public = tmp_path / "public"
    public.mkdir()
    monkeypatch.setattr(bs, "PUBLIC_DIR", public)

    def w(name, data): (public / name).write_text(json.dumps(data), encoding="utf-8")
    w("sec_insiders_30d.json", [
        {"id": "b1", "insider_name": "Ann", "insider_title": "CEO", "ticker": "DPC",
         "tx_code": "P", "value_usd": 1e6, "tx_date": "2026-06-20"},
        {"id": "b2", "insider_name": "Bob", "insider_title": "CFO", "ticker": "DPC",
         "tx_code": "P", "value_usd": 5e5, "tx_date": "2026-06-21"},
        {"id": "s1", "insider_name": "Cid", "insider_title": "Director", "ticker": "DPC",
         "tx_code": "S", "value_usd": 8e5, "tx_date": "2026-06-22"}])
    w("congress_trades_30d.json", [])
    w("sec_13d_13g_30d.json", [])
    w("institutional_changes_latest.json", [])
    w("health_report.json", {"datasets": {}})
    sigs = bs.build()
    buys = [s for s in sigs if s["direction"] == "buy"]
    sells = [s for s in sigs if s["direction"] == "sell"]
    assert buys and sells
    assert all("cluster_buy" in s["risk_flags"] for s in buys)
    assert all("cluster_buy" not in s["risk_flags"] for s in sells)


def test_top_movements_dedup_misma_transaccion(tmp_path, monkeypatch):
    """La misma transaccion firmada por varios insiders sale una sola vez."""
    import pipelines.build_top_movements as tm
    public = tmp_path / "public"
    public.mkdir()
    monkeypatch.setattr(tm, "PUBLIC_DIR", public)

    def w(name, data): (public / name).write_text(json.dumps(data), encoding="utf-8")
    # 3 firmantes distintos declaran la MISMA venta en bloque ($1.0B, mismo dia)
    same = {"ticker": "OLPX", "direction": "sell", "amount_estimated": 1028905668.26,
            "event_date": "2026-07-07", "source_type": "corporate_insider",
            "importance_score": 90}
    w("signals_30d.json", [
        {**same, "actor_name": "Advent", "actor_type": "ten_percent_owner"},
        {**same, "actor_name": "Glynn Tricia", "actor_type": "director"},
        {**same, "actor_name": "White Michael", "actor_type": "director"},
        {"ticker": "COE", "direction": "buy", "amount_estimated": 9.3e6,
         "event_date": "2026-07-02", "actor_name": "Huang Jack",
         "actor_type": "ceo", "importance_score": 80},
    ])
    w("news_context_30d.json", [])
    data = tm.build()
    olpx = [m for m in data["movements"] if m["ticker"] == "OLPX"]
    assert len(olpx) == 1
    assert data["count"] == 2


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
