"""Schema unificado para los outputs de WATCHDOG.

Centraliza claves canonicas, helpers de dedup y validacion ligera.
Los scrapers escriben en data/*.json siguiendo estos esquemas.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

# Campos del bloque temporal obligatorio en TODO registro normalizado (v3).
# Es el corazon del sistema: permite consulta historica y anti-lookahead.
TEMPORAL_FIELDS = {"event_date", "known_date", "scrape_date", "delay_days"}

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


def _to_iso_date(value: Any) -> str:
    """Normaliza una fecha a ISO YYYY-MM-DD. Acepta ISO, US (M/D/YYYY), timestamps.

    Devuelve '' si no se reconoce. Reimplementacion ligera para no crear
    dependencia circular con scrapers._dates.
    """
    if not value:
        return ""
    s = str(value).strip()
    if not s:
        return ""
    # ISO con hora -> recortar
    if "T" in s and len(s) >= 10 and s[4] == "-":
        return s[:10]
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%Y/%m/%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            continue
    return s[:10] if len(s) >= 10 and s[4:5] == "-" else ""


def temporal_block(
    event_date: Any,
    known_date: Any = None,
    scrape_date: str | None = None,
    *,
    estimated: bool = False,
) -> dict[str, Any]:
    """Construye el bloque temporal obligatorio de un registro normalizado.

    Args:
        event_date: cuando ocurrio el hecho real (transaccion, periodo 13F...).
        known_date: cuando fue publico (filing/disclosure). Si None, se asume
            que coincide con event_date (datos publicos al instante: Polymarket,
            noticias).
        scrape_date: ISO 8601 UTC de cuando lo capturamos. Si None, ahora.
        estimated: True si la known_date es una estimacion (datos viejos sin
            fecha de disclosure fiable). Anade known_date_estimated=true.

    Returns:
        dict con event_date, known_date, scrape_date, delay_days y
        opcionalmente known_date_estimated.

    Regla anti-lookahead: known_date NUNCA debe ser anterior a event_date. Si
    lo fuera (dato inconsistente), known_date se fuerza a event_date.
    """
    ev = _to_iso_date(event_date)
    kn = _to_iso_date(known_date) if known_date else ev
    if not kn:
        kn = ev
    # Forzar known_date >= event_date (no se puede conocer antes de que ocurra).
    if ev and kn and kn < ev:
        kn = ev
    delay = None
    if ev and kn:
        try:
            d_ev = datetime.strptime(ev, "%Y-%m-%d").date()
            d_kn = datetime.strptime(kn, "%Y-%m-%d").date()
            delay = (d_kn - d_ev).days
        except ValueError:
            delay = None
    block = {
        "event_date": ev,
        "known_date": kn,
        "scrape_date": scrape_date or datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "delay_days": delay,
    }
    if estimated:
        block["known_date_estimated"] = True
    return block


def validate_temporal(record: dict, name: str = "record") -> None:
    """Verifica que un registro tenga el bloque temporal y sea coherente.

    Lanza ValueError si faltan campos o si known_date < event_date (lookahead).
    """
    missing = TEMPORAL_FIELDS - set(record.keys())
    if missing:
        raise ValueError(f"[{name}] falta bloque temporal {sorted(missing)}: {record!r}")
    ev, kn = record.get("event_date"), record.get("known_date")
    if ev and kn and kn < ev:
        raise ValueError(f"[{name}] lookahead: known_date {kn} < event_date {ev}")


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
