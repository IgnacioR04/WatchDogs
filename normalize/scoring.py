"""Sistema de scoring de senales de WATCHDOG.

Calcula un `importance_score` (0-100) para cada senal unificada, combinando
seis sub-scores con los pesos del informe de arquitectura:

    importance_score =
        actor_score          * 0.25
      + amount_score         * 0.25
      + source_quality_score * 0.20
      + freshness_score      * 0.15
      + rarity_score         * 0.10
      + cross_source_score   * 0.05

Cada sub-score esta normalizado a 0-100. Las tablas (actor, source quality,
freshness) son constantes derivadas del informe.
"""

from __future__ import annotations

import math
from typing import Any

from scrapers._dates import delay_days

# --- Pesos del importance score -------------------------------------------
WEIGHTS = {
    "actor": 0.25,
    "amount": 0.25,
    "source_quality": 0.20,
    "freshness": 0.15,
    "rarity": 0.10,
    "cross_source": 0.05,
}

# --- Tabla de actor_score --------------------------------------------------
# Cuanto mas relevante/informado el actor, mayor el score base.
ACTOR_SCORE = {
    "ceo": 95,
    "cfo": 90,
    "ten_percent_owner": 85,
    "10%_owner": 85,
    "senator": 85,
    "house_rep_top_committee": 80,
    "house_rep": 75,
    "director": 75,
    "officer": 78,
    "top_institutional_manager": 90,
    "institutional_manager": 80,
    "large_holder": 82,           # 13D/13G
    "polymarket_elite": 75,
    "polymarket_whale": 70,
    "insider": 70,                # insider generico sin cargo claro
    "unknown": 50,
}

# --- Tabla de source_quality_score ----------------------------------------
# Fiabilidad/estructuracion de la fuente.
SOURCE_QUALITY_SCORE = {
    "sec_form_4": 98,
    "sec_form_3": 95,
    "sec_form_5": 95,
    "corporate_insider": 98,
    "sec_13f": 95,
    "institutional": 95,
    "sec_13d": 95,
    "sec_13g": 95,
    "large_holder": 95,
    "senate_efd": 88,
    "house_pdf_parsed": 85,
    "house_pdf_metadata": 55,
    "congress": 80,               # fallback generico congress
    "polymarket": 82,
    "polymarket_data_api": 82,
    "gdelt": 70,
    "news": 70,
    "unknown": 50,
}

# --- Tabla de freshness_score (por delay de divulgacion en dias) ----------
def freshness_score(delay: int | None) -> float:
    """Score de frescura segun el retraso (dias) entre evento y divulgacion.

    0-1d=100, 2-7d=90, 8-30d=70, 31-45d=55, >45d=25. Si no hay delay, 60 neutro.
    """
    if delay is None:
        return 60.0
    if delay <= 1:
        return 100.0
    if delay <= 7:
        return 90.0
    if delay <= 30:
        return 70.0
    if delay <= 45:
        return 55.0
    return 25.0


def amount_score(amount_usd: float | None) -> float:
    """Score por tamano economico de la operacion (escala logaritmica 0-100).

    Mapea $10k -> ~20, $100k -> ~40, $1M -> ~60, $10M -> ~80, $100M+ -> ~100.
    Operaciones sin importe conocido reciben 40 (neutro-bajo).
    """
    if not amount_usd or amount_usd <= 0:
        return 40.0
    # log10($) : 4 (10k) .. 8+ (100M). Escalamos linealmente a 20..100.
    decades = math.log10(amount_usd)  # 4 para 10k, 8 para 100M
    score = (decades - 4) * 20 + 20    # 10k->20, 100M->100
    return float(max(0.0, min(100.0, score)))


def actor_score(actor_type: str | None) -> float:
    """Devuelve el score base de un tipo de actor (default 50)."""
    if not actor_type:
        return ACTOR_SCORE["unknown"]
    return float(ACTOR_SCORE.get(str(actor_type).lower(), ACTOR_SCORE["unknown"]))


def source_quality_score(source: str | None, source_type: str | None = None) -> float:
    """Score de calidad de fuente. Prueba `source` y luego `source_type`."""
    for key in (source, source_type):
        if key and str(key).lower() in SOURCE_QUALITY_SCORE:
            return float(SOURCE_QUALITY_SCORE[str(key).lower()])
    return float(SOURCE_QUALITY_SCORE["unknown"])


def rarity_score(signal: dict[str, Any]) -> float:
    """Score de rareza: penaliza eventos rutinarios, premia los inusuales.

    Heuristica v1:
    - Compras de insider en mercado abierto (tx_code P) son raras y valiosas: 90.
    - Ventas programadas/grants/pagos de impuestos (S/A/F/M) son rutinarias: 30-50.
    - Resto: 60 neutro.
    """
    tx_code = (signal.get("tx_code") or "").upper()
    if tx_code == "P":
        return 90.0
    if tx_code in {"A", "F"}:   # grant, pago impuestos
        return 30.0
    if tx_code in {"M", "S", "D"}:
        return 50.0
    return 60.0


def normalize_cross_source(raw: float | None) -> float:
    """Normaliza el cross_source_score (suele venir 0-1) a escala 0-100."""
    if raw is None:
        return 0.0
    v = float(raw)
    # Si viene en 0-1, escalamos. Si ya viene 0-100, lo dejamos.
    return v * 100.0 if v <= 1.0 else min(v, 100.0)


def score_signal(signal: dict[str, Any]) -> dict[str, Any]:
    """Anade los sub-scores y el importance_score a una senal (in-place).

    Espera un dict con (algunos opcionales):
      actor_type, source, source_type, amount_estimated/value_usd,
      event_date, disclosure_date, tx_code, cross_source_score.

    Devuelve el mismo dict enriquecido con:
      actor_score, amount_score, source_quality_score, freshness_score,
      rarity_score, cross_source_score (normalizado), importance_score.
    """
    a_score = actor_score(signal.get("actor_type"))
    amt = signal.get("amount_estimated")
    if amt is None:
        amt = signal.get("value_usd")
    amt_score = amount_score(amt)
    sq_score = source_quality_score(signal.get("source"), signal.get("source_type"))
    delay = signal.get("delay_days")
    if delay is None:
        delay = delay_days(signal.get("event_date"), signal.get("disclosure_date"))
    fresh = freshness_score(delay)
    rare = rarity_score(signal)
    cross = normalize_cross_source(signal.get("cross_source_score"))

    importance = (
        a_score * WEIGHTS["actor"]
        + amt_score * WEIGHTS["amount"]
        + sq_score * WEIGHTS["source_quality"]
        + fresh * WEIGHTS["freshness"]
        + rare * WEIGHTS["rarity"]
        + cross * WEIGHTS["cross_source"]
    )

    signal["actor_score"] = round(a_score, 1)
    signal["amount_score"] = round(amt_score, 1)
    signal["source_quality_score"] = round(sq_score, 1)
    signal["freshness_score"] = round(fresh, 1)
    signal["rarity_score"] = round(rare, 1)
    signal["cross_source_score"] = round(cross, 1)
    signal["delay_days"] = delay
    signal["importance_score"] = round(importance, 1)
    return signal
