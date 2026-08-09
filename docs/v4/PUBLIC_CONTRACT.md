# Current public contract

Baseline: `main` at `287e4d8`, 2026-08-09. GitHub Pages serves repository files at `https://ignacior04.github.io/WatchDogs/<path>`. These static files are compatibility contracts; they are not a query API and must remain available until an explicit, tested deprecation.

## Contract rules in current code

- `data/public/` contains 25 versioned artifacts: 22 JSON, two Markdown and one text file.
- `data/` contains four legacy JSON contracts.
- [`pipelines/publish_public_30d.py`](../../pipelines/publish_public_30d.py) filters four event datasets to 30 days and treats seven other configured datasets as snapshots; it emits `manifest_public.json` and `latest.json`.
- Other stages write additional artifacts not enumerated by the publisher manifest.
- The hourly bot commits only `data/public/*.json` and `data/public/*.md`; `llm_response.txt` is not in that pattern.
- JSON arrays have no response envelope or pagination. Dates are strings, usually ISO-like, and schema enforcement is producer/test-specific rather than a single formal JSON Schema catalog.
- The root dashboard and both `dashboard/*.html` variants fetch static artifacts directly.

## `data/public/` inventory

The “shape” column records current top-level keys (and representative array item keys) from the baseline snapshot. Counts are volatile and are not contract guarantees.

| Artifact | Shape at baseline | Primary producer / in-repository consumers |
|---|---|---|
| `congress_trades_30d.json` | array (257); item includes `id`, `politician`, `actor_name/type`, `chamber`, `ticker`, `asset_name`, `tx_type`, amounts, event/known/scrape/disclosure dates, scores, source/provenance | House/Senate scraper + publisher; dashboard, signals, health |
| `sec_insiders_30d.json` | array (776); item includes `id`, insider/company/ticker, transaction code/type, shares/price/value, transaction/filing/event/known/scrape dates, `source_url` | Form 4 scraper + publisher; dashboard, signals, health |
| `sec_13d_13g_30d.json` | array (250); item includes filer/issuer CIK/name, filing type, ownership/shares, ticker/company, dates, scores, `source_url` | 13D/13G scraper + publisher; dashboard, signals, health, LLM context |
| `institutional_holdings_latest.json` | array (37); manager, CIK, report/filing/quarter dates, AUM, nested `holdings`, temporal/stale flags, source | 13F scraper + publisher; dashboard, health |
| `institutional_changes_latest.json` | array (500); manager, ticker/asset/CUSIP, previous/current/delta values, percent, direction, quarter | 13F scraper + publisher; dashboard, signals, LLM context |
| `polymarket_smart_traders.json` | array (46); wallet/profile, PnL/volume, closed/win/loss counts, scores, categories and nested top positions, temporal/source fields | Polymarket scraper + publisher; dashboard, health, LLM/daily context |
| `polymarket_whales.json` | array (50); same profile family as smart traders | Polymarket scraper + publisher; dashboard, health, LLM context |
| `news_context_30d.json` | array (12); id, title/url/domain, publish/event/known/scrape dates, tickers, themes, language/country/source | GDELT + publisher; dashboard, movements, LLM/daily context |
| `signals_30d.json` | array (1,783); normalized actor/security/event/direction/amount/date/source plus importance/signal/confidence/cross-source scores and risk flags | signals builder + publisher; dashboard, movements, LLM, market-universe, portfolio, validation |
| `top_movements_30d.json` | object: `count`, `generated_at`, `movements`, `window`, `window_days` | movements builder + publisher; dashboard, LLM/daily context |
| `llm_context_30d.json` | object: project/window/time, signal count, top tickers, insider/congress/institutional/holder/Polymarket/news/movement summaries, market/data quality and instructions | LLM context builder + publisher; dashboard/manual LLM consumer |
| `manifest_public.json` | object: `project`, `generated_at`, `public_window_days`, `window`, `datasets` | publisher; dashboards |
| `latest.json` | object: `generated_at`, `overall_status`, dataset count map | publisher; dashboards and several pipeline modules |
| `health_report.json` | object: `generated_at`, `overall_status`, `datasets` | health builder; dashboards, daily/LLM context and pipeline guards |
| `market_prices_latest.json` | array (110); `symbol`, `date`, `close`, 1/5/20-day returns | market scraper; daily context |
| `macro_latest.json` | array (14); FRED series/name/group/date/value/1-month change | macro scraper; regime, daily context |
| `regime.json` | object: `generated_at`, `risk_state`, `recommended_risk_budget`, `states`, `reasons`, `context`, `summary` | regime engine; dashboard, portfolio, risk, validation, daily context |
| `portfolio_proposal.json` | object: profile/time, core/satellite/cash/weights, rationale, metrics, regime budget and risk gate | allocator; dashboard, risk, validation, daily context, local orchestrator |
| `risk_report.json` | object: `generated_at`, `portfolio`, `regime_budget`, `metrics`, `limits`, `monte_carlo`, `gate` | risk engine; dashboard |
| `llm_portfolio.json` | object: approval/verdict/confidence/thesis, final weights, adjustments, risks, metrics, gate and violations | LLM-output validator; trader-prompt builder |
| `paper_ledger.json` | array (14); approval time, verdict/confidence/thesis, weights and adjustment count | LLM-output validator; paper metrics |
| `paper_trading.json` | object: budget/cost model, cycles/count, positions, equity curve, metrics and generation time | paper metrics; dashboard |
| `daily_context.md` | Markdown briefing assembled from signals, health, market, macro, regime, portfolio, risk, paper and news artifacts | daily-context builder; dashboard/manual LLM, trader-prompt and validator |
| `trader_prompt.md` | Markdown prompt containing current context, prior approved allocation and trading instructions | trader-prompt builder; manual LLM consumer |
| `llm_response.txt` | free-form external LLM response input | consumed and validated by `pipelines.validate_llm_output`; not generated by hourly workflow |

