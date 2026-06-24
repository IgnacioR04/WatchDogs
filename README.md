# WATCHDOG

[![pages](https://img.shields.io/badge/site-live-3fb950?logo=github)](https://ignacior04.github.io/WatchDogs/)
[![data](https://img.shields.io/badge/api-data%2F*.json-58a6ff)](https://ignacior04.github.io/WatchDogs/data/congress_trades.json)

> **API estatica + dashboard para seguir el "smart money": congresistas USA, insiders corporativos, fondos institucionales y whales de Polymarket. Sin servidor propio, sin auth, sin coste.**

---

## Resumen ejecutivo

WATCHDOG agrega 4 fuentes publicas de informacion financiera, las normaliza al
mismo schema, y las publica como JSON estatico en GitHub Pages.

**Para que sirve:**
- **Investigacion / research personal**: ver que estan operando los politicos,
  insiders de empresas cotizadas, fondos top y traders top de Polymarket — todo
  en un solo sitio, con filtros y cross-reference por ticker.
- **Fuente de senales para bots**: cualquier sistema (paper trader, IA, modelo
  cuantitativo) puede hacer `fetch()` a las URLs publicas. La idea con
  [watchdog-trader](#roadmap) es alimentar una IA cada N horas con estos JSONs
  y dejar que decida una cartera paper.
- **Educacion**: ejemplo limpio de pipeline ETL serverless con cron en GitHub
  Actions, sin pagar nada.

**Lo que NO es:**
- No es una alerta en tiempo real (los disclosures llegan con dias/semanas de
  delay legal; los workflows refrescan cada 15 min - 6h segun fuente).
- No es uso comercial autorizado (ver [restricciones legales](#restricciones-legales)).
- No es asesoramiento financiero.

---

## Lo que esta vivo ahora mismo

| Recurso | URL |
|---|---|
| Dashboard | https://ignacior04.github.io/WatchDogs/ |
| API Congress | https://ignacior04.github.io/WatchDogs/data/congress_trades.json |
| API Insiders SEC | https://ignacior04.github.io/WatchDogs/data/insider_trades.json |
| API 13F | https://ignacior04.github.io/WatchDogs/data/institutional_holdings.json |
| API Polymarket | https://ignacior04.github.io/WatchDogs/data/polymarket_top_traders.json |

Volumetria actual (snapshot inicial):

| Dataset | Records | Tamano |
|---|---|---|
| congress_trades | ~8.300 | 3.5 MB |
| insider_trades  | ~500 (rolling 30d) | 200 KB |
| institutional_holdings | ~39 managers, ~100 holdings c/u | 600 KB |
| polymarket_top_traders | ~45 traders | 50 KB |

---

## Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│  GitHub Actions (cron en la nube, gratis para repos publicos) │
│                                                             │
│   scrape_polymarket   ──► cada 15 min                       │
│   scrape_congress     ──► cada 6h                           │
│   scrape_sec          ──► cada 6h                           │
└────────────────────────┬────────────────────────────────────┘
                         │ (cada workflow ejecuta los scrapers Python)
                         ▼
                ┌───────────────────┐
                │  scrapers/*.py    │  ──► descargan de:
                │                   │       House Clerk ZIP
                │  congress.py      │       Senate stock watcher (github)
                │  sec_insider.py   │       SEC EDGAR
                │  sec_13f.py       │       data.sec.gov
                │  polymarket.py    │       data-api.polymarket.com
                └─────────┬─────────┘
                          │
                          ▼ (genera JSON, hace git commit + git push)
                ┌───────────────────┐
                │  data/*.json      │  ←── ESTA ES TU API
                │  en el repo       │
                └─────────┬─────────┘
                          │ (GitHub Pages sirve el repo entero)
                          ▼
        https://ignacior04.github.io/WatchDogs/data/*.json
                          │
                          ▼
                ┌───────────────────┐
                │ dashboard React   │  fetch() puro, sin backend
                │ (mismo repo)      │
                └───────────────────┘
```

**Tres claves del diseno:**

1. **API = archivos JSON en el repo.** GitHub Pages los sirve como hosting
   estatico. No hay servidor, no hay base de datos, no hay rate-limit que tu
   pagues. Coste fijo = $0.
2. **Workflows escriben al repo.** Cada cron hace pull, regenera el JSON, hace
   commit y push. Hay un `concurrency: watchdog-write-data` global que
   serializa los 3 workflows para que nunca se pisen al pushear.
3. **Dashboard 100% frontend.** React via CDN + Babel standalone. Cero build,
   cero deps Node. Lee los JSONs y los muestra. Cualquiera puede forkearlo y
   tener su propio dashboard al instante.

---

## Workflows (CI cron)

| Workflow | Cron | Cadencia | Scripts ejecutados | Output(s) |
|---|---|---|---|---|
| [`scrape_polymarket`](.github/workflows/scrape_polymarket.yml) | `*/15 * * * *` | cada 15 min | `scrapers/polymarket.py` | `data/polymarket_top_traders.json` |
| [`scrape_congress`](.github/workflows/scrape_congress.yml) | `0 */6 * * *` | cada 6h | `scrapers/congress.py` | `data/congress_trades.json` |
| [`scrape_sec`](.github/workflows/scrape_sec.yml) | `0 */6 * * *` | cada 6h | `scrapers/sec_insider.py` + `scrapers/sec_13f.py` | `data/insider_trades.json`, `data/institutional_holdings.json` |

Los 3 son tambien lanzables manualmente desde **Actions > Run workflow**.

Cada workflow:
1. Hace checkout del repo (con `fetch-depth: 0` para que el rebase tenga ancestros).
2. Instala Python 3.11 + `requirements.txt` con cache de pip.
3. Ejecuta el(los) scraper(s) Python correspondientes — escriben en `data/`.
4. **`git pull --rebase origin main`** para integrar cualquier commit del bot
   que haya entrado mientras corria.
5. `stefanzweifel/git-auto-commit-action@v5` con `--force-with-lease` para
   commitear y pushear solo si el archivo cambio.

**Por que cadencias diferentes:** Polymarket es mercado en vivo, cambia rapido.
House/Senate disclosures llegan con 30-45 dias de retraso por ley — pedir mas
de cada 6h no aporta nada. SEC Forms 4 tienen 2 dias de delay regulatorio. 13F
es trimestral (90 dias).

---

## Scrapers — funcionamiento detallado

Todos comparten utilidades en [`scrapers/_http.py`](scrapers/_http.py) (sesion
requests con retry exponencial en 429/5xx, User-Agent declarado) y
[`normalize/schema.py`](normalize/schema.py) (IDs estables, dedup, validacion,
escritura JSON).

### 1. Congress — [`scrapers/congress.py`](scrapers/congress.py)

Trades de **House of Representatives + Senate**, basados en los PTRs (Periodic
Transaction Reports) que los legisladores deben presentar.

| Camara | Fuente | Que se extrae |
|---|---|---|
| **Senate** | [github.com/timothycarambat/senate-stock-watcher-data](https://github.com/timothycarambat/senate-stock-watcher-data) `aggregate/all_transactions.json` | Datos completos: senador, ticker, asset_description, tipo (Purchase/Sale), amount range, fechas, link al PTR oficial. |
| **House** | [disclosures-clerk.house.gov](https://disclosures-clerk.house.gov/) `public_disc/financial-pdfs/{year}FD.ZIP` (ZIP oficial del Clerk de la Camara) | Solo metadata del filing: representante, fecha de disclosure, DocID y link al PDF. **No incluye ticker/monto porque eso vive en cada PDF**, que habria que OCR-ear. |

**Por que distintas fuentes:** los buckets S3 originales (`house-stock-watcher-data`,
`senate-stock-watcher-data`) que solia usar la comunidad llevan caidos
desde 2025 con HTTP 403. El mirror github del Senate sigue actualizandose; el
House nadie lo mantiene. Asi que para House recurrimos al ZIP oficial.

**Output:** [`data/congress_trades.json`](data/congress_trades.json) — array de
objetos:
```json
{
  "id": "abc123ef",
  "politician": "Nancy Pelosi",
  "chamber": "house|senate",
  "party": "D|R|I",
  "ticker": "NVDA",
  "asset_name": "NVIDIA Corp",
  "tx_type": "purchase|sale|exchange|ptr|other",
  "amount_range": "$1,000,001 - $5,000,000",
  "tx_date": "2026-06-15",
  "disclosure_date": "2026-06-20",
  "source_url": "https://disclosures-clerk.house.gov/..."
}
```

**Dedup:** hash sha1 de `(politician, ticker, tx_date, amount, tx_type)`.

### 2. SEC Insiders — [`scrapers/sec_insider.py`](scrapers/sec_insider.py)

**Forms 3/4/5** de SEC EDGAR — compras y ventas de insiders corporativos
(CEOs, directores, +10%-owners).

**Fuente:** `efts.sec.gov/LATEST/search-index` filtrando `forms=4` y rango
custom de los ultimos 30 dias. Para cada hit baja el XML estructurado del
filing desde `www.sec.gov/Archives/edgar/data/{cik}/{accession}/{doc}.xml`
y lo parsea con `xml.etree.ElementTree`.

**Que se extrae:** issuer (ticker, nombre), insider (nombre, titulos:
Director / Officer / 10%-Owner / officerTitle), y por cada
`nonDerivativeTransaction`: fecha, codigo de transaccion (P/S/A/M/...), shares
y precio por share.

Los codigos crudos se mapean a etiquetas legibles:
```
P-Purchase, S-Sale, A-Grant, M-OptionExercise, D-Disposition, F-PaymentByShares...
```

**Caps operativos:**
- Ventana: 30 dias por defecto.
- Max filings parseados por ejecucion: 400 (la API EDGAR pagina de 100 en 100).
- Rate limit suave: ~5 req/s (sleep 0.2s entre filings) — por debajo del limite
  oficial de 10 req/s con User-Agent declarado.

**Output:** [`data/insider_trades.json`](data/insider_trades.json) — un
registro por transaccion individual (un filing puede tener varias):
```json
{
  "id": "0001209191-26-079821-0",
  "insider_name": "HUANG JEN-HSUN",
  "insider_title": "Director, President and CEO",
  "company": "NVIDIA CORP",
  "ticker": "NVDA",
  "tx_type": "S-Sale",
  "shares": 120000,
  "price_per_share": 130.50,
  "tx_date": "2026-06-18",
  "source_url": "https://www.sec.gov/Archives/edgar/data/.../"
}
```

### 3. SEC 13F — [`scrapers/sec_13f.py`](scrapers/sec_13f.py)

**Holdings institucionales** (>$100M en AUM) — Form 13F-HR, presentado
trimestralmente.

**Fuente:** lista hardcodeada de ~50 managers top con su CIK (Berkshire,
BlackRock, Vanguard, Citadel, Renaissance, Tiger Global, Pershing Square,
Bridgewater, Soros, ARK, etc.).

**Por cada CIK:**
1. `GET data.sec.gov/submissions/CIK{cik10}.json` → busca el ultimo filing
   `13F-HR` en `filings.recent`.
2. `GET /Archives/edgar/data/{cik}/{accession}/index.json` → localiza el
   `informationTable` XML del filing.
3. Parsea el XML extrayendo todas las `infoTable` con: `nameOfIssuer`, `cusip`,
   `value` (USD), `shrsOrPrnAmt/sshPrnamt` (shares).
4. Ordena por valor desc, queda con top 100 holdings.

**Limitacion:** el `informationTable` no incluye ticker, solo CUSIP y nombre.
El dashboard puede buscar por nombre. Resolucion CUSIP→ticker requiere data
externa que no incluimos.

**Output:** [`data/institutional_holdings.json`](data/institutional_holdings.json):
```json
{
  "manager": "Berkshire Hathaway Inc",
  "cik": "0001067983",
  "report_date": "2026-03-31",
  "aum_usd": 271234000000,
  "holdings": [
    {"asset_name": "APPLE INC", "cusip": "037833100", "ticker": "", "shares": 905560000, "value_usd": 158472000000},
    ...
  ],
  "source_url": "https://www.sec.gov/Archives/edgar/data/.../"
}
```

### 4. Polymarket — [`scrapers/polymarket.py`](scrapers/polymarket.py)

**Top traders del mercado de prediccion** ordenados por PnL all-time.

**Fuentes:**
1. `GET data-api.polymarket.com/v1/leaderboard?period=ALL&sortBy=PNL&limit=100`
   → top 100 traders (en practica devuelve 50 — cap del endpoint).
2. Por cada wallet del top 100:
   `GET data-api.polymarket.com/v1/closed-positions?user={wallet}&limit=200`
   → posiciones cerradas (max 200 por trader).
3. Calcula `win_rate = posiciones con realizedPnl>0 / total cerradas`.
4. Top 5 posiciones por size absoluto se incluyen en el output.

**Filtro:** solo traders con `>= 10` posiciones cerradas (descarta noise).

**Rate limit:** sleep 0.1s entre traders → ~10 req/s. El limite documentado
es 150 req/10s para positions, asi que tenemos margen 1.5x.

**Output:** [`data/polymarket_top_traders.json`](data/polymarket_top_traders.json):
```json
{
  "wallet": "0xabc...",
  "username": "whale_politics",
  "category": "ALL",
  "pnl": 542000,
  "volume": 2100000,
  "markets_traded": 87,
  "win_rate_positions": 0.91,
  "top_positions": [
    {"market": "Will X win 2026 election?", "position": "Yes", "size": 45000, "realized_pnl": 12000}
  ]
}
```

---

## Modelo de datos unificado

Centralizado en [`normalize/schema.py`](normalize/schema.py). Cada scraper
escribe un array de objetos siguiendo el schema canonico de su dataset:

- `CONGRESS_REQUIRED` = `{id, politician, chamber, party, ticker, asset_name, tx_type, amount_range, tx_date, disclosure_date, source_url}`
- `INSIDER_REQUIRED` = `{id, insider_name, insider_title, company, ticker, tx_type, shares, price_per_share, tx_date, source_url}`
- `INSTITUTIONAL_REQUIRED` = `{manager, cik, report_date, holdings, source_url}`
- `POLYMARKET_REQUIRED` = `{wallet, username, category, pnl, volume, markets_traded, win_rate_positions, top_positions}`

Helpers compartidos:
- `stable_id(*parts)` — SHA1 truncado de 16 chars sobre los args. Determinista,
  sirve como ID para dedup cuando la fuente no expone uno propio.
- `dedupe_by_key(records, key='id')` — primera ocurrencia gana.
- `validate_records(records, required, name)` — lanza ValueError si falta
  campo requerido. Se usa en cada `run()`.
- `write_json(path, data)` — UTF-8, indent 2, crea directorios padre.

---

## Estructura del repo

```
watchdog/
├── README.md
├── PROJECT_CONTEXT.md          # spec original (no editado por workflows)
├── requirements.txt            # requests, pandas, pytest
├── run_all.py                  # corre los 4 scrapers en serie (uso local)
├── index.html                  # redirect raiz → dashboard/
├── .nojekyll                   # evita procesamiento Jekyll de Pages
├── .github/workflows/
│   ├── scrape_congress.yml     # cron 0 */6 * * *
│   ├── scrape_sec.yml          # cron 0 */6 * * *  (insider + 13F)
│   └── scrape_polymarket.yml   # cron */15 * * * *
├── scrapers/
│   ├── _http.py                # session + retry + User-Agent helpers
│   ├── congress.py
│   ├── sec_insider.py
│   ├── sec_13f.py
│   └── polymarket.py
├── normalize/
│   └── schema.py               # validacion, dedup, IDs estables
├── data/                       # ★ OUTPUT — esta es la API estatica
│   ├── congress_trades.json
│   ├── insider_trades.json
│   ├── institutional_holdings.json
│   └── polymarket_top_traders.json
├── tests/                      # 12 tests pytest (unit + integration)
│   ├── test_congress.py
│   ├── test_sec.py
│   └── test_polymarket.py
└── dashboard/
    ├── index.html              # SPA React + CDN, auto-detect URL base
    └── artifact.html           # variante con URL absoluta para Claude.ai artifacts
```

---

## Ejecutar localmente

```bash
pip install -r requirements.txt

# Los 4 scrapers en serie
python run_all.py

# O cada uno por separado
python -m scrapers.congress
python -m scrapers.sec_insider
python -m scrapers.sec_13f
python -m scrapers.polymarket

# Tests
pytest

# Dashboard local
python -m http.server 8766
# Abrir http://localhost:8766/dashboard/index.html
```

Variable de entorno (obligatoria solo para los scrapers SEC):

```
USER_AGENT_EMAIL=tu_email@ejemplo.com
```

SEC EDGAR exige User-Agent con email valido o rechaza con 403.

---

## Configuracion para fork / clone (primera vez)

1. **Fork o clone** del repo.
2. **GitHub > Settings > Secrets and variables > Actions > New repository secret**
   - Name: `USER_AGENT_EMAIL`
   - Value: tu email
3. **GitHub > Settings > Pages**
   - Source: `Deploy from a branch`
   - Branch: `main` / `(root)`
   - Save
4. **Actions > Run workflow** en cada workflow la primera vez para tener
   datos frescos (luego ya corren solos por cron).

---

## Dashboard

`dashboard/index.html` es una **SPA standalone**: React 18 + Babel standalone
vienen de CDN (unpkg), todo el codigo de la app esta en un solo `<script
type="text/babel">`. Hace `fetch()` puro a los 4 JSONs y los muestra.

**5 tabs:**
- **Congress** — tabla ordenable, filtros por partido / ticker / politico,
  ranking de tickers mas comprados.
- **Insiders** — tabla con filtros por ticker / insider / direccion (buy/sell).
  Verde para compras (P/M), rojo para ventas (S/D).
- **Institucionales** — top managers desplegables con sus holdings; buscador
  por nombre de empresa para ver "quien la tiene".
- **Polymarket** — ranking por PnL, click en trader expande top posiciones.
- **Cross-ref** — input un ticker → muestra simultaneamente: congresistas que
  lo operaron, insiders activos, fondos que lo tienen.

**Diseno:** oscuro, tipografia monospace (tabular numbers), responsive,
sin dependencias propias mas alla del HTML.

**Para Claude.ai artifacts:** usar [`dashboard/artifact.html`](dashboard/artifact.html)
(tiene URL hardcodeada a `https://ignacior04.github.io/WatchDogs/data/`).

---

## Restricciones legales

- **House / Senate / OGE disclosures**: prohibido **uso comercial** salvo
  medios de comunicacion. Uso personal / investigacion / educativo = OK.
  El ZIP del Clerk y los datos del Senate son publicos por ley pero su uso
  esta regulado por el [Ethics in Government Act](https://www.govinfo.gov/app/details/USCODE-2010-title5/USCODE-2010-title5-app-ethicsing).
- **SEC EDGAR**: uso libre. Respetar el limite de 10 req/s y declarar User-Agent
  con email funcional. Ver [SEC Fair Access policy](https://www.sec.gov/os/accessing-edgar-data).
- **Polymarket**: APIs publicas de lectura sin restricciones documentadas.
  No abusar (los limites son generosos: 1000 req/10s general, 150 req/10s en
  positions).
- **General**: no es asesoramiento financiero. No intentar deducir carteras
  privadas de clientes de brokers (ilegal e imposible con datos publicos).

---

## Roadmap

### v1 (esto, ya hecho)
- [x] 4 scrapers + tests + workflows con cron
- [x] API estatica via Pages
- [x] Dashboard SPA con 5 tabs y cross-reference
- [x] Concurrency global resuelto (no race en pushes paralelos)

### v2 — alertas
- [ ] Workflow que, tras cada refresh, detecta trades > $1M de congresistas y
      manda notificacion (Discord webhook / email / Telegram bot).
- [ ] Diff incremental: en lugar de regenerar el JSON entero, solo agregar
      los nuevos registros y mantener historia compacta.

### v3 — alpha research
- [ ] Calculo de **alpha post-trade**: para cada compra de congresista /
      insider, comparar retorno del ticker en 1d / 7d / 30d / 90d contra SPY.
      Ranking de "quien tiene mejor track record" historicamente.
- [ ] Crossref con earnings calendar: que insiders venden justo antes /
      compran justo despues de earnings.

### v4 — paper trader con IA  →  **otro repo: `watchdog-trader`**

```
                         ┌──────────────────────────────┐
                         │  WATCHDOG (esto que tienes)  │
                         │  data/*.json en GitHub Pages │
                         └────────────┬─────────────────┘
                                      │ fetch JSON
                                      ▼
        ┌───────────────────────────────────────────────────┐
        │  Otro repo nuevo: watchdog-trader                 │
        │                                                   │
        │  GitHub Action cron cada 4h:                      │
        │   1. fetch los 4 JSONs de WatchDogs               │
        │   2. construir prompt con "top trades 24h"        │
        │   3. POST a Claude API con context + cartera      │
        │   4. parsear decision (buy/sell/hold + sizing)    │
        │   5. ejecutar en paper trading                    │
        │   6. log en results.json                          │
        └───────────────────────────────────────────────────┘
```

Reutiliza el chassis de tu repo existente `LLM_Trader` (mismo patron: cron +
fetch + prompt + paper trading + log). Cambio principal: en vez de fetch de
features de BTC, fetch de los JSONs de WATCHDOG.

### v5 — Europa
- [ ] Adaptadores: CNMV (Espana), Companies House (UK), FCA, ESMA.
- [ ] Schema unificado entre USA y Europa.

---

## Notas tecnicas

- **Python 3.11+** en local. En CI usamos `3.11` explicitamente
  (Python 3.14 todavia no tiene wheels para pandas / numpy en pypi → falla en
  CI con compilacion lenta o errores de gcc).
- Sin TypeScript, sin bundlers, sin Node. El dashboard usa Babel standalone
  para JSX y React via CDN — esto es **intencional** para que cualquiera pueda
  forkear y abrir `index.html` sin instalar nada.
- El repo tiene autores divididos: humanos para los commits de codigo,
  `watchdog-bot <actions@github.com>` para los commits automaticos de
  refresh de data. Filtrable con `git log --author=watchdog-bot`.
- Race condition solucionada con `concurrency: watchdog-write-data` global en
  los 3 workflows + `git pull --rebase` + `push_options: --force-with-lease`.
  Detalle en commit [`5f21222`](https://github.com/IgnacioR04/WatchDogs/commit/5f21222).
