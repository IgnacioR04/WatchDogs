"""Contexto de noticias via GDELT DOC API.

GDELT es una plataforma abierta y gratuita que monitoriza noticias globales y
se actualiza cada 15 minutos. Buscamos noticias de los tickers/empresas mas
relevantes de signals_30d.json para dar contexto de mercado al LLM.

Limite: 1 request cada 5 segundos (GDELT lo exige). Por eso limitamos el numero
de tickers consultados por run.

Salida: data/public/news_context_30d.json
"""

from __future__ import annotations

import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

from normalize.schema import temporal_block
from scrapers._http import UA_DEFAULT

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "data" / "public"
OUTPUT_PATH = PUBLIC_DIR / "news_context_30d.json"
GDELT_URL = "https://api.gdeltproject.org/api/v2/doc/doc"

MAX_TICKERS = 10          # cuantos tickers consultar (limite de rate de GDELT)
ARTICLES_PER_TICKER = 6
SLEEP_BETWEEN = 6.0       # GDELT exige >=5s entre requests (margen de seguridad)

# Temas detectables por palabras clave en titulares.
THEME_KEYWORDS = {
    "earnings": ["earnings", "revenue", "profit", "quarterly", "eps", "guidance"],
    "ai": ["ai", "artificial intelligence", "chip", "semiconductor", "gpu"],
    "merger": ["merger", "acquisition", "acquire", "buyout", "takeover", "deal"],
    "legal": ["lawsuit", "sued", "investigation", "probe", "settlement", "fraud"],
    "regulatory": ["fda", "sec", "antitrust", "regulator", "approval", "ban"],
    "leadership": ["ceo", "resign", "appoint", "executive", "board"],
    "stock": ["stock", "shares", "rally", "plunge", "surge", "downgrade", "upgrade"],
}


def _clean_company_query(name: str, ticker: str) -> str:
    """Construye la query GDELT a partir del nombre de empresa (o ticker)."""
    n = re.sub(r"\b(CORP|CORPORATION|INC|LLC|LTD|CO|PLC|GROUP|HOLDINGS|THE)\b", "", name or "", flags=re.I)
    n = re.sub(r"[^A-Za-z0-9 &]", " ", n).strip()
    n = " ".join(n.split()[:3])  # primeras palabras significativas
    if len(n) < 3:
        return f'"{ticker}"'
    return f'"{n}"'


def _detect_themes(title: str) -> list[str]:
    """Detecta temas en un titular por palabras clave."""
    t = (title or "").lower()
    return [theme for theme, kws in THEME_KEYWORDS.items() if any(k in t for k in kws)]


