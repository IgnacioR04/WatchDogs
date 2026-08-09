# WATCHDOG V4 status

Last verified: 2026-08-09 against `main` commit `c90b4d2` (`c90b4d2ff9ac8e89606391835b60f6e71785ae0e`), after P0 incident recovery, workflow hardening and a successful manual hourly smoke run.

## Executive status

| Field | State |
|---|---|
| Current phase | P1.1 — Architecture Decision Records — **IN PROGRESS** ([#6](https://github.com/IgnacioR04/WatchDogs/issues/6)) |
| Phase gate | P0 **PASS**; P1 is not yet eligible for evaluation |
| Migration progress | **0%** — no PostgreSQL, entity-resolution, repository or API migration has started |
| Production behavior | Current static pipeline remains authoritative; hardened hourly writer is active and its manual smoke run succeeded |
| Known regressions | None introduced by V4 work |
| Blocking defects | None known after P0 document recovery and hourly-writer hardening |
| Default test baseline | `137 passed, 1 deselected` |
| Explicit live coverage | 1 Congress test, excluded unless `-m live` is requested |

## Work packages

| Item | Status | Evidence |
|---|---|---|
| Issue [#1](https://github.com/IgnacioR04/WatchDogs/issues/1), isolate live/mutating pytest coverage | Closed | PR [#3](https://github.com/IgnacioR04/WatchDogs/pull/3) merged as `287e4d8`; implementation commit `bde4303` |
| Issue [#2](https://github.com/IgnacioR04/WatchDogs/issues/2), P0 repository baseline | Closed | PR [#30](https://github.com/IgnacioR04/WatchDogs/pull/30) merged as `91bda83`; final release and post-merge evidence [PASS](https://github.com/IgnacioR04/WatchDogs/pull/30#issuecomment-5231721967) |
| Issue [#33](https://github.com/IgnacioR04/WatchDogs/issues/33), restore the P0 baseline after hourly history rewrite | Closed | PR [#35](https://github.com/IgnacioR04/WatchDogs/pull/35) merged as `3cf491c`; the six accepted P0 documents were restored without replacing the newer data snapshot |
| Issue [#34](https://github.com/IgnacioR04/WatchDogs/issues/34), make the hourly writer fail closed | Closed | PR [#36](https://github.com/IgnacioR04/WatchDogs/pull/36) merged as `0a8b894`; active/manual post-hardening [smoke run 31317548954](https://github.com/IgnacioR04/WatchDogs/actions/runs/31317548954) succeeded with a normal fast-forward data push |
| Issue [#6](https://github.com/IgnacioR04/WatchDogs/issues/6), P1.1 Architecture Decision Records | In progress | Architecture overview and ten ADRs proposed on `v4/p1-architecture-adrs`; independent approval still required |

## Open roadmap issues

Snapshot of open issues on 2026-08-09. Dependencies are gate-level summaries of each issue body; later status updates must refresh this table rather than treating it as live GitHub state.

| Issue | Title | Phase | Dependency |
|---|---|---|---|
| [#4](https://github.com/IgnacioR04/WatchDogs/issues/4) | Central typed settings and environment contract | P1.3 | P1.1 and P1.2 (#6, #7) |
| [#5](https://github.com/IgnacioR04/WatchDogs/issues/5) | Database package, initial migrations and lifecycle tests | P1.4–P1.6 | P1.1–P1.3 (#4, #6, #7) |
| [#6](https://github.com/IgnacioR04/WatchDogs/issues/6) | Architecture Decision Records | P1.1 | Issue #2 merged |
| [#7](https://github.com/IgnacioR04/WatchDogs/issues/7) | Add and constrain V4 runtime dependencies | P1.2 | P1.1 ADRs approved (#6) |
| [#8](https://github.com/IgnacioR04/WatchDogs/issues/8) | Ambiguity-safe person entity resolution | P3 | P2 gate green (#10) |
| [#9](https://github.com/IgnacioR04/WatchDogs/issues/9) | Persist SEC 13D/13G through the V4 connector contract | P4.B | P3 gate green (#8) |
| [#10](https://github.com/IgnacioR04/WatchDogs/issues/10) | Domain services, repositories, DTOs and idempotent upserts | P2 | P1 gate green (#4–#7) |
| [#11](https://github.com/IgnacioR04/WatchDogs/issues/11) | Persist SEC Forms 3/4/5 through the V4 connector contract | P4.A | P3 gate green (#8) |
| [#12](https://github.com/IgnacioR04/WatchDogs/issues/12) | Redesign and persist SEC 13F ingestion | P4.C | P3 gate green (#8) |
| [#13](https://github.com/IgnacioR04/WatchDogs/issues/13) | Persist House PTR filings including unparseable PDFs | P4.D | P3 gate green (#8) |
| [#14](https://github.com/IgnacioR04/WatchDogs/issues/14) | Model Polymarket traders separately from markets about people | P4.F | P3 gate green (#8) |
| [#15](https://github.com/IgnacioR04/WatchDogs/issues/15) | Persist Senate disclosure data with provenance limits | P4.E | P3 gate green (#8) |
| [#16](https://github.com/IgnacioR04/WatchDogs/issues/16) | Person-aware GDELT ingestion | P4.G | P3 gate green (#8) |
| [#17](https://github.com/IgnacioR04/WatchDogs/issues/17) | Congress.gov identity connector | P5.B | P3 gate green (#8) |
| [#18](https://github.com/IgnacioR04/WatchDogs/issues/18) | FEC/OpenFEC candidate and campaign-finance connector | P5.C | P3 gate green (#8) |
| [#19](https://github.com/IgnacioR04/WatchDogs/issues/19) | Wikidata identity connector | P5.A | P3 gate green (#8) |
| [#20](https://github.com/IgnacioR04/WatchDogs/issues/20) | OGE public financial disclosure connector | P5.D | P3 gate green (#8) |
| [#21](https://github.com/IgnacioR04/WatchDogs/issues/21) | Versioned FastAPI query and protected admin layer | P6 | P5 gate green (#17–#20) |
| [#22](https://github.com/IgnacioR04/WatchDogs/issues/22) | Incremental dashboard person search and compatibility gate | P8.3–P8.4 | P6 and P8.1 stable (#21, #24) |
| [#23](https://github.com/IgnacioR04/WatchDogs/issues/23) | Migrate intelligence reads to repository/query interfaces | P8.2 | P8.1 stable (#24) |
| [#24](https://github.com/IgnacioR04/WatchDogs/issues/24) | Generate compatible static JSON from PostgreSQL | P8.1 | P7 reconciliation approved (#25) |
| [#25](https://github.com/IgnacioR04/WatchDogs/issues/25) | Resumable idempotent historical migration and reconciliation | P7 | P6 green and real history access (#21) |
| [#26](https://github.com/IgnacioR04/WatchDogs/issues/26) | Production hardening, observability, backup and performance | P9 | P8 gate green (#22–#24) |
| [#27](https://github.com/IgnacioR04/WatchDogs/issues/27) | System acceptance and release report | FINAL | All P0–P11 gates green |
| [#28](https://github.com/IgnacioR04/WatchDogs/issues/28) | Evidence-based legacy cleanup | P11 | P10 accepted and stable observation period (#29) |
| [#29](https://github.com/IgnacioR04/WatchDogs/issues/29) | CI/CD and dual-run workflow transition | P10 | P9 gate green (#26) |

## P0 acceptance tracking

- [x] Repository, pipeline, generated data, history and bot workflow inventoried.
- [x] Current and legacy public contracts and in-repository consumers inventoried.
- [x] Test baseline and live-test separation recorded.
- [x] Configuration, secrets, personal-path and historical-storage assumptions recorded.
- [x] Migration risk register R1–R14 recorded.
- [x] No production code or generated data changed by the documentation work package.
- [x] Documentation/code review completed independently: final [APPROVE](https://github.com/IgnacioR04/WatchDogs/pull/30#pullrequestreview-4891444140).
- [x] QA and data-quality review completed independently: Data Quality [APPROVE](https://github.com/IgnacioR04/WatchDogs/pull/30#issuecomment-5231673121) and QA [PASS](https://github.com/IgnacioR04/WatchDogs/pull/30#issuecomment-5231682598).
- [x] Configuration-only security review completed independently: [PASS](https://github.com/IgnacioR04/WatchDogs/pull/30#issuecomment-5231706193).
- [x] PR [#30](https://github.com/IgnacioR04/WatchDogs/pull/30) merged by the release/orchestrator role as `91bda83`: release [PASS](https://github.com/IgnacioR04/WatchDogs/pull/30#issuecomment-5231721967).
- [x] Post-merge smoke test on `main` completed and issue [#2](https://github.com/IgnacioR04/WatchDogs/issues/2) closed: release and smoke [PASS](https://github.com/IgnacioR04/WatchDogs/pull/30#issuecomment-5231721967).
- [x] Hourly history-rewrite incident [#33](https://github.com/IgnacioR04/WatchDogs/issues/33) recovered through reviewed PR [#35](https://github.com/IgnacioR04/WatchDogs/pull/35), merged as `3cf491c`, while retaining the newer generated-data snapshot.
- [x] Hourly writer hardened through issue [#34](https://github.com/IgnacioR04/WatchDogs/issues/34) and reviewed PR [#36](https://github.com/IgnacioR04/WatchDogs/pull/36), merged as `0a8b894`; [manual run 31317548954](https://github.com/IgnacioR04/WatchDogs/actions/runs/31317548954) passed after activation.

## Next gates

1. Complete independent architecture and QA/documentation review of P1.1 issue [#6](https://github.com/IgnacioR04/WatchDogs/issues/6).
2. Do not begin P1.2 or mark any later gate complete until the ten P1.1 ADRs are accepted and merged.

## Approval limitation

All automated agents currently act through the single repository-owner GitHub identity. GitHub rejects official self-approval when that identity also authored the PR. Independent agents can still record separate review, QA, data-quality and security verdicts as PR review comments tied to an exact commit, but those comments are not equivalent to GitHub's protected-branch `APPROVED` state. A genuinely distinct GitHub identity is required if official independent approvals become a branch-protection requirement.

## Durable baseline documents

- [Current state](CURRENT_STATE.md)
- [Public contract](PUBLIC_CONTRACT.md)
- [Test baseline](TEST_BASELINE.md)
- [Risk register](RISK_REGISTER.md)
