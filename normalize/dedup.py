"""Deduplicacion de registros mediante IDs estables por fuente.

Cada fuente tiene un conjunto de campos clave que identifican univocamente un
registro (tabla del informe v2). `stable_id` genera un hash SHA256 determinista
de esos campos, de modo que el mismo registro produce siempre el mismo ID entre
runs distintos. Esto permite deduplicar contra un indice persistente.
"""

from __future__ import annotations

import hashlib
from typing import Any, Iterable

# Campos clave por fuente para construir el stable_id.
# El orden importa: define el orden de concatenacion en el hash.
KEY_FIELDS: dict[str, list[str]] = {
    "sec_form_4": ["accession", "owner", "ticker", "tx_date", "tx_code", "shares", "price"],
    "sec_form_3": ["accession", "owner", "ticker", "tx_date", "tx_code", "shares", "price"],
    "sec_form_5": ["accession", "owner", "ticker", "tx_date", "tx_code", "shares", "price"],
    "sec_13f": ["manager_cik", "quarter", "cusip", "value", "shares"],
    "sec_13d": ["accession", "filer_cik", "issuer_cik", "filing_date"],
    "sec_13g": ["accession", "filer_cik", "issuer_cik", "filing_date"],
    "congress": ["politician", "ticker", "tx_date", "amount_range", "source_doc_id"],
    "house_pdf": ["doc_id", "row_index", "asset", "tx_date", "amount"],
    "polymarket": ["wallet", "conditionId", "outcome", "timestamp", "realizedPnl"],
    "news": ["url"],
}

# Campos alternativos (alias) por si el registro usa otro nombre de clave.
FIELD_ALIASES: dict[str, list[str]] = {
    "owner": ["insider_name", "owner"],
    "ticker": ["ticker"],
    "tx_date": ["tx_date", "transaction_date", "event_date"],
    "price": ["price", "price_per_share"],
    "manager_cik": ["manager_cik", "cik"],
    "filer_cik": ["filer_cik"],
    "issuer_cik": ["issuer_cik"],
    "filing_date": ["filing_date", "disclosure_date"],
    "source_doc_id": ["source_doc_id", "doc_id"],
    "amount_range": ["amount_range"],
    "wallet": ["wallet", "proxyWallet"],
    "url": ["url", "source_url"],
}


def _resolve(record: dict[str, Any], field: str) -> str:
    """Resuelve el valor de un campo probando el nombre y sus alias."""
    if field in record and record[field] is not None:
        return str(record[field])
    for alias in FIELD_ALIASES.get(field, []):
        if alias in record and record[alias] is not None:
            return str(record[alias])
    return ""


def stable_id(source: str, record: dict[str, Any]) -> str:
    """Genera un ID estable (SHA256 truncado a 20 hex) para un registro.

    `source` debe ser una de las claves de KEY_FIELDS. Si no se reconoce, se
    usa un fallback que hashea todos los valores del registro ordenados.
    El ID lleva prefijo de fuente para legibilidad: 'sec_form_4_a1b2c3...'.
    """
    fields = KEY_FIELDS.get(source)
    if fields:
        parts = [_resolve(record, f) for f in fields]
    else:
        # Fallback determinista: todos los pares clave=valor ordenados.
        parts = [f"{k}={record[k]}" for k in sorted(record.keys())]
    raw = "||".join(parts)
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:20]
    return f"{source}_{digest}"


def deduplicate(
    records: Iterable[dict[str, Any]],
    source: str,
    seen_ids: set[str] | None = None,
) -> tuple[list[dict[str, Any]], set[str]]:
    """Deduplica `records` de una `source`, anadiendo 'id' a cada registro nuevo.

    Args:
        records: iterable de dicts a deduplicar.
        source: clave de fuente (para elegir los campos del stable_id).
        seen_ids: set de IDs ya vistos en runs anteriores (persistente). Si es
            None, se parte de vacio.

    Returns:
        (new_records, updated_seen_ids):
          - new_records: solo los registros cuyo ID no estaba en seen_ids ni
            duplicado dentro del propio batch. Cada uno lleva su campo 'id'.
          - updated_seen_ids: seen_ids ampliado con los IDs nuevos.
    """
    seen = set(seen_ids) if seen_ids else set()
    new_records: list[dict[str, Any]] = []
    batch_ids: set[str] = set()
    for r in records:
        rid = r.get("id") or stable_id(source, r)
        if rid in seen or rid in batch_ids:
            continue
        r["id"] = rid
        batch_ids.add(rid)
        new_records.append(r)
    seen |= batch_ids
    return new_records, seen
