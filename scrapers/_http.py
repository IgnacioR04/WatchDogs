"""HTTP utils compartidos: sesion con retries, User-Agent, rate limiter y logging.

Este modulo centraliza toda la comunicacion HTTP del proyecto para garantizar:
- User-Agent declarado (obligatorio para SEC EDGAR).
- Rate limiting configurable (max N requests por segundo) para respetar limites.
- Backoff exponencial automatico en 429/503/5xx.
- Logging basico de cada peticion.
"""

from __future__ import annotations

import logging
import os
import threading
import time
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# --- Configuracion de logging ---------------------------------------------
logging.basicConfig(
    level=os.environ.get("WATCHDOG_LOG_LEVEL", "INFO"),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger("watchdog.http")

# --- User-Agent ------------------------------------------------------------
# Email para el User-Agent de SEC (obligatorio). Cae a un default solo en local.
SEC_UA_EMAIL = os.environ.get("USER_AGENT_EMAIL", "ignaciusypunto2@gmail.com")

# SEC requiere un User-Agent especifico con email valido o devuelve 403.
UA_SEC = f"Watchdog/1.0 ({SEC_UA_EMAIL})"
UA_DEFAULT = "Watchdog/1.0 (+https://github.com/IgnacioR04/WatchDogs)"


class RateLimiter:
    """Limitador de tasa simple y thread-safe (token bucket basico).

    Garantiza un maximo de `max_per_sec` llamadas por segundo bloqueando
    el hilo el tiempo necesario entre peticiones. Es deliberadamente
    conservador: mide el intervalo minimo entre llamadas consecutivas.
    """

    def __init__(self, max_per_sec: float = 5.0):
        """max_per_sec: numero maximo de peticiones por segundo permitidas."""
        self.min_interval = 1.0 / max_per_sec if max_per_sec > 0 else 0.0
        self._last_call = 0.0
        self._lock = threading.Lock()

    def wait(self) -> None:
        """Bloquea hasta que sea seguro hacer la siguiente peticion."""
        if self.min_interval <= 0:
            return
        with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_call
            if elapsed < self.min_interval:
                time.sleep(self.min_interval - elapsed)
            self._last_call = time.monotonic()


class Client:
    """Cliente HTTP con sesion, rate limiting y helpers JSON.

    Uso:
        client = Client(user_agent=UA_SEC, max_per_sec=5)
        data = client.get_json(url, params={...})
    """

    def __init__(
        self,
        user_agent: str = UA_DEFAULT,
        max_per_sec: float = 5.0,
        total_retries: int = 5,
    ):
        """Crea el cliente con su sesion configurada y rate limiter."""
        self.session = make_session(user_agent=user_agent, total_retries=total_retries)
        self.limiter = RateLimiter(max_per_sec=max_per_sec)
        self.user_agent = user_agent

    def get(self, url: str, *, params: dict | None = None, timeout: int = 30) -> requests.Response:
        """GET con rate limiting y logging. Devuelve la Response cruda."""
        self.limiter.wait()
        log.debug("GET %s params=%s", url, params)
        r = self.session.get(url, params=params, timeout=timeout)
        if r.status_code >= 400:
            log.warning("GET %s -> %s", url, r.status_code)
        return r

    def get_json(self, url: str, *, params: dict | None = None, timeout: int = 30) -> Any:
        """GET que valida estado y devuelve JSON parseado."""
        r = self.get(url, params=params, timeout=timeout)
        r.raise_for_status()
        return r.json()


def make_session(user_agent: str = UA_DEFAULT, total_retries: int = 5) -> requests.Session:
    """Crea una sesion requests con retries exponenciales y User-Agent fijo.

    Reintenta automaticamente en 429, 500, 502, 503, 504 con backoff
    exponencial (backoff_factor=1.5).
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


def get_json(
    session: requests.Session,
    url: str,
    *,
    params: dict | None = None,
    timeout: int = 30,
    sleep_after: float = 0.0,
) -> Any:
    """GET que devuelve JSON (compat). Sleep opcional tras la llamada.

    Se mantiene por compatibilidad con los scrapers que ya usan `make_session`
    + `get_json`. Para codigo nuevo, preferir la clase `Client`.
    """
    r = session.get(url, params=params, timeout=timeout)
    r.raise_for_status()
    if sleep_after > 0:
        time.sleep(sleep_after)
    return r.json()
