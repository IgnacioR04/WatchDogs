"""Tests de deduplicacion (normalize/dedup.py)."""

from __future__ import annotations

from normalize.dedup import deduplicate, stable_id


def test_stable_id_determinista():
    """El mismo registro produce siempre el mismo ID."""
    rec = {
        "accession": "0001-26-1",
        "insider_name": "HUANG",
        "ticker": "NVDA",
        "tx_date": "2026-06-18",
        "tx_code": "S",
        "shares": 120000,
        "price_per_share": 130.5,
    }
    id1 = stable_id("sec_form_4", rec)
    id2 = stable_id("sec_form_4", dict(rec))
    assert id1 == id2
    assert id1.startswith("sec_form_4_")


def test_stable_id_cambia_con_los_campos():
    """Cambiar un campo clave cambia el ID."""
    base = {"accession": "0001-26-1", "insider_name": "HUANG", "ticker": "NVDA",
            "tx_date": "2026-06-18", "tx_code": "S", "shares": 120000, "price_per_share": 130.5}
    other = dict(base, shares=999)
    assert stable_id("sec_form_4", base) != stable_id("sec_form_4", other)


def test_stable_id_usa_alias():
    """stable_id resuelve campos por alias (insider_name -> owner)."""
    a = {"accession": "x", "owner": "HUANG", "ticker": "NVDA", "tx_date": "2026-06-18",
         "tx_code": "S", "shares": 1, "price": 2}
    b = {"accession": "x", "insider_name": "HUANG", "ticker": "NVDA", "tx_date": "2026-06-18",
         "tx_code": "S", "shares": 1, "price_per_share": 2}
    assert stable_id("sec_form_4", a) == stable_id("sec_form_4", b)


def test_deduplicate_elimina_duplicados_en_batch():
    """En un batch con un duplicado, deduplicate devuelve solo los unicos."""
    r1 = {"accession": "0001-26-1", "insider_name": "HUANG", "ticker": "NVDA",
          "tx_date": "2026-06-18", "tx_code": "S", "shares": 120000, "price_per_share": 130.5}
    r2 = {"accession": "0001-26-2", "insider_name": "X", "ticker": "AAPL",
          "tx_date": "2026-06-19", "tx_code": "P", "shares": 1000, "price_per_share": 200}
    new, seen = deduplicate([r1, dict(r1), r2], "sec_form_4")
    assert len(new) == 2
    assert len(seen) == 2
    assert all("id" in r for r in new)


def test_deduplicate_contra_seen_ids_previos():
    """Un segundo run con los mismos registros no añade nada nuevo."""
    r1 = {"accession": "a", "insider_name": "X", "ticker": "AAPL", "tx_date": "2026-06-19",
          "tx_code": "P", "shares": 1, "price_per_share": 1}
    new1, seen1 = deduplicate([r1], "sec_form_4")
    assert len(new1) == 1
    new2, seen2 = deduplicate([dict(r1)], "sec_form_4", seen1)
    assert len(new2) == 0
    assert seen2 == seen1
