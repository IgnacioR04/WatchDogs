# P0 test baseline

Baseline source: `main` commit `287e4d8`, verified 2026-08-09 on Linux/Python 3.12 using the previously provisioned project virtual environment.

## Baseline before the P0 fix

The original default collection contained 135 tests: 134 deterministic cases plus `tests/test_congress.py::test_run_genera_json_con_minimos`. That case performed a live network call during ordinary pytest execution and called the Congress scraper with its tracked output path. P0 QA observed it overwrite `data/public/congress_trades_30d.json`; the incidental snapshot change was restored before any V4 commit.

This meant “default pytest” was not a trustworthy deterministic/non-mutating gate even when the live source happened to respond. Issue [#1](https://github.com/IgnacioR04/WatchDogs/issues/1) classified it as a P0 baseline blocker.

## Fix and post-fix baseline

PR [#3](https://github.com/IgnacioR04/WatchDogs/pull/3), implementation `bde4303`, merged as `287e4d8`:

- registered the `live` marker;
- made default pytest exclude `live` tests;
- moved the connectivity probe inside the explicitly selected live test;
- redirected its output to `tmp_path`;
- documented opt-in commands.

Independent PR evidence recorded:

| Check | Result |
|---|---|
| Default suite with outbound socket APIs blocked | `134 passed, 1 deselected` and zero network attempts |
| Targeted Congress default tests offline | `2 passed, 1 deselected` |
| Live collect-only | exactly one Congress live test selected |
| Live marker offline | one skipped; tracked output unchanged |
| Tracked Congress snapshot SHA-256 | `8db0cc9477c67050f93c96c2c4d6ab60cf71954ade4138382dfe4188a5d9dec3` before/after PR verification |
| Diff hygiene | `git diff --check` passed; no generated-data change |

P0 documentation-branch verification reproduced:

```text
134 passed, 1 deselected in 2.16s
```

The external live integration was not exercised during offline verification. That is intentional: live-provider availability is not a normal PR gate.

## Suite classification

| Class | Current command/status |
|---|---|
| Deterministic default | `pytest` or `python -m pytest`; 134 pass |
| Live integration | `pytest -m live`; one Congress case, explicitly opt-in |
| Secret-dependent | No default tests require real secrets; FRED behavior uses monkeypatched values |
| Filesystem-history-dependent | History/index/market/risk tests use temporary fixtures; no default test requires the owner's real `WATCHDOG_HISTORY` |
| External database | None; PostgreSQL does not exist yet |

## Coverage by test module

The 26 modules cover SEC 13D/13G and 13F timing, Congress/House parsing, temporal schema, dedup/scoring, Drive mocks, history indexes, health, market/macro, news, Polymarket, public publishing, signals/LLM context, portfolio/liquidity, paper metrics, regime, risk and LLM-output validation.

Current gaps relevant to V4 include no PostgreSQL migration/repository tests, no API tests, no canonical identity-resolution tests, no full source-document provenance model, no concurrency/idempotent database tests, and no contract test spanning all 29 static artifact paths.

## Commands for P0 gate

```bash
python -m pytest -q
python -m pytest -m live --collect-only -q
git diff --check
git status --short
```

A P0 documentation PR must leave all `data/`, production code, workflow and tests unchanged. Live execution should only be attempted explicitly and remains subject to upstream availability.
