"""Parser de PDFs de PTR de la Camara: extrae transacciones reales.

Descarga el PDF de cada PTR (filing tipo P) del House Clerk y extrae las
transacciones individuales: ticker, activo, tipo, fecha e importe. El ticker
viene en parentesis explicitos en el PDF (ej '(AMZN)'), por lo que la confianza
es alta y NO se inventa ningun ticker por heuristica.

Estructura tipica de una fila en el texto extraido:
    Amazon.com, Inc. - Common Stock (AMZN) [ST] S (partial) 03/16/202603/16/2026$1,001 - $15,000

Algunos PTRs son escaneos sin capa de texto (pypdf no extrae nada): se marcan
como no parseables y se omiten (no rompen el pipeline).

Genera registros normalizados al schema de congress y los combina con el
historico de Senate (mirror) en data/public/congress_trades_30d.json.
"""

from __future__ import annotations

import io
import re
from pathlib import Path
from typing import Any

import pypdf

from normalize.scoring import score_signal
from scrapers._dates import delay_days, to_iso
from scrapers._http import Client, UA_DEFAULT
from scrapers.congress_house_pdf_index import PTRFiling, fetch_index

OUT_PATH = Path(__file__).resolve().parents[1] / "data" / "public" / "congress_trades_30d.json"

# Regex de una fila de transaccion. El ticker va entre parentesis (patron
# explicito = alta confianza). Capturamos: activo, ticker, tipo, 2 fechas, importe.
ROW_RE = re.compile(
    r"([A-Za-z0-9][^\n(]{1,90}?)\s*"                       # 1: nombre del activo
    r"\(([A-Z][A-Z.\-/]{0,5})\)\s*"                         # 2: ticker
    r"\[[A-Z]{2}\]\s*"                                       # marcador tipo activo [ST]
    r"(P \(partial\)|S \(partial\)|S \(full\)|P|S|E)\s*"     # 3: tipo de transaccion
    r"(\d{2}/\d{2}/\d{4})(\d{2}/\d{2}/\d{4})\s*"             # 4,5: fecha tx + fecha notif
    r"(\$[\d,]+\s*-\s*\$[\d,]+|Over \$[\d,]+|\$[\d,]+\+?)"   # 6: importe
)

TX_TYPE_MAP = {
    "P": "purchase", "P (partial)": "purchase",
    "S": "sale", "S (partial)": "sale", "S (full)": "sale",
    "E": "exchange",
}


def _parse_amount(raw: str) -> tuple[int | None, int | None]:
    """Convierte un rango de importe a (min, max) en USD enteros."""
    nums = [int(n.replace(",", "")) for n in re.findall(r"\$([\d,]+)", raw)]
    if not nums:
        return None, None
    if raw.strip().lower().startswith("over"):
        return nums[0], None
    if len(nums) == 1:
        return nums[0], nums[0]
    return nums[0], nums[1]


def _clean_asset(name: str) -> str:
    """Limpia el nombre del activo (quita sufijos de clase y espacios sobrantes)."""
    n = re.sub(r"\s*-\s*(Common Stock|Class [A-Z]|Ordinary Shares).*$", "", name).strip()
    return n[:120]


def _us_to_iso(d: str) -> str:
    """MM/DD/YYYY -> ISO."""
    return to_iso(d)


def parse_pdf_text(text: str) -> list[dict[str, Any]]:
    """Extrae las transacciones de un texto de PTR. Devuelve dicts crudos."""
    out: list[dict[str, Any]] = []
    for m in ROW_RE.finditer(text):
        asset, ticker, txtype, d_tx, d_notif, amount = m.groups()
        amin, amax = _parse_amount(amount)
        out.append({
            "asset_name": _clean_asset(asset),
            "ticker": ticker.strip("."),
            "tx_type": TX_TYPE_MAP.get(txtype, "other"),
            "tx_date": _us_to_iso(d_tx),
            "notification_date": _us_to_iso(d_notif),
            "amount_min": amin,
            "amount_max": amax,
        })
    return out


def parse_filing(filing: PTRFiling, client: Client) -> list[dict[str, Any]]:
    """Descarga y parsea el PDF de un PTR. Devuelve registros normalizados.

    Si el PDF es un escaneo sin texto, devuelve [] (no parseable).
    """
    try:
        r = client.get(filing.pdf_url, timeout=60)
        if r.status_code != 200 or not r.content:
            return []
        reader = pypdf.PdfReader(io.BytesIO(r.content))
        text = "\n".join(p.extract_text() or "" for p in reader.pages)
    except Exception:
        return []
    if len(text.strip()) < 50:
        return []  # escaneo sin capa de texto

    rows = parse_pdf_text(text)
    records: list[dict[str, Any]] = []
    for i, row in enumerate(rows):
        rec = {
            "id": f"house_{filing.doc_id}_{i}",
            "source": "house_pdf_parsed",
            "source_type": "congress",
            "politician": filing.politician,
            "actor_name": filing.politician,
            "actor_type": "house_rep",
            "chamber": "house",
            "party": "",                       # no esta en datos del Clerk
            "state": filing.state_dst,
            "related_person": "",
            "ticker": row["ticker"],
            "ticker_source": "pdf_explicit_field",
            "ticker_confidence": 0.95,
            "asset_name": row["asset_name"],
            "tx_type": row["tx_type"],
            "direction": "buy" if row["tx_type"] == "purchase" else (
                "sell" if row["tx_type"] == "sale" else "other"),
            "amount_min": row["amount_min"],
            "amount_max": row["amount_max"],
            "amount_estimated": row["amount_max"] or row["amount_min"],
            "tx_date": row["tx_date"],
            "event_date": row["tx_date"],
            "disclosure_date": filing.filing_date,
            "delay_days": delay_days(row["tx_date"], filing.filing_date),
            "source_url": filing.pdf_url,
        }
        score_signal(rec)  # anade importance_score y sub-scores
        records.append(rec)
    return records


def run(recent_days: int = 45, max_filings: int = 200) -> Path:
    """Parsea los PTRs recientes del House y escribe congress_trades_30d.json.

    Solo procesa PTRs presentados en los ultimos `recent_days` dias (para no
    descargar cientos de PDFs). Combina con el historico de Senate del mirror.
    """
    from normalize.schema import write_json
    from scrapers import congress as congress_mirror

    client = Client(user_agent=UA_DEFAULT, max_per_sec=5)
    filings = fetch_index(recent_days=recent_days, client=client)[:max_filings]
    print(f"[house_pdf] {len(filings)} PTRs recientes a parsear")

    house_records: list[dict[str, Any]] = []
    parsed_ok = 0
    no_text = 0
    for i, f in enumerate(filings):
        recs = parse_filing(f, client)
        if recs:
            parsed_ok += 1
            house_records.extend(recs)
        else:
            no_text += 1
        if (i + 1) % 25 == 0:
            print(f"  {i + 1}/{len(filings)} ({len(house_records)} tx)")

    # Senate historico (mirror) como contexto adicional, marcado por su fuente.
    try:
        senate = congress_mirror.fetch_senate(congress_mirror.make_session())
    except Exception as e:
        print(f"  [senate_mirror] no disponible: {e}")
        senate = []

    combined = house_records + senate
    combined.sort(key=lambda r: r.get("disclosure_date") or r.get("tx_date") or "", reverse=True)
    write_json(OUT_PATH, combined)
    print(
        f"[house_pdf] {parsed_ok} PTRs con texto, {no_text} escaneos, "
        f"{len(house_records)} transacciones House + {len(senate)} Senate -> {OUT_PATH}"
    )
    return OUT_PATH


if __name__ == "__main__":
    run()
