"""Tests de SEC 13D/13G (scrapers/sec_13d_13g.py) y Senate eFD."""

from __future__ import annotations

import requests

from scrapers import sec_13d_13g, senate_efd

SAMPLE_XML = """<?xml version="1.0"?>
<edgarSubmission>
  <headerData><submissionType>SCHEDULE 13D/A</submissionType></headerData>
  <formData>
    <coverPageHeader>
      <issuerName>Navigator Holdings Ltd.</issuerName>
      <issuerCIK>0001581804</issuerCIK>
      <issuerCusipNumber>Y62132108</issuerCusipNumber>
      <dateOfEvent>06/22/2026</dateOfEvent>
    </coverPageHeader>
    <reportingPersonName>BW Group Limited</reportingPersonName>
    <reportingPersonCIK>0001649312</reportingPersonCIK>
    <aggregateAmountOwned>6089011.00</aggregateAmountOwned>
    <percentOfClass>9.87</percentOfClass>
  </formData>
</edgarSubmission>
"""


def test_extract_ticker_de_display_name():
    """Extrae el ticker del display_name del issuer."""
    assert sec_13d_13g._extract_ticker("Navigator Holdings Ltd.  (NVGS)  (CIK 0001581804)") == "NVGS"
    assert sec_13d_13g._extract_ticker("Foo Corp (CIK 0001)") == ""


def test_parse_primary_doc_xml():
    """Parsea los campos clave del primary_doc.xml estructurado."""
    f = sec_13d_13g.parse_primary_doc(SAMPLE_XML)
    assert f["submissionType"] == "SCHEDULE 13D/A"
    assert f["issuerName"] == "Navigator Holdings Ltd."
    assert f["percentOfClass"] == "9.87"
    assert f["aggregateAmountOwned"] == "6089011.00"
    assert f["reportingPersonName"] == "BW Group Limited"


def test_parse_primary_doc_invalido():
    """XML invalido -> dict vacio, sin excepcion."""
    assert sec_13d_13g.parse_primary_doc("<not xml") == {}


def test_hit_to_record_schema():
    """hit_to_record construye el schema esperado (con cliente mockeado)."""
    class _FakeResp:
        status_code = 200
        text = SAMPLE_XML

    class _FakeClient:
        def get(self, url, timeout=30):
            return _FakeResp()

    hit = {
        "_id": "0001213900-26-071731:primary_doc.xml",
        "_source": {
            "display_names": ["Navigator Holdings Ltd.  (NVGS)  (CIK 0001581804)",
                              "BW Group Ltd  (CIK 0001649312)"],
            "ciks": ["0001581804", "0001649312"],
            "file_date": "2026-06-25",
            "file_type": "SCHEDULE 13D/A",
        },
    }
    rec = sec_13d_13g.hit_to_record(_FakeClient(), hit)
    assert rec["ticker"] == "NVGS"
    assert rec["company"] == "Navigator Holdings Ltd."
    assert rec["ownership_pct"] == 9.87
    assert rec["shares_owned"] == 6089011
    assert rec["filer_name"] == "BW Group Limited"
    assert rec["source"] == "sec_13d"
    assert 0 <= rec["importance_score"] <= 100


def test_senate_efd_detecta_bloqueo_akamai():
    """_is_akamai_block detecta la pagina de bloqueo (403 / Access Denied)."""
    class _R403:
        status_code = 403
        text = "<HTML><HEAD><TITLE>Access Denied</TITLE>"

    class _Rok:
        status_code = 200
        text = "<html>contenido normal</html>"

    assert senate_efd._is_akamai_block(_R403()) is True
    assert senate_efd._is_akamai_block(_Rok()) is False