def _parse_seendate(s: str) -> str:
    """Convierte 'YYYYMMDDTHHMMSSZ' de GDELT a ISO 8601."""
    try:
        dt = datetime.strptime(s, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
        return dt.isoformat()
    except (ValueError, TypeError):
        return s or ""


def top_tickers_from_signals(limit: int = MAX_TICKERS) -> list[tuple[str, str]]:
    """Devuelve [(ticker, company)] de las senales mas importantes con ticker."""
    p = PUBLIC_DIR / "signals_30d.json"
    if not p.exists():
        return []
    signals = json.loads(p.read_text(encoding="utf-8"))
    # Agregamos importancia por ticker y guardamos un nombre de empresa.
    agg: dict[str, dict[str, Any]] = {}
    for s in signals:
        tk = s.get("ticker")
        if not tk or tk in {"NONE", "N", "A"}:
            continue
        e = agg.setdefault(tk, {"score": 0.0, "company": s.get("asset_name", "")})
        e["score"] += s.get("importance_score", 0)
        if not e["company"] and s.get("asset_name"):
            e["company"] = s["asset_name"]
    ranked = sorted(agg.items(), key=lambda kv: kv[1]["score"], reverse=True)
    return [(tk, e["company"]) for tk, e in ranked[:limit]]


def _gdelt_get(session: requests.Session, params: dict, retries: int = 2) -> dict:
    """GET a GDELT con paceo manual (>=6s) y reintento suave en 429.

    GDELT exige 1 request/5s GLOBALMENTE; un retry agresivo lo empeora, asi que
    espaciamos manualmente y reintentamos pocas veces.
    """
    for attempt in range(retries + 1):
        time.sleep(SLEEP_BETWEEN)
        try:
            r = session.get(GDELT_URL, params=params, timeout=30)
        except requests.RequestException:
            continue
        if r.status_code == 200:
            try:
                return r.json()
            except ValueError:
                return {}
        # 429 u otro: esperar mas y reintentar
        if r.status_code == 429:
            time.sleep(SLEEP_BETWEEN)
    return {}


def _is_relevant(title: str, ticker: str, company_query: str) -> bool:
    """True si el titular menciona realmente al ticker o a la empresa.

    GDELT hace matching laxo y devuelve articulos que no tienen nada que ver
    (ej. noticias genericas o en otros idiomas). Sin este filtro, el briefing
    etiqueta titulares con tickers equivocados.
    """
    t = (title or "").lower()
    needles = []
    name = company_query.strip('"').strip().lower()
    words = name.split()
    if len(name) >= 4:
        needles.append(name)
        # version corta del nombre: 1a palabra si es distintiva, o las 2 primeras
        # (evita falsos positivos con palabras genericas tipo 'super').
        if len(words) >= 2:
            needles.append(" ".join(words[:2]))
        elif words and len(words[0]) >= 5:
            needles.append(words[0])
    if len(ticker) >= 2:
        needles.append(ticker.lower())
    return any(n in t for n in needles)


def fetch_news_for(session: requests.Session, ticker: str, company: str) -> list[dict[str, Any]]:
    """Consulta GDELT para un ticker/empresa y devuelve articulos normalizados."""
    query = _clean_company_query(company, ticker)
    params = {"query": f"{query} sourcelang:eng", "mode": "ArtList", "format": "json",
              "maxrecords": str(ARTICLES_PER_TICKER), "timespan": "2w", "sort": "DateDesc"}
    data = _gdelt_get(session, params)
    out = []
    for a in data.get("articles", []):
        title = a.get("title", "")
        if not _is_relevant(title, ticker, query):
            continue
        published = _parse_seendate(a.get("seendate", ""))
        rec = {
            "id": "news_" + str(abs(hash(a.get("url", ""))) % (10 ** 12)),
            "source": "gdelt",
            "title": title,
            "url": a.get("url", ""),
            "published_at": published,
            "language": a.get("language", ""),
            "domain": a.get("domain", ""),
            "country": a.get("sourcecountry", ""),
            "tickers_detected": [ticker],
            "themes": _detect_themes(title),
        }
        # Noticia: el evento ES su publicacion (publico al instante). event=known.
        rec.update(temporal_block(published, published))
        out.append(rec)
    return out


def run() -> Path:
    """Descarga noticias de los top tickers y escribe news_context_30d.json."""
    session = requests.Session()  # sesion plana: SIN auto-retry (pelearia con GDELT)
    session.headers.update({"User-Agent": UA_DEFAULT})
    tickers = top_tickers_from_signals()
    if not tickers:
        print("[news_gdelt] sin signals_30d.json o sin tickers; nada que buscar")
        OUTPUT_PATH.write_text("[]", encoding="utf-8")
        return OUTPUT_PATH

    print(f"[news_gdelt] consultando {len(tickers)} tickers (~6s entre cada uno)")
    all_news: list[dict[str, Any]] = []
    seen_urls: set[str] = set()
    for ticker, company in tickers:
        arts = fetch_news_for(session, ticker, company)
        for a in arts:
            if a["url"] and a["url"] not in seen_urls:
                seen_urls.add(a["url"])
                all_news.append(a)

    all_news.sort(key=lambda a: a.get("published_at", ""), reverse=True)
    OUTPUT_PATH.write_text(json.dumps(all_news, indent=2, ensure_ascii=False),
                           encoding="utf-8")
    print(f"[news_gdelt] {len(all_news)} noticias de {len(tickers)} tickers -> {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == "__main__":
    run()
