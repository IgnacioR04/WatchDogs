# WATCHDOG current state — P0 baseline

This is an evidence-based description of the repository at `main` commit `287e4d8` on 2026-08-09. It describes what exists, not the target V4 architecture.

## What WATCHDOG is today

WATCHDOG is a Python batch ETL and intelligence pipeline. It fetches public-source data, normalizes and scores it, derives market/risk artifacts, writes versioned static files under `data/public/`, and serves those files plus a browser-only dashboard through GitHub Pages. It has no database, HTTP query service, canonical Person entity, entity-resolution service or migration framework.

```text
external sources
  -> source-specific scrapers
  -> normalized static snapshots
  -> signals/news/movements/LLM context
  -> market + macro -> regime -> portfolio -> risk
  -> data/public/*
  -> GitHub Pages dashboard and LLM/manual consumers
```

The current public “API” is static content served by GitHub Pages. It is not a person-query API and normal requests cannot resolve names or query historical records.

## Real entry points and pipeline

### Scraper orchestrator

[`run_all.py`](../../run_all.py) accepts `all`, `sec`, `congress` or `polymarket` and invokes:

1. `congress_house_pdf_parser.run`;
2. `sec_insider.run`;
3. `sec_13f.run`;
4. `sec_13d_13g.run`;
5. `polymarket_leaderboard.run`.

It catches exceptions per scraper and returns a non-zero status if any fail. [`run_pipeline.py`](../../run_pipeline.py) calls `run_all.main("all")` without checking that return value, so a scraper group failure can be reported as a successful `scrapers` step at that orchestration layer.

### Local full orchestrator

[`run_pipeline.py`](../../run_pipeline.py) has 13 best-effort steps in dependency order:

1. scrapers;
2. publish 30-day/static contracts;
3. unified signals;
4. GDELT news;
5. top movements;
6. legacy LLM context;
7. health report;
8. market prices;
9. FRED macro;
10. regime;
11. portfolio proposal;
12. risk report;
13. daily context.

Each step failure is logged and the pipeline continues using existing artifacts. The CLI supports `--from`, `--only` and `--profile`.

### Production hourly workflow

[`.github/workflows/scrape_hourly.yml`](../../.github/workflows/scrape_hourly.yml) runs at minute 17 hourly, on manual dispatch, and on non-`data/**` pushes to `main`. It:

1. checks out full history and installs Python 3.11 dependencies;
2. runs `run_all.py` for the requested group;
3. publishes 30-day/static artifacts;
4. builds signals, GDELT news, movements, LLM context and health;
5. runs market, macro, regime, portfolio, risk, paper metrics, daily context and trader-prompt steps as `continue-on-error` where configured;
6. rebases from `main` with errors tolerated;
7. commits `data/public/*.json` and `data/public/*.md` as `watchdog-bot` using message `data: hourly refresh [skip ci]` and `--force-with-lease`.

A global `watchdog-write-data` concurrency group serializes writers. `WATCHDOG_HISTORY_DIR` points to an ephemeral `_ci_history` directory, so deep history created during an Actions run is lost at runner teardown. `llm_response.txt` is versioned but is outside the workflow's commit pattern.

The workflow has 16 data/intelligence build invocations rather than the 13 steps in `run_pipeline.py`: it additionally runs paper metrics and trader-prompt generation and invokes risk through the module CLI.

## Repository components

| Area | Current responsibility |
|---|---|
| `scrapers/` | SEC, Congress/House PDFs, Senate mirror/eFD prototype, Polymarket, GDELT, market prices, FRED, HTTP/Drive/EDGAR utilities |
| `normalize/` | shared schema, temporal fields, stable IDs/dedup and scoring |
| `pipelines/` | public publication, signals, context, health, movements, historical backfill/indexes, paper metrics and LLM validation/prompting |
| `portfolio/` | constraint profiles, allocation and optimization |
| `risk/` | historical risk engine and Monte Carlo |
| `regime/` | price/macro market-state classification |
| `dashboard/` and root `index.html` | static browser UI that fetches published artifacts directly |
| `tests/` | 26 test modules, 135 collected cases: 134 deterministic and one `live` |
| `data/public/` | 25 generated/versioned public artifacts |
| `data/*.json` | four legacy public snapshot contracts |

## Public and generated outputs

There are 25 files under `data/public/`: 22 JSON files, two Markdown files and one text file. Four additional legacy JSON snapshots remain under `data/`. Exact shape and consumer details are in [PUBLIC_CONTRACT.md](PUBLIC_CONTRACT.md).

The publisher treats event datasets as a rolling 30-day window and snapshot/derived datasets as complete snapshots for that artifact. The static contract does not include deep historical partitions.

## External sources and dependencies

| Source/service | Use | Current limitation |
|---|---|---|
| SEC EDGAR/EFTS | Form 4, 13D/13G, 13F and bulk/index backfill | request caps and per-run parsing limits; requires declared User-Agent |
| House Clerk | PTR index and PDFs | recent-window/filing cap; scanned/no-text PDFs yield no persisted filing record |
| Senate mirror | historical Senate transactions | non-official mirror; official eFD is blocked by Akamai and marked unavailable |
| Polymarket Data API | leaderboard and closed positions | leaderboard and per-wallet pagination caps |
| GDELT | ticker-related news context | queries only a bounded signal-derived ticker universe |
| Yahoo Finance (`yfinance`) | market-price history/snapshot | network/provider instability; best-effort in CI |
| FRED | macro history/snapshot | requires `FRED_API_KEY`; best-effort in CI |
| Google Drive API | intended history sync | service accounts cannot upload to the personal Drive design; OAuth integration postponed |

