"""Tests de scrapers SEC (insiders y 13F).

Tests unitarios sobre parseo de XML. Los tests de red estan separados y
marcados con `@pytest.mark.network` para poder ejecutarlos solo bajo demanda.
"""

from __future__ import annotations

import pytest
import requests

from scrapers import sec_13f, sec_insider

FORM4_SAMPLE = """<?xml version="1.0" encoding="UTF-8"?>
<ownershipDocument>
  <issuer>
    <issuerCik>0001045810</issuerCik>
    <issuerName>NVIDIA CORP</issuerName>
    <issuerTradingSymbol>NVDA</issuerTradingSymbol>
  </issuer>
  <reportingOwner>
    <reportingOwnerId>
      <rptOwnerName>HUANG JEN-HSUN</rptOwnerName>
    </reportingOwnerId>
    <reportingOwnerRelationship>
      <isDirector>1</isDirector>
      <isOfficer>1</isOfficer>
      <officerTitle>President and CEO</officerTitle>
    </reportingOwnerRelationship>
  </reportingOwner>
  <nonDerivativeTable>
    <nonDerivativeTransaction>
      <transactionDate><value>2025-06-15</value></transactionDate>
      <transactionCoding>
        <transactionCode>S</transactionCode>
      </transactionCoding>
      <transactionAmounts>
        <transactionShares><value>120000</value></transactionShares>
        <transactionPricePerShare><value>130.50</value></transactionPricePerShare>
      </transactionAmounts>
    </nonDerivativeTransaction>
  </nonDerivativeTable>
</ownershipDocument>
"""

INFO_TABLE_SAMPLE = """<?xml version="1.0" encoding="UTF-8"?>
<informationTable xmlns="http://www.sec.gov/edgar/document/thirteenf/informationtable">
  <infoTable>
    <nameOfIssuer>APPLE INC</nameOfIssuer>
    <titleOfClass>COM</titleOfClass>
    <cusip>037833100</cusip>
    <value>158472000000</value>
    <shrsOrPrnAmt>
      <sshPrnamt>905560000</sshPrnamt>
      <sshPrnamtType>SH</sshPrnamtType>
    </shrsOrPrnAmt>
  </infoTable>
  <infoTable>
    <nameOfIssuer>BANK OF AMERICA CORP</nameOfIssuer>
    <titleOfClass>COM</titleOfClass>
    <cusip>060505104</cusip>
    <value>41314000000</value>
    <shrsOrPrnAmt>
      <sshPrnamt>1032852000</sshPrnamt>
      <sshPrnamtType>SH</sshPrnamtType>
    </shrsOrPrnAmt>
  </infoTable>
</informationTable>
"""


def test_parse_form4_extrae_insider_y_tx():
    """Parseo de XML Form 4: insider name, titulo, ticker, transaction."""
    parsed = sec_insider._parse_form4_xml(FORM4_SAMPLE)
    assert parsed is not None
    assert parsed["company"] == "NVIDIA CORP"
    assert parsed["ticker"] == "NVDA"
    assert parsed["insider_name"] == "HUANG JEN-HSUN"
    assert "Director" in parsed["insider_title"]
    assert "President and CEO" in parsed["insider_title"]
    assert len(parsed["transactions"]) == 1
    tx = parsed["transactions"][0]
    assert tx["tx_date"] == "2025-06-15"
    assert tx["tx_code"] == "S"
    assert tx["shares"] == "120000"
    assert tx["price"] == "130.50"


def test_parse_form4_xml_invalido_devuelve_none():
    """XML invalido -> None, no excepcion."""
    assert sec_insider._parse_form4_xml("<not xml") is None


def test_parse_info_table_extrae_holdings():
    """Parseo de informationTable: nameOfIssuer, cusip, value, shares."""
    holdings = sec_13f._parse_info_table(INFO_TABLE_SAMPLE)
    assert len(holdings) == 2
    aapl = holdings[0]
    assert aapl["asset_name"] == "APPLE INC"
    assert aapl["cusip"] == "037833100"
    assert aapl["shares"] == 905560000
    assert aapl["value_usd"] == 158472000000


def test_tx_code_map_cubre_codigos_principales():
    """Los codigos P/S/A/D/F/M deben tener etiqueta legible."""
    for code in ["P", "S", "A", "D", "F", "M"]:
        assert code in sec_insider.TX_CODE_MAP
        assert sec_insider.TX_CODE_MAP[code].startswith(code + "-")
