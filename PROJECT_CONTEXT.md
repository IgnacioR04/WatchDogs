# WATCHDOG - Congress, Insider & Polymarket Tracker

## Que es
Sistema de agregacion de datos publicos de trades de congresistas USA, insiders corporativos (SEC), holdings institucionales (13F) y traders top de Polymarket. Pipeline batch automatizado con GitHub Actions, persistido en el propio repo como JSON estatico, y servido via GitHub Pages para consumo desde un dashboard (Claude artifact o web).

## Por que es viable
- **SEC EDGAR**: API REST publica, sin auth, 10 req/s. Datasets estructurados de Forms 3/4/5 (insiders) y 13F (institucionales) en JSON/XML.
- **House disclosures**: Portal publico con PTRs descargables. Existe `house-stock-watcher` (GitHub) que ya scrapea y expone JSON.
- **Senate eFD**: Portal publico con PTRs. Existe `senate-stock-watcher` (GitHub) que hace lo mismo.
- **Polymarket**: Gamma API + Data API + CLOB 100% publicos, sin auth para lectura. Leaderboard por categoria, trades, posiciones, top holders. Rate limits generosos (1000 req/10s general).

## Arquitectura

```
GitHub Actions (cron cada 6h batch / 15min Polymarket)
    |
    +-- scraper_congress.py    -> house-stock-watcher JSON + senate-stock-watcher JSON
    +-- scraper_sec.py         -> EDGAR 13F datasets + Forms 3/4/5 insider datasets
    +-- scraper_polymarket.py  -> leaderboard + top traders + closed positions + top holders
    |
    +-- normalize.py           -> schema unificado -> JSON estaticos
    |
    +-- commit & push -> /data/*.json en el repo
                          |
                    GitHub Pages sirve /data/ como API estatica
                          |
                    Dashboard (Claude artifact / React SPA)
                      fetch() a https://<user>.github.io/watchdog/data/*.json
                      0 tokens extra - es solo frontend
```

## Modelo de datos

### congress_trades.json
```json
[{
  "id": "hash",
  "politician": "Nancy Pelosi",
  "chamber": "house",
  "party": "D",
  "ticker": "NVDA",
  "asset_name": "NVIDIA Corp",
  "tx_type": "purchase",
  "amount_range": "$1,000,001 - $5,000,000",
  "tx_date": "2026-06-15",
  "disclosure_date": "2026-06-20",
  "source_url": "https://..."
}]
```

### insider_trades.json (SEC Forms 3/4/5)
```json
[{
  "id": "accession_number",
  "insider_name": "Jensen Huang",
  "insider_title": "CEO",
  "company": "NVIDIA Corp",
  "ticker": "NVDA",
  "tx_type": "S-Sale",
  "shares": 120000,
  "price_per_share": 130.50,
  "tx_date": "2026-06-18",
  "source_url": "https://www.sec.gov/..."
}]
```

### institutional_holdings.json (13F)
```json
[{
  "manager": "Berkshire Hathaway",
  "cik": "0001067983",
  "report_date": "2026-03-31",
  "holdings": [
    {"ticker": "AAPL", "shares": 905560000, "value_usd": 158472000000},
    {"ticker": "BAC", "shares": 1032852000, "value_usd": 41314000000}
  ],
  "source_url": "https://www.sec.gov/..."
}]
```

### polymarket_top_traders.json
```json
[{
  "wallet": "0xabc...",
  "username": "whale_politics",
  "category": "POLITICS",
  "pnl": 542000,
  "volume": 2100000,
  "markets_traded": 87,
  "win_rate_positions": 0.91,
  "top_positions": [
    {"market": "Will X win 2026 election?", "position": "Yes", "size": 45000}
  ]
}]
```

## Restricciones legales
- Disclosures de House/Senate/OGE: **prohibido uso comercial** salvo medios de comunicacion. Proyecto personal/research = OK.
- SEC EDGAR: uso libre, respetar 10 req/s y User-Agent declarado.
- Polymarket: APIs publicas de lectura sin restricciones documentadas.
- **No** intentar obtener carteras privadas de clientes de brokers (ilegal/imposible).

## Stack tecnico
- Python 3.11+ (requests, pandas, json)
- GitHub Actions (cron workflows)
- GitHub Pages (static hosting)
- React artifact (dashboard) - fetch puro a GitHub Pages, sin backend

## Fuentes de datos

| Fuente | URL / Endpoint | Auth | Formato |
|--------|---------------|------|---------|
| House trades | house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json | No | JSON |
| Senate trades | senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.json | No | JSON |
| SEC 13F filings | data.sec.gov / efts.sec.gov | No | JSON/XML |
| SEC insider (3/4/5) | efts.sec.gov/LATEST/search-index forms=4 | No | JSON |
| Polymarket leaderboard | data-api.polymarket.com/v1/leaderboard | No | JSON |
| Polymarket positions | data-api.polymarket.com/v1/closed-positions | No | JSON |