[`requirements.txt`](../../requirements.txt) currently declares `requests`, `pandas`, `pytest`, Google auth/API clients, `pypdf`, `yfinance`, `pyarrow` and `numpy` with minimum versions. It does not yet include FastAPI, SQLAlchemy, psycopg, Alembic, `pydantic-settings` or a PostgreSQL test stack.

## Coverage limits and partial datasets

Coverage-affecting limits are not consistently represented as `partial` metadata:

| Area | Current bound/behavior |
|---|---|
| Form 4 | 30-day window; at most 400 filings per run |
| 13D/13G live | at most 250 documents; EFTS pagination stops around offset 1000 |
| 13D/13G backfill | at most 800 documents per quarter and the quarter is checkpointed as complete |
| 13F | hardcoded curated manager map; current and previous filing only; top 100 holdings per filing; at most 50 managers emitted; 500 changes emitted |
| House PTR | 45 recent days and at most 200 filings; no-text/scanned PDFs counted in logs but not persisted |
| Senate | official live source blocked; mirror provides historical context and has known stale/coverage limits |
| Polymarket | requests top 100 leaderboard entries; scans at most 1,000 closed positions per trader; keeps top five positions |
| GDELT | at most 10 signal-derived tickers queried |
| Market prices | at most 80 signal-derived tickers plus configured market symbols |
| Derived views | top movements 40; multiple LLM/dashboard lists are intentionally top-N presentation summaries |

Presentation caps are reasonable for static exports, but they cannot be treated as complete canonical history in V4.

## Historical data

Deep history lives outside the repository under `WATCHDOG_HISTORY_DIR`, whose personal-machine fallback is `G:/Mi unidad/WATCHDOG_HISTORY`.

```text
WATCHDOG_HISTORY/
  normalized/<source>/year=YYYY/quarter=QX/<source>.jsonl.gz
  indexes/checkpoint.json
  indexes/dataset_index.json
  indexes/ticker_index.json
  indexes/actor_index.json
  prices/symbol=<symbol>/timeframe=1d/year=YYYY/*.parquet
  macro/series=<series_id>/*.jsonl.gz
```

[`pipelines/backfill.py`](../../pipelines/backfill.py) supports `sec_insiders`, `sec_13d_13g` and `congress`; [`pipelines/build_indexes.py`](../../pipelines/build_indexes.py) builds coverage, ticker and actor-string indexes. The actor index maps strings to files and is not entity resolution. Historical files and indexes are neither versioned here nor exposed through the static public contract, and no P0 run had access to the owner's local historical directory to reconcile counts.

## Configuration and secret findings

No credential value was found committed in the reviewed configuration paths, but personal fallbacks and fragmented settings exist:

| Setting | Current behavior |
|---|---|
| `USER_AGENT_EMAIL` | environment override; otherwise personal Gmail address hardcoded in `scrapers/_http.py` |
| `FRED_API_KEY` | environment; `run_pipeline.py` also reads `C:/Users/ignac/watchdog-secrets/fred_api_key.txt` |
| `WATCHDOG_HISTORY_DIR` | environment; otherwise `G:/Mi unidad/WATCHDOG_HISTORY` in several modules |
| `WATCHDOG_LOG_LEVEL` | scraper logging level |
| `GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON_B64` | optional Drive service-account credentials |
| `GOOGLE_DRIVE_SA_FILE` | optional local credentials path |
| `GOOGLE_DRIVE_ROOT_FOLDER_ID` | target Drive folder |

There is no central settings object. V4 P1 must make environment-specific configuration explicit and remove personal email/path production defaults without placing secret values in docs or code.

## Documentation drift

[`README.md`](../../README.md) and [`PROJECT_CONTEXT.md`](../../PROJECT_CONTEXT.md) describe an earlier four-dataset/multiple-workflow architecture. The repository now has one hourly workflow, House PDF parsing, 13D/13G, a history/backfill layer, 22 public JSON artifacts, signals, market/macro, regime, portfolio, risk, paper trading and LLM briefing outputs. Some README links point to workflow/module names that no longer exist. These documents remain user-facing legacy documentation and are intentionally outside issue #2's owned files; updating them belongs to a coordinated later documentation package.

## History and authorship evidence

The inspected branch contains 521 commits. Recent history is dominated by `data: hourly refresh [skip ci]` commits. Git author metadata attributes 519 commits to IgnacioR04 across two email identities, one to Ignacio and one to Codex; many feature commits contain `Co-Authored-By` trailers for Claude/Claude variants. GitHub Actions configures `watchdog-bot`, but resulting commits may appear under the repository owner's authenticated identity. Therefore authorship must be assessed from author metadata, subjects, trailers, workflow configuration and diffs together—not from a single field.

Relevant history shows the full orchestrator introduced in `82da3ed`, the earlier LLM/run-all documentation in `3532050`, the expanded README in `913e140`, and the P0 live-test isolation in `bde4303` merged by `287e4d8`. Existing Claude-authored/co-authored code and bot snapshots are treated as evidence, not as disposable output.
