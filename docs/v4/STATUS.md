# WATCHDOG V4 status

Last verified: 2026-08-09 against `main` commit `287e4d8`.

## Executive status

| Field | State |
|---|---|
| Current phase | P0 — Repository forensics, baseline and safety |
| Phase gate | **IN PROGRESS**; documentation PR, independent reviews, merge and post-merge smoke test remain |
| Migration progress | **0%** — no PostgreSQL, entity-resolution, repository or API migration has started |
| Production behavior | Unchanged; the current static pipeline remains authoritative |
| Known regressions | None introduced by V4 work |
| Blocking defects | None known after the live-test isolation merge |
| Default test baseline | `134 passed, 1 deselected` |
| Explicit live coverage | 1 Congress test, excluded unless `-m live` is requested |

## Work packages

| Item | Status | Evidence |
|---|---|---|
| Issue [#1](https://github.com/IgnacioR04/WatchDogs/issues/1), isolate live/mutating pytest coverage | Closed | PR [#3](https://github.com/IgnacioR04/WatchDogs/pull/3) merged as `287e4d8`; implementation commit `bde4303` |
| Issue [#2](https://github.com/IgnacioR04/WatchDogs/issues/2), P0 repository baseline | In progress | Branch `v4/p0-repo-audit`; this documentation set |

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
- [ ] Documentation/code review completed independently.
- [ ] QA and data-quality review completed independently.
- [ ] Configuration-only security review completed independently.
- [ ] PR merged by the release/orchestrator role.
- [ ] Post-merge smoke test on `main` completed and issue #2 closed.

## Next gates

1. Review the P0 documentation PR against issue #2 and [MASTER_PLAN.md](MASTER_PLAN.md).
2. Run independent QA: Markdown/path checks, `git diff --check`, default pytest, and generated-data cleanliness.
3. Complete data-quality review of contract classification, source limits and historical gaps.
4. Complete security review of configuration findings only; this package changes no attack surface.
5. Merge only after the required evidence is attached, smoke-test `main`, close #2, then begin P1 ADR/database planning.

## Approval limitation

All automated agents currently act through the single repository-owner GitHub identity. GitHub rejects official self-approval when that identity also authored the PR. Independent agents can still record separate review, QA, data-quality and security verdicts as PR review comments tied to an exact commit, but those comments are not equivalent to GitHub's protected-branch `APPROVED` state. A genuinely distinct GitHub identity is required if official independent approvals become a branch-protection requirement.

## Durable baseline documents

- [Current state](CURRENT_STATE.md)
- [Public contract](PUBLIC_CONTRACT.md)
- [Test baseline](TEST_BASELINE.md)
- [Risk register](RISK_REGISTER.md)