Nested structures such as 13F `holdings`, Polymarket `top_positions`, movement lists, equity curves and manifest dataset entries are part of actual consumer expectations even though no central schema file currently formalizes them.

## Legacy `data/*.json` inventory

| Artifact | Baseline shape | Current status |
|---|---|---|
| `congress_trades.json` | array (8,307); `id`, politician/chamber/party, ticker/asset, type/range, transaction/disclosure dates, source URL | advertised in README; older `scrapers.congress` code can write it; not the current `run_all` output |
| `insider_trades.json` | array (472); insider/title/company/ticker, type, shares/price, transaction date, source URL | advertised in README; legacy snapshot, while current Form 4 output is in `data/public/` |
| `institutional_holdings.json` | array (39); manager/CIK/report date/AUM, nested holdings and source URL | advertised legacy snapshot; no current production writer reference outside documentation |
| `polymarket_top_traders.json` | array (41); wallet/user/category, PnL/volume/markets/win rate and nested positions | advertised legacy snapshot; no current production writer reference outside documentation |

Legacy URLs are public and may have unknown external consumers even when no current in-repository code reads them. Absence of an internal reference is not permission to delete them.

## Consumer groups

| Consumer | Contracts relied on |
|---|---|
| Root/dashboard HTML | core event datasets, institutional/Polymarket, signals, movements, LLM context, health/manifest/latest, regime/portfolio/risk, paper trading and daily context |
| Signal/intelligence pipeline | Congress, insiders, 13D/13G, 13F changes, news and existing signals |
| LLM/manual workflow | `llm_context_30d.json`, `daily_context.md`, `trader_prompt.md`, `llm_response.txt`, portfolio and ledger artifacts |
| Market/portfolio/risk | signals -> market universe; history + regime -> portfolio; portfolio + history -> risk |
| GitHub Pages/external clients | any repository path; only internal consumers are statically searchable, so external dependency is unknown |

## Migration requirements

1. PostgreSQL will become source of truth for the V4 API, but these paths remain compatibility exports until explicit deprecation.
2. Preserve filenames and required shapes during additive migration; protect them with contract/snapshot tests.
3. Mark preview/partial/top-N semantics instead of presenting bounded exports as complete history.
4. Do not redirect consumers to API endpoints until the database/API path is proven and rollback is available.
5. Do not conflate prediction markets *about* a person, campaign finance *related to* a person, and holdings/trades *by* a person.
