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
