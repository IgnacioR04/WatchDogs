"""Utilidades de fechas y quarters para WATCHDOG.

Todo en UTC y formato ISO (YYYY-MM-DD). Centraliza la logica de:
- Calculo del quarter actual y del quarter esperado para filings 13F.
- Ventanas rolling (ultimos N dias) para la capa publica de 30 dias.
- Conversiones y parsing tolerante de fechas de las distintas fuentes.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone


def now_utc() -> datetime:
    """Devuelve el datetime actual en UTC (timezone-aware)."""
    return datetime.now(timezone.utc)


def today_iso() -> str:
    """Fecha de hoy en formato ISO YYYY-MM-DD (UTC)."""
    return now_utc().date().isoformat()


def days_ago(n: int) -> datetime:
    """Devuelve el datetime de hace `n` dias (UTC, timezone-aware)."""
    return now_utc() - timedelta(days=n)


def days_ago_iso(n: int) -> str:
    """Fecha ISO de hace `n` dias."""
    return days_ago(n).date().isoformat()


def rolling_window(days: int = 30) -> tuple[str, str]:
    """Devuelve (from_iso, to_iso) de la ventana rolling de los ultimos `days` dias.

    Ejemplo: rolling_window(30) -> ('2026-05-25', '2026-06-24').
    """
    return days_ago_iso(days), today_iso()


def current_quarter(ref: datetime | None = None) -> str:
    """Devuelve el quarter natural actual en formato 'YYYYQX'.

    Ejemplo: una fecha en abril-junio 2026 -> '2026Q2'.
    """
    d = ref or now_utc()
    q = (d.month - 1) // 3 + 1
    return f"{d.year}Q{q}"


def quarter_end_date(quarter: str) -> str:
    """Devuelve la fecha de cierre (periodOfReport) de un quarter 'YYYYQX'.

    13F reporta el ultimo dia del trimestre: Q1=03-31, Q2=06-30, Q3=09-30, Q4=12-31.
    """
    year_s, q_s = quarter.upper().split("Q")
    year, q = int(year_s), int(q_s)
    ends = {1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)}
    month, day = ends[q]
    return f"{year:04d}-{month:02d}-{day:02d}"


def expected_13f_quarter(ref: datetime | None = None) -> str:
    """Devuelve el quarter 13F que ya deberia estar disponible publicamente.

    Los gestores 13F tienen 45 dias tras el cierre del trimestre para presentar.
    El quarter "esperado" (con la mayoria de filings ya presentados) es el mas
    reciente cuyo deadline (cierre del quarter + 45 dias) ya haya pasado.

    Ejemplo:
    - El 25-jun-2026: Q1 2026 cerro el 31-mar, deadline ~15-may -> ya paso.
      Q2 cierra el 30-jun (deadline ~14-ago) -> aun no. Esperado = '2026Q1'.
    """
    d = ref or now_utc()
    # Partimos del quarter actual y retrocedemos mientras su deadline no haya pasado.
    q = current_quarter(d)
    for _ in range(8):  # como mucho retrocedemos 2 anos por seguridad
        deadline = parse_date(quarter_end_date(q))
        if deadline and (deadline + timedelta(days=45)) <= d:
            return q
        q = _previous_quarter(q)
    return q


def _previous_quarter(quarter: str) -> str:
    """Devuelve el quarter anterior a 'YYYYQX'."""
    year_s, q_s = quarter.upper().split("Q")
    year, q = int(year_s), int(q_s)
    if q == 1:
        return f"{year - 1}Q4"
    return f"{year}Q{q - 1}"


def parse_date(value: str | None) -> datetime | None:
    """Parsea una fecha de fuentes heterogeneas a datetime UTC, o None.

    Acepta formatos comunes: ISO (YYYY-MM-DD), US (M/D/YYYY, MM/DD/YYYY),
    y timestamps ISO con hora. Devuelve None si no se reconoce.
    """
    if not value:
        return None
    s = str(value).strip()
    if not s:
        return None
    # ISO con hora (ej '2026-06-24T12:30:00Z')
    iso = s.replace("Z", "+00:00")
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%-m/%-d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    try:
        dt = datetime.fromisoformat(iso)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def to_iso(value: str | None) -> str:
    """Normaliza cualquier fecha reconocible a ISO YYYY-MM-DD, o '' si falla."""
    d = parse_date(value)
    return d.date().isoformat() if d else ""


def delay_days(event_date: str | None, disclosure_date: str | None) -> int | None:
    """Dias entre el evento (tx) y su divulgacion publica. None si falta dato.

    Mide el retraso legal de publicacion: clave para el freshness score.
    """
    ev = parse_date(event_date)
    dis = parse_date(disclosure_date)
    if not ev or not dis:
        return None
    return (dis.date() - ev.date()).days


def within_last_days(value: str | None, days: int = 30) -> bool:
    """True si la fecha `value` cae dentro de los ultimos `days` dias."""
    d = parse_date(value)
    if not d:
        return False
    return d >= days_ago(days)
