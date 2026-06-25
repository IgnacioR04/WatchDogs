"""Genera data/public/health_report.json: control de calidad por fuente.

El health report es la capa que evita errores silenciosos: detecta datos
viejos tratados como frescos, tickers contaminados, quarters 13F mezclados,
metricas falsas de Polymarket y fuentes bloqueadas.

Lee los JSONs ya generados en data/public/ (NO ejecuta scrapers) y produce un
informe con status por dataset y un overall_status agregado.

Uso:
    python -m pipelines.build_health_report
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from scrapers._dates import (
    expected_13f_quarter,
    now_utc,
    parse_date,
    quarter_end_date,
    within_last_days,
)

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
OUTPUT_PATH = PUBLIC_DIR / "health_report.json"

# Umbrales de los checks.
SENATE_STALE_DAYS = 45        # si el ultimo trade es mas viejo -> stale
INFLATED_WIN_RATE = 0.80      # win rate medio por encima -> sospechoso
INVALID_TICKER_SET = {"PDF", "N", "A", "THE", "INC", "LLC", "CORP"}

# Orden de severidad para agregar el overall.
SEVERITY = {"ok": 0, "warning": 1, "error": 2}


def _load(path: Path) -> Any:
    """Carga un JSON o devuelve None si no existe / falla."""
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _latest_date(records: list[dict], *keys: str) -> str | None:
    """Devuelve la fecha mas reciente encontrada en `keys` de los registros."""
    best = None
    for r in records:
        for k in keys:
            d = parse_date(r.get(k))
            if d and (best is None or d > best):
                best = d
    return best.date().isoformat() if best else None


def _count_30d(records: list[dict], *keys: str) -> int:
    """Cuenta registros cuya fecha (primera key valida) cae en los ultimos 30d."""
    n = 0
    for r in records:
        for k in keys:
            if r.get(k):
                if within_last_days(r.get(k), 30):
                    n += 1
                break
    return n


def check_congress() -> dict[str, Any]:
    """Health check del dataset de Congress."""
    data = _load(PUBLIC_DIR / "congress_trades_30d.json")
    if data is None:
        return {"status": "error", "issues": ["file_missing"], "blocked_for_signals": True}

    issues: list[str] = []
    latest_tx = _latest_date(data, "tx_date")
    latest_disc = _latest_date(data, "disclosure_date")
    records_30d = _count_30d(data, "tx_date", "disclosure_date")

    # Check 1: Senate viejo (fuente stale). El dato mas reciente es muy antiguo.
    blocked = False
    if latest_tx:
        age_days = (now_utc().date() - parse_date(latest_tx).date()).days
        if age_days > SENATE_STALE_DAYS:
            issues.append(f"stale_source_latest_tx_{age_days}d_old")
            blocked = True
    else:
        issues.append("no_valid_tx_dates")
        blocked = True

    # Check 2: ticker contaminado (ej "PDF").
    bad_tickers = sorted({r.get("ticker") for r in data
                          if (r.get("ticker") or "").upper() in INVALID_TICKER_SET})
    if bad_tickers:
        issues.append(f"invalid_tickers_present:{','.join(bad_tickers)}")

    # Check 3: muchos tickers de baja confianza (House sin parsear PDF).
    low_conf = sum(1 for r in data if (r.get("ticker_confidence") or 1.0) < 0.5
                   and r.get("ticker"))
    if low_conf > 0:
        issues.append(f"low_confidence_ticker_records:{low_conf}")

    status = "ok"
    if blocked:
        status = "error" if not records_30d else "warning"
    elif issues:
        status = "warning"

    return {
        "status": status,
        "records_total": len(data),
        "records_30d": records_30d,
        "latest_tx_date": latest_tx,
        "latest_disclosure_date": latest_disc,
        "issues": issues,
        "blocked_for_signals": blocked,
    }


def check_sec_insiders() -> dict[str, Any]:
    """Health check de SEC insiders (Forms 3/4/5)."""
    data = _load(PUBLIC_DIR / "sec_insiders_30d.json")
    if data is None:
        # Fichero ausente o vacio puede indicar SEC bloqueada (403) o sin run.
        return {"status": "error", "issues": ["file_missing_or_sec_blocked"],
                "blocked_for_signals": True}
    if not data:
        return {"status": "error", "issues": ["empty_dataset_possible_sec_block"],
                "records_30d": 0, "blocked_for_signals": True}

    issues: list[str] = []
    latest_tx = _latest_date(data, "tx_date")
    records_30d = _count_30d(data, "tx_date", "filing_date")

    # Check: frescura. Si el ultimo trade es muy viejo, algo falla.
    blocked = False
    if latest_tx:
        age = (now_utc().date() - parse_date(latest_tx).date()).days
        if age > SENATE_STALE_DAYS:
            issues.append(f"stale_latest_tx_{age}d")
    else:
        issues.append("no_valid_tx_dates")
        blocked = True

    status = "ok" if not issues else "warning"
    if blocked:
        status = "error"
    return {
        "status": status,
        "records_total": len(data),
        "records_30d": records_30d,
        "latest_tx_date": latest_tx,
        "insiders_unique": len({r.get("insider_name") for r in data if r.get("insider_name")}),
        "issues": issues,
        "blocked_for_signals": blocked,
    }


def check_institutional_13f() -> dict[str, Any]:
    """Health check de 13F usando los flags de consenso (is_stale/quarter)."""
    data = _load(PUBLIC_DIR / "institutional_holdings_latest.json")
    if data is None:
        return {"status": "error", "issues": ["file_missing"], "blocked_for_signals": True}

    # El scraper ya determina el quarter de consenso y marca is_stale por manager.
    quarters = [m.get("quarter") for m in data if m.get("quarter")]
    consensus_q = max(quarters) if quarters else "?"
    stale_managers = [m.get("manager", "?") for m in data if m.get("is_stale")]

    issues: list[str] = []
    if stale_managers:
        issues.append("stale_manager_report_date")

    # Solo es problema si MUCHOS managers estan atras (sino, 1-2 rezagados es normal).
    status = "ok"
    if data and len(stale_managers) / len(data) > 0.3:
        status = "warning"

    return {
        "status": status,
        "managers": len(data),
        "consensus_quarter": consensus_q,
        "stale_managers": stale_managers[:20],
        "stale_count": len(stale_managers),
        "issues": issues,
        "blocked_for_signals": False,
    }


def check_sec_13d_13g() -> dict[str, Any]:
    """Health check de 13D/13G (grandes accionistas)."""
    data = _load(PUBLIC_DIR / "sec_13d_13g_30d.json")
    if data is None:
        return {"status": "warning", "issues": ["file_missing"], "blocked_for_signals": False}
    issues: list[str] = []
    with_pct = sum(1 for r in data if r.get("ownership_pct") is not None)
    latest = _latest_date(data, "filing_date")
    if not data:
        issues.append("empty_dataset")
    return {
        "status": "ok" if data else "warning",
        "records_30d": len(data),
        "with_ownership_pct": with_pct,
        "latest_filing_date": latest,
        "issues": issues,
        "blocked_for_signals": False,
    }


def check_polymarket() -> dict[str, Any]:
    """Health check de Polymarket: volume=0, win rate inflado."""
    smart = _load(PUBLIC_DIR / "polymarket_smart_traders.json")
    whales = _load(PUBLIC_DIR / "polymarket_whales.json")
    if smart is None and whales is None:
        return {"status": "error", "issues": ["files_missing"], "blocked_for_signals": True}
    smart = smart or []
    whales = whales or []
    all_traders = smart + whales

    issues: list[str] = []

    # Check 1: volume = 0 en todos (campo mal mapeado).
    vol_zero = sum(1 for t in all_traders if not t.get("volume"))
    if all_traders and vol_zero == len(all_traders):
        issues.append("all_volume_zero")
    elif vol_zero > len(all_traders) * 0.7 if all_traders else False:
        issues.append(f"high_volume_zero_count:{vol_zero}")

    # Check 2: win rate inflado (señal de no paginar).
    win_rates = [t.get("win_rate", 0) for t in smart if t.get("closed_positions", 0) >= 10]
    avg_wr = round(sum(win_rates) / len(win_rates), 4) if win_rates else 0.0
    if avg_wr > INFLATED_WIN_RATE:
        issues.append(f"inflated_avg_win_rate:{avg_wr}")

    status = "ok" if not issues else "warning"
    return {
        "status": status,
        "smart_traders": len(smart),
        "whales": len(whales),
        "volume_zero_count": vol_zero,
        "avg_win_rate": avg_wr,
        "issues": issues,
        "blocked_for_signals": False,
    }


def build() -> dict[str, Any]:
    """Construye el informe completo con todos los checks."""
    datasets = {
        "congress": check_congress(),
        "sec_insiders": check_sec_insiders(),
        "sec_13d_13g": check_sec_13d_13g(),
        "institutional_13f": check_institutional_13f(),
        "polymarket": check_polymarket(),
    }
    # Overall = peor severidad entre los datasets.
    overall = "ok"
    for ds in datasets.values():
        if SEVERITY.get(ds["status"], 0) > SEVERITY[overall]:
            overall = ds["status"]
    return {
        "generated_at": now_utc().isoformat(),
        "overall_status": overall,
        "datasets": datasets,
    }


def run() -> Path:
    """Genera el informe y lo escribe en data/public/health_report.json."""
    report = build()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[health_report] overall={report['overall_status']} -> {OUTPUT_PATH}")
    for name, ds in report["datasets"].items():
        print(f"  {name}: {ds['status']}  issues={ds.get('issues')}")
    return OUTPUT_PATH


if __name__ == "__main__":
    run()
