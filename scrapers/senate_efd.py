"""Scraper del Senate eFD oficial (efdsearch.senate.gov).

ESTADO (2026-06-25): el portal eFD esta protegido por Akamai con deteccion de
bots por fingerprint TLS. Las peticiones con `requests` reciben 403 incluso
desde IP residencial y con headers de navegador. Vencerlo requiere un navegador
real (Playwright/Selenium), dependencia pesada que ademas no corre comodo en
GitHub Actions. Por tanto, la fuente viva de Senate queda PENDIENTE.

Este modulo implementa el flujo correcto (agreement + CSRF + report/data) para
estar listo si en el futuro se anade una capa de navegador o un proxy que pase
Akamai. Mientras tanto `run()` detecta el bloqueo y devuelve [] sin romper el
pipeline. El historico de Senate (2012-2020) vive en el mirror antiguo via
congress.py, marcado como stale por el health report.
"""

from __future__ import annotations

import re
from typing import Any

import requests

from scrapers._dates import delay_days, to_iso

SEARCH_URL = "https://efdsearch.senate.gov/search/"
HOME_URL = "https://efdsearch.senate.gov/search/home/"
DATA_URL = "https://efdsearch.senate.gov/search/report/data/"

BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)


def _new_session() -> requests.Session:
    """Sesion con headers de navegador (no basta para Akamai, pero es lo correcto)."""
    s = requests.Session()
    s.headers.update({
        "User-Agent": BROWSER_UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })
    return s


def _is_akamai_block(resp: requests.Response) -> bool:
    """Detecta la pagina de bloqueo de Akamai (403 corto / 'Access Denied')."""
    return resp.status_code == 403 or "Access Denied" in resp.text[:500]


def fetch_ptr_rows(start_date: str, max_rows: int = 100) -> list[dict[str, Any]]:
    """Intenta consultar PTRs del Senate eFD. Devuelve filas crudas o [] si bloqueado.

    start_date en formato MM/DD/YYYY. report_types=[11] son los PTR.
    """
    s = _new_session()
    r1 = s.get(SEARCH_URL, timeout=20)
    if _is_akamai_block(r1):
        print("[senate_efd] BLOQUEADO por Akamai en GET /search/ (403). Senate live no disponible.")
        return []
    m = re.search(r'name="csrfmiddlewaretoken"\s+value="([^"]+)"', r1.text)
    if not m:
        print("[senate_efd] sin CSRF token (pagina inesperada). Abortando.")
        return []
    csrf = m.group(1)
    s.headers["Referer"] = SEARCH_URL
    s.post(HOME_URL, data={"csrfmiddlewaretoken": csrf, "prohibition_agreement": "1"}, timeout=20)
    csrf2 = s.cookies.get("csrftoken", csrf)
    r3 = s.post(
        DATA_URL,
        headers={"X-CSRFToken": csrf2, "X-Requested-With": "XMLHttpRequest", "Referer": SEARCH_URL},
        data={
            "start": "0", "length": str(max_rows), "report_types": "[11]", "filer_types": "[]",
            "submitted_start_date": f"{start_date} 00:00:00", "submitted_end_date": "",
            "candidate_state": "", "senator_state": "", "office_id": "", "first_name": "", "last_name": "",
        },
        timeout=30,
    )
    if _is_akamai_block(r3):
        print("[senate_efd] BLOQUEADO por Akamai en POST /report/data/.")
        return []
    try:
        return r3.json().get("data", [])
    except ValueError:
        return []


def run() -> dict[str, Any]:
    """Punto de entrada. Devuelve dict con status y filas (vacio si bloqueado).

    No escribe fichero propio: la integracion real de Senate vendra cuando haya
    una via que pase Akamai. Por ahora informa del estado para el health report.
    """
    rows = fetch_ptr_rows(start_date="01/01/2026", max_rows=50)
    status = "ok" if rows else "blocked_akamai"
    print(f"[senate_efd] status={status} rows={len(rows)}")
    return {"status": status, "rows": rows}


if __name__ == "__main__":
    run()
