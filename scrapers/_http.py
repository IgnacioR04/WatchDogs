"""HTTP utils compartidos: sesion con retries, User-Agent y rate limit suave."""

from __future__ import annotations

import os
import time
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Email para User-Agent de SEC (obligatorio). Cae a un default solo en local.
SEC_UA_EMAIL = os.environ.get("USER_AGENT_EMAIL", "ignaciusypunto2@gmail.com")

# User-Agents por fuente. SEC requiere uno especifico con email valido.
UA_SEC = f"Watchdog/1.0 ({SEC_UA_EMAIL})"
UA_DEFAULT = "Watchdog/1.0 (https://github.com/IgnacioR04/WatchDogs)"


def make_session(user_agent: str = UA_DEFAULT, total_retries: int = 5) -> requests.Session:
    """Crea una sesion con retries exponenciales y User-Agent fijo.

    Reintenta automaticamente en 429, 500, 502, 503, 504 con backoff.
    """
    s = requests.Session()
    s.headers.update({"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate"})
    retry = Retry(
        total=total_retries,
        backoff_factor=1.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["GET", "HEAD"]),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=10, pool_maxsize=10)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    return s


def get_json(session: requests.Session, url: str, *, params: dict | None = None,
             timeout: int = 30, sleep_after: float = 0.0) -> Any:
    """GET que devuelve JSON. Sleep opcional tras la llamada para rate limit suave."""
    r = session.get(url, params=params, timeout=timeout)
    r.raise_for_status()
    if sleep_after > 0:
        time.sleep(sleep_after)
    return r.json()
