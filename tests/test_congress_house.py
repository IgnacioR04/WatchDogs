"""Tests del parser de PDFs de House (scrapers/congress_house_pdf_parser.py)."""

from __future__ import annotations

from scrapers.congress_house_pdf_parser import _clean_asset, _parse_amount, parse_pdf_text

# Fragmento real del texto extraido de un PTR (formato del House Clerk).
SAMPLE_TEXT = """
ID Owner Asset Transaction Type Date Notification Date Amount
Amazon.com, Inc. - Common Stock (AMZN) [ST] S (partial) 03/16/202603/16/2026$1,001 - $15,000
Apple Inc. - Common Stock (AAPL) [ST] P 05/29/202605/30/2026$1,000,001 - $5,000,000
NVIDIA Corporation (NVDA) [ST] P (partial) 06/01/202606/02/2026$15,001 - $50,000
"""


def test_parse_pdf_text_extrae_transacciones():
    """Extrae ticker, tipo, fechas e importe de las filas del PTR."""
    rows = parse_pdf_text(SAMPLE_TEXT)
    assert len(rows) == 3
    by_ticker = {r["ticker"]: r for r in rows}
    assert by_ticker["AMZN"]["tx_type"] == "sale"
    assert by_ticker["AAPL"]["tx_type"] == "purchase"
    assert by_ticker["AAPL"]["amount_min"] == 1_000_001
    assert by_ticker["AAPL"]["amount_max"] == 5_000_000
    assert by_ticker["AAPL"]["tx_date"] == "2026-05-29"
    assert by_ticker["NVDA"]["tx_type"] == "purchase"


def test_parse_amount_rangos():
    """Convierte rangos de importe a (min, max)."""
    assert _parse_amount("$1,001 - $15,000") == (1001, 15000)
    assert _parse_amount("$1,000,001 - $5,000,000") == (1_000_001, 5_000_000)
    assert _parse_amount("Over $50,000,000") == (50_000_000, None)
    assert _parse_amount("nada") == (None, None)


def test_clean_asset_quita_sufijos():
    """Limpia sufijos de clase del nombre del activo."""
    assert _clean_asset("Apple Inc. - Common Stock") == "Apple Inc."
    assert _clean_asset("Alphabet Inc. - Class A") == "Alphabet Inc."


def test_no_inventa_tickers_sin_parentesis():
    """Texto sin tickers entre parentesis no produce filas (no inventa 'PDF')."""
    rows = parse_pdf_text("Some random text about PDF documents and LLC entities")
    assert rows == []
