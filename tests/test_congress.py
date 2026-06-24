"""Tests del scraper de Congress (House + Senate).

Hace una corrida real contra los datasets publicos. Marca como xfail si la
red esta caida o el host devuelve 5xx (no es bug nuestro).
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import requests

from normalize.schema import CONGRESS_REQUIRED
from scrapers import congress


def _network_ok() -> bool:
    """Comprueba si tenemos red basica antes de pedir endpoints reales."""
    try:
        requests.head("https://aws.amazon.com", timeout=5)
        return True
    except Exception:
        return False


@pytest.mark.skipif(not _network_ok(), reason="sin conectividad")
def test_run_genera_json_con_minimos():
    """Run completo: descarga + normaliza + escribe JSON con >100 registros."""
    out_path = congress.run()
    assert Path(out_path).exists()
    data = json.loads(Path(out_path).read_text(encoding="utf-8"))
    assert isinstance(data, list)
    assert len(data) > 100, f"esperaba >100 trades, hay {len(data)}"
    # El primer registro debe tener todos los campos requeridos
    for k in CONGRESS_REQUIRED:
        assert k in data[0], f"falta campo {k}"
    # Chamber debe ser house o senate
    assert {r["chamber"] for r in data[:50]}.issubset({"house", "senate"})


def test_norm_tx_type_canonicaliza():
    """Tests unitarios de la normalizacion de tx_type."""
    assert congress._norm_tx_type("Purchase") == "purchase"
    assert congress._norm_tx_type("Sale (Full)") == "sale"
    assert congress._norm_tx_type("Sale (Partial)") == "sale"
    assert congress._norm_tx_type("EXCHANGE") == "exchange"
    assert congress._norm_tx_type(None) == "other"
    assert congress._norm_tx_type("") == "other"
    assert congress._norm_tx_type("weird") == "other"


def test_clean_ticker_quita_dolar_y_basura():
    """Tickers se limpian a uppercase, sin '$', sin '--', sin espacios."""
    assert congress._clean_ticker("$nvda") == "NVDA"
    assert congress._clean_ticker(" aapl ") == "AAPL"
    assert congress._clean_ticker("--") == ""
    assert congress._clean_ticker(None) == ""
    assert congress._clean_ticker("BRK/B Common") == "BRK/B"
