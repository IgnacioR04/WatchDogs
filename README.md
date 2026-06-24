# WATCHDOG

Sistema agregador de datos publicos de **trades de congresistas USA**, **insiders corporativos (SEC Forms 3/4/5)**, **holdings institucionales (13F)** y **traders top de Polymarket**.

Pipeline batch automatizado en GitHub Actions, persistido en el propio repo como JSON estatico, y servido via GitHub Pages para consumo desde un dashboard React standalone.

## Arquitectura

```
GitHub Actions (cron 6h batch / 15min Polymarket)
    |
    +-- scrapers/congress.py       --> house-stock-watcher + senate-stock-watcher
    +-- scrapers/sec_insider.py    --> SEC EDGAR Forms 3/4/5
    +-- scrapers/sec_13f.py        --> SEC EDGAR 13F filings
    +-- scrapers/polymarket.py     --> leaderboard + top traders + posiciones
    |
    +-- normalize/schema.py        --> schema unificado
    |
    +-- commit & push --> data/*.json
                              |
                        GitHub Pages sirve data/ como API estatica
                              |
                        dashboard/index.html (React via CDN, fetch puro)
```

## Estructura

```
watchdog/
|-- README.md
|-- requirements.txt
|-- .github/workflows/      (3 workflows: congress, sec, polymarket)
|-- scrapers/               (congress, sec_insider, sec_13f, polymarket)
|-- normalize/              (schema unificado y deduplicacion)
|-- data/                   (JSONs servidos por GitHub Pages)
|-- tests/                  (pytest)
+-- dashboard/              (SPA standalone React+CDN)
```

## Modelos de datos

Ver [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) para los schemas completos. Resumen:

- `data/congress_trades.json` — trades de House+Senate (PTRs)
- `data/insider_trades.json` — Forms 3/4/5 de SEC (ultimos 30 dias)
- `data/institutional_holdings.json` — 13F top 50 managers
- `data/polymarket_top_traders.json` — leaderboard PNL all-time + posiciones

## Ejecutar localmente

```bash
pip install -r requirements.txt

# Cada scraper se ejecuta como modulo y escribe en data/
python -m scrapers.congress
python -m scrapers.sec_insider
python -m scrapers.sec_13f
python -m scrapers.polymarket

# Tests
pytest
```

Variable de entorno (solo necesaria para SEC):
```
USER_AGENT_EMAIL=tu_email@ejemplo.com
```

## Dashboard

Abrir `dashboard/index.html` localmente, o publicar via GitHub Pages (rama `main`, carpeta raiz). El dashboard hace fetch puro a los JSONs de `data/` — **cero API calls**, cero coste por usuario.

URL en produccion: `https://IgnacioR04.github.io/WatchDogs/`

## Restricciones legales

- **House / Senate / OGE disclosures**: prohibido uso comercial salvo medios. Proyecto personal / research = OK.
- **SEC EDGAR**: uso libre. Respetar 10 req/s y User-Agent declarado.
- **Polymarket**: APIs publicas de lectura, sin restricciones documentadas.

## Roadmap (post v1)

- Alertas via GitHub Actions cuando un congresista compra >$1M
- Polymarket WebSocket para real-time (requiere worker externo fuera de Actions)
- Adaptadores Europa: CNMV (Espana), Companies House (UK), FCA, ESMA
- Estudio de correlacion: precio post-trade del congresista, alpha de insiders
