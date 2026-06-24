"""Schema unificado para los outputs de WATCHDOG.

Centraliza claves canonicas, helpers de dedup y validacion ligera.
Los scrapers escriben en data/*.json siguiendo estos esquemas.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

# Campos requeridos por modelo (para validacion y tests)
CONGRESS_REQUIRED = {
    "id",
    "politician",
    "chamber",
    "party",
    "ticker",
    "asset_name",
    "tx_type",
    "amount_range",
    "tx_date",
    "disclosure_date",
    "source_url",
}

INSIDER_REQUIRED = {
    "id",
    "insider_name",
    "insider_title",
    "company",
    "ticker",
    "tx_type",
    "shares",
    "price_per_share",
    "tx_date",
    "source_url",
}

INSTITUTIONAL_REQUIRED = {
    "manager",
    "cik",
    "report_date",
    "holdings",
    "source_url",
}

POLYMARKET_REQUIRED = {
    "wallet",
    "username",
    "category",
    "pnl",
    "volume",
    "markets_traded",
    "win_rate_positions",
    "top_positions",
}


def stable_id(*parts: Any) -> str:
    """Genera un hash sha1 (16 chars) determinista a partir de los args.

    Sirve como ID estable para deduplicar trades de congresistas, ya que
    las fuentes no exponen un ID propio consistente.
    """
    joined = "||".join("" if p is None else str(p) for p in parts)
    return hashlib.sha1(joined.encode("utf-8")).hexdigest()[:16]


def dedupe_by_key(records: Iterable[dict], key: str = "id") -> list[dict]:
    """Elimina duplicados conservando el primero por clave (default 'id')."""
    seen: set[str] = set()
    out: list[dict] = []
    for r in records:
        k = r.get(key)
        if k is None or k in seen:
            continue
        seen.add(k)
        out.append(r)
    return out


def validate_records(records: list[dict], required: set[str], name: str) -> None:
    """Lanza ValueError si algun registro no tiene los campos requeridos.

    Solo verifica el primer registro deficiente para no spammear logs.
    """
    if not records:
        raise ValueError(f"[{name}] lista vacia")
    for i, r in enumerate(records):
        missing = required - set(r.keys())
        if missing:
            raise ValueError(
                f"[{name}] registro #{i} falta campos {sorted(missing)}: {r!r}"
            )


def write_json(path: Path, data: Any) -> Path:
    """Escribe JSON con indent=2, UTF-8, y separators compactos en arrays grandes.

    Crea el directorio padre si no existe.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    return path
