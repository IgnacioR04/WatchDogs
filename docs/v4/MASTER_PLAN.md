# WATCHDOG V4 — MASTER MULTI‑AGENT EXECUTION PLAN

> **Purpose:** This document is the authoritative execution runbook for evolving the existing WATCHDOG repository from a batch/static-JSON data pipeline into a production-grade, person-centric data platform with PostgreSQL, entity resolution, ingestion workers, FastAPI, auditable provenance, historical querying, and backward compatibility with the current dashboard/intelligence/trading layers.
>
> **Primary rule:** Do not rewrite WATCHDOG from scratch. Preserve working behavior, migrate incrementally, prove each phase with tests, and merge only after independent review and QA.
>
> **Repository:** `IgnacioR04/WatchDogs`
>
> **Historical context:** The repository has been heavily developed and maintained through Claude Code and automated WATCHDOG bot commits. Agents MUST inspect repository history, current behavior, tests, generated-data workflows, and architectural decisions before modifying anything. Existing Claude-authored code is not assumed to be correct, but it is also not disposable. Every change must be justified by evidence.

---

# 0. EXECUTIVE MISSION

WATCHDOG currently behaves primarily as:

```text
external sources
    ↓
scrapers
    ↓
normalization
    ↓
derived signals / scoring / market intelligence
    ↓
data/public/*.json
    ↓
GitHub Pages / dashboard / LLM context
```

The target architecture is:

```text
                    ┌─────────────────────────────┐
                    │       EXTERNAL SOURCES      │
                    │ SEC / House / Senate / OGE  │
                    │ FEC / Congress / Wikidata   │
                    │ Polymarket / GDELT / Market │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │ CONNECTORS / INGESTION      │
                    │ discovery / fetch / parse   │
                    │ normalize / validate        │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │ ENTITY RESOLUTION           │
                    │ Person / Org / Security     │
                    │ aliases / external IDs      │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │ POSTGRESQL — SOURCE OF TRUTH│
                    │ people / events / filings   │
                    │ provenance / coverage       │
                    │ ingestion runs / history    │
                    └──────────────┬──────────────┘
                                   │
                  ┌────────────────┴────────────────┐
                  ▼                                 ▼
          ┌───────────────┐                 ┌────────────────┐
          │ FastAPI /v1   │                 │ Static exporter│
          │ Query layer   │                 │ data/public/*  │
          └───────┬───────┘                 └───────┬────────┘
                  │                                  │
          ┌───────┴───────────┐                      │
          ▼                   ▼                      ▼
     Dashboard            LLM/Agents          Legacy compatibility
          │
          ▼
 WATCHDOG Intelligence
          │
          ▼
 regime / portfolio / risk / trader
```

The final product must support the following conceptual request:

> “Search any public figure, politician, executive, investor, manager or celebrity. Resolve who they are. Determine which public data sources are applicable. Return only real public records that were actually found, with provenance and coverage status. Never invent holdings, trades or disclosures.”

The API must distinguish:

- data **about** a person;
- financial events **performed/reported by** a person;
- holdings/disclosures **belonging to or filed by** a person;
- campaign-finance records **related to** a person;
- news **about** a person;
- prediction markets **about** a person.

A Polymarket market about a politician is not a financial position held by that politician.

---

# 1. NON‑NEGOTIABLE ENGINEERING PRINCIPLES

Every agent must obey these rules.

## 1.1 Preserve the working system during migration

Until an explicit deprecation phase:

- `run_all.py` must keep working.
- `run_pipeline.py` must keep working.
- `data/public/*.json` must remain available.
- the current dashboard must not be broken.
- current risk / portfolio / regime / trader code must not be broken.
- the hourly workflow must remain operational or be replaced only after the replacement is proven.
- existing public URLs must remain valid whenever practical.

Migration is additive first, substitutive later.

## 1.2 PostgreSQL becomes the new source of truth

The new API MUST NOT simply read `data/public/*.json`.

JSON files become:

- compatibility exports;
- cache/static snapshots;
- debugging artifacts;
- public GitHub Pages outputs.

The source of truth for the new query API is PostgreSQL.

## 1.3 Reads and ingestion are separate

A normal API request must not synchronously call SEC, FEC, OGE, Congress, Wikidata, GDELT and other sources.

Correct architecture:

```text
scheduled/manual ingestion
       ↓
 external source
       ↓
 PostgreSQL

user request
       ↓
 FastAPI
       ↓
 PostgreSQL
```

A refresh is an explicit ingestion action.

## 1.4 Identity is first-class

Names are not IDs.

The system must not equate:

```text
"Donald Trump"
"TRUMP DONALD J"
"Donald J. Trump"
```

using string equality alone.

Identity must be represented by canonical entities and external IDs.

## 1.5 No silent data loss

If a document cannot be parsed:

- persist the document metadata;
- persist parse status;
- persist parse error;
- record whether OCR or manual review is required.

Never silently disappear records just because parsing failed.

## 1.6 No silent truncation

Any cap such as 250 documents, 400 filings or top 50 managers must be explicitly classified as one of:

- `preview/live_fast`;
- `partial`;
- `complete`.

A complete historical ingestion must paginate/checkpoint until exhaustion or record why it did not.

## 1.7 Idempotency

Re-running the same ingestion must not duplicate data.

This must be enforced at database constraint level where possible, not only in Python.

## 1.8 Provenance is mandatory

Every externally derived record must know:

- provider/source;
- source record identifier;
- source URL when available;
- fetch timestamp;
- parser version;
- document hash where possible;
- confidence;
- relationship to the canonical person/org/security.

## 1.9 Anti-lookahead temporal model is preserved

The existing temporal concepts are retained:

- `event_date`
- `known_date`
- `scrape_date`
- `delay_days`

The invariant `known_date >= event_date` remains enforced.

## 1.10 Tests are gates, not suggestions

A builder does not approve its own work.

Every merged feature passes:

1. implementation;
2. independent code review;
3. independent tests/QA;
4. relevant data-quality checks;
5. required security review;
6. release/orchestrator gate.

---

# 2. MULTI‑AGENT ORGANIZATION

The system must operate as a coordinated engineering team.

No single agent should design, implement, review, test and merge a substantial feature alone.

## 2.1 Agent roles

### A. ORCHESTRATOR / PROGRAM LEAD

Responsibilities:

- reads this document first;
- inspects current repository state;
- creates GitHub issues/work packages;
- assigns each issue to a phase and owner-agent;
- ensures scope boundaries;
- prevents agents from editing overlapping files without coordination;
- enforces phase gates;
- monitors PR dependencies;
- decides when a phase is complete;
- never marks work done based only on builder claims;
- coordinates conflict resolution;
- maintains the migration board and progress document.

The Orchestrator should avoid writing production code except for tiny integration fixes.

Required artifacts:

- `docs/v4/STATUS.md`
- GitHub issues for each work package;
- milestone/phase tracking;
- dependency map;
- final phase acceptance report.

### B. REPOSITORY FORENSICS AGENT

Responsibilities:

- inspect repository history;
- identify generated vs source-controlled artifacts;
- inspect commits authored by Claude/Claude Code/watchdog-bot;
- identify obsolete documentation;
- map current workflows;
- map tests;
- map local-only assumptions;
- identify current output contracts;
- create baseline inventory.

This agent does not refactor.

### C. ARCHITECTURE AGENT

Responsibilities:

- define domain boundaries;
- propose DB schema;
- define repository interfaces;
- define entity-resolution rules;
- define API contracts;
- create Architecture Decision Records;
- identify migration risks.

This agent should avoid implementation except prototypes when necessary.

### D. BUILDER AGENTS

Multiple independent builders, each assigned a bounded work package.

Examples:

- DB Foundation Builder
- Domain Model Builder
- Entity Resolution Builder
- SEC Connector Builder
- Congress Connector Builder
- FEC Connector Builder
- OGE Connector Builder
- API Builder
- History Migration Builder
- Dashboard Migration Builder
- CI/Deployment Builder

A builder:

- works on one branch;
- edits only assigned scope unless coordinated;
- adds/updates tests associated with its code;
- documents decisions;
- opens a PR;
- never merges its own PR.

### E. CODE REVIEW AGENT

Responsibilities:

- reviews PR diff independently;
- checks architecture compliance;
- checks backward compatibility;
- searches for hidden truncation/data-loss;
- checks error handling;
- checks idempotency;
- checks transaction boundaries;
- checks type safety;
- checks configuration/secrets;
- requests changes rather than silently fixing substantial issues.

The reviewer must not be the same agent/context that implemented the change.

### F. QA / TEST AGENT

Responsibilities:

- checks out the PR branch;
- runs required automated suites;
- adds adversarial tests if coverage is insufficient;
- performs integration tests;
- validates migrations;
- checks API behavior;
- checks repeated ingestion;
- checks rollback if relevant;
- reports exact evidence.

QA should not assume passing existing tests means the feature works.

### G. DATA QUALITY / PROVENANCE AGENT

Responsibilities:

- validate data semantics;
- inspect representative real source records;
- detect false identity merges;
- detect false ticker associations;
- verify temporal fields;
- verify coverage states;
- verify source provenance;
- verify historical completeness/partial status;
- inspect counts before/after migration.

This role is mandatory for connector and migration PRs.

### H. SECURITY / PRIVACY REVIEW AGENT

Responsibilities:

- secrets/env audit;
- admin endpoint auth;
- injection checks;
- CORS;
- rate limiting;
- request validation;
- log redaction;
- dependency risk;
- PII handling;
- SSRF risk for source URLs;
- path traversal/file handling;
- database permissions.

Mandatory for API/admin/deployment phases.

### I. RELEASE MANAGER AGENT

Responsibilities:

- confirms required approvals;
- verifies branch is current with `main`;
- verifies CI green;
- verifies migrations forward/backward strategy;
- merges PRs in dependency order;
- tags milestones/releases where appropriate;
- updates changelog/status;
- performs post-merge smoke checks.

The Release Manager does not bypass red tests.

---

# 3. THE REQUIRED AGENT LOOP

Every work package follows this lifecycle:

```text
GitHub Issue
    ↓
Builder branch
    ↓
Implementation + builder tests
    ↓
Pull Request
    ↓
Independent Code Review
    ↓
Independent QA/Test
    ↓
Data Quality review (when applicable)
    ↓
Security review (when applicable)
    ↓
Builder fixes requested findings
    ↓
Re-review
    ↓
Re-test
    ↓
Release Manager merge
    ↓
Post-merge smoke test
    ↓
Issue closed
```

If review or QA discovers a material architectural problem, return to the Architecture Agent rather than layering patches.

No phase may advance if its gate is red.

---

# 4. GIT AND GITHUB OPERATING CONTRACT

The repository has a meaningful history generated by human work, Claude Code, Claude co-authored commits and `watchdog-bot` data refreshes. Agents must treat git history as evidence.

## 4.1 Before any code edit

Every builder must run/inspect:

```bash
git status
git branch --show-current
git log --oneline --decorate -n 40
git remote -v
git fetch origin
git log --oneline origin/main..HEAD
git log --oneline HEAD..origin/main
```

Also inspect relevant file history:

```bash
git log --follow -- path/to/file
git blame path/to/file
```

Goal: understand why code exists before replacing it.

## 4.2 Main branch

Rules:

- no direct feature pushes to `main`;
- no history rewriting on `main`;
- no `git push --force` to `main`;
- no deleting historical commits;
- no squashing data-history blindly if it changes public behavior.

## 4.3 Branch naming

Examples:

```text
v4/p0-repo-audit
v4/p1-db-foundation
v4/p2-domain-repository
v4/p3-entity-resolution
v4/p4-sec-ingestion
v4/p5-fec-connector
v4/p6-api-people
v4/p7-history-import
v4/p8-dashboard-api
v4/p9-production-hardening
fix/v4-13f-filing-window
```

One branch should map to one coherent issue/work package.

## 4.4 Commits

Commit messages must explain intent.

Good:

```text
v4(db): add canonical person and alias tables
v4(entity): add ambiguity-safe person resolver
v4(sec): persist form4 records idempotently
fix(13f): distinguish filing-window pending from late
test(api): add cursor pagination regression coverage
```

Avoid:

```text
fix stuff
changes
wip final
claude update
```

## 4.5 Generated data

`data/public/*` is generated output.

Code PRs should avoid unrelated huge generated-data diffs.

If a code change legitimately changes generated contracts:

- explain it in PR;
- include a small representative fixture or intentional generated snapshot;
- avoid mixing hundreds of incidental hourly changes.

## 4.6 Pull request template

Every V4 PR must contain:

```markdown
## Work package
Issue:
Phase:

## Goal

## Files changed

## Database/schema impact

## API contract impact

## Backward compatibility

## Data/provenance impact

## Tests run

## Repeated-ingestion/idempotency evidence

## Reviewer concerns / known debt

## Rollback plan

## Generated data changed?
yes/no

## Secrets/config changed?
yes/no
```

## 4.7 Merge conditions

A PR cannot merge unless:

- builder tests pass;
- CI passes;
- independent reviewer approves;
- QA approves;
- data reviewer approves when data semantics change;
- security approves when attack surface changes;
- migrations are reviewed when DB changes;
- backward compatibility status is explicit.

---

# 5. REQUIRED PROJECT DOCUMENTATION

Create and maintain:

```text
docs/v4/
├── MASTER_PLAN.md
├── STATUS.md
├── ARCHITECTURE.md
├── DOMAIN_MODEL.md
├── DATA_SOURCES.md
├── ENTITY_RESOLUTION.md
├── API_CONTRACT.md
├── INGESTION.md
├── MIGRATION.md
├── TEST_STRATEGY.md
├── SECURITY.md
├── OPERATIONS.md
├── ROLLBACK.md
└── adr/
    ├── ADR-0001-postgres-source-of-truth.md
    ├── ADR-0002-person-centric-identity.md
    ├── ADR-0003-read-write-separation.md
    └── ...
```

`STATUS.md` is continuously maintained by the Orchestrator and must include:

- current phase;
- open issues;
- merged PRs;
- blockers;
- known regressions;
- current test counts;
- migration status;
- next gate.

---

# 6. TARGET DOMAIN MODEL

The following is the minimum conceptual model.

## 6.1 Persons

```text
persons
- id UUID PK
- canonical_name
- normalized_name
- slug UNIQUE
- entity_type
- birth_date nullable
- country_code nullable
- description nullable
- created_at
- updated_at
```

## 6.2 Person aliases

```text
person_aliases
- id
- person_id FK
- alias
- normalized_alias
- source
- confidence
- created_at
```

Indexes:

- normalized alias B-tree;
- pg_trgm GIN/GiST for similarity search.

## 6.3 External identities

```text
external_identities
- id
- person_id
- provider
- external_id
- external_url nullable
- verified
- confidence
- metadata JSONB
- created_at
- updated_at
```

Expected providers include:

```text
wikidata
sec_cik
congress_bioguide
fec_candidate
oge
house
senate
polymarket_wallet
```

Unique constraints should prevent the same provider/external ID from mapping to multiple people unless explicitly modelled as an exceptional relationship.

## 6.4 Person roles

```text
person_roles
- id
- person_id
- role_type
- organization_id nullable
- title nullable
- start_date nullable
- end_date nullable
- source_id nullable
- metadata JSONB
```

Roles are extensible.

## 6.5 Organizations

```text
organizations
- id UUID
- canonical_name
- normalized_name
- organization_type
- sec_cik nullable
- wikidata_qid nullable
- metadata JSONB
- created_at
- updated_at
```

## 6.6 Securities

```text
securities
- id UUID
- ticker nullable
- cusip nullable
- isin nullable
- issuer_organization_id nullable
- asset_name
- exchange nullable
- metadata JSONB
```

Do not assume ticker is always available.

## 6.7 Data sources

```text
data_sources
- id
- provider
- source_type
- name
- base_url nullable
- authoritative_level
- metadata JSONB
```

## 6.8 Source documents

```text
source_documents
- id UUID
- source_id
- source_record_id
- source_url
- fetched_at
- http_status nullable
- content_sha256 nullable
- parser_version
- parse_status
- parse_error nullable
- requires_ocr boolean
- metadata JSONB
```

## 6.9 Events

```text
events
- id UUID
- person_id nullable
- organization_id nullable
- security_id nullable
- event_type
- direction nullable
- event_date
- known_date
- scrape_date
- delay_days nullable
- amount_min nullable
- amount_max nullable
- amount_estimated nullable
- source_id
- source_record_id
- source_document_id nullable
- confidence
- metadata JSONB
- created_at
- updated_at
```

## 6.10 Specialized tables

At minimum consider:

```text
trades
holdings
ownership_filings
financial_disclosures
campaign_finance_records
news_mentions
prediction_markets
```

Specialized fields belong here rather than forcing every source into a single generic JSON blob.

## 6.11 Coverage

Coverage is a first-class concept.

Possible table:

```text
person_source_coverage
- person_id
- source_id
- status
- last_checked_at
- last_success_at
- records_found
- coverage_from
- coverage_to
- completeness
- error_code nullable
- error_message nullable
- metadata JSONB
```

Allowed statuses:

```text
available
no_records
not_applicable
not_checked
partial
stale
source_error
```

## 6.12 Ingestion runs

```text
ingestion_runs
- id UUID
- source_id
- scope_type
- scope_value
- started_at
- finished_at
- status
- records_discovered
- records_inserted
- records_updated
- records_failed
- watermark_before
- watermark_after
- partial_reason nullable
- error_summary nullable
- metadata JSONB
```

---

# 7. PHASE 0 — REPOSITORY FORENSICS, BASELINE AND SAFETY

## Goal

Create a trustworthy baseline before refactoring.

## Lead agents

- Repository Forensics Agent
- Orchestrator
- QA Agent

## Work packages

### P0.1 Repository inventory

Inspect:

- root scripts;
- `scrapers/`;
- `normalize/`;
- `pipelines/`;
- `portfolio/`;
- `risk/`;
- `regime/`;
- `.github/workflows/`;
- `tests/`;
- `dashboard/`;
- `data/public/`;
- git history.

Produce:

`docs/v4/CURRENT_STATE.md`

Must include:

- actual current pipeline;
- outdated docs;
- generated outputs;
- local-only paths;
- external dependencies;
- source caps;
- known partial datasets;
- historical data locations;
- test suite structure;
- bot workflows.

### P0.2 Baseline tests

Run:

```bash
pytest
```

Separate:

- deterministic unit tests;
- live integration tests;
- tests requiring secrets;
- tests requiring filesystem history.

Record baseline.

### P0.3 Current public contract

Capture:

- public JSON filenames;
- schemas;
- dashboard dependencies;
- LLM context dependencies;
- workflow command entrypoints.

### P0.4 Secrets/config audit

Identify:

- hardcoded email fallback;
- local Windows paths;
- secrets;
- environment variables;
- Drive assumptions.

Do not change yet unless it is an immediate security issue.

### P0.5 Risk register

Create a migration risk table:

- data duplication;
- missing records;
- identity false merge;
- DB migration failure;
- dashboard regression;
- workflow downtime;
- source rate limits;
- generated data conflicts;
- history import inconsistency.

## Gate P0

Phase 0 passes only if:

- baseline tests are documented;
- current architecture is documented;
- main public contracts are known;
- risks are known;
- no code behavior has been unintentionally changed.

---

# 8. PHASE 1 — ARCHITECTURE AND DATABASE FOUNDATION

## Goal

Create the runtime foundation without migrating existing behavior yet.

## Lead agents

- Architecture Agent
- DB Foundation Builder
- DB Reviewer
- QA Agent

## Work packages

### P1.1 Architecture Decision Records

Required ADRs:

1. PostgreSQL as source of truth.
2. SQLAlchemy 2 + Alembic.
3. UUID canonical identity.
4. repository/service separation.
5. read vs ingestion separation.
6. static JSON compatibility exporter.
7. cursor pagination strategy.
8. event + specialized-table design.
9. provenance requirements.
10. entity resolution non-auto-merge rule.

### P1.2 Dependencies

Add appropriate pinned/compatible packages for:

- FastAPI;
- SQLAlchemy 2;
- psycopg;
- Alembic;
- pydantic-settings;
- test DB tooling;
- httpx;
- optional rate limiting library if chosen.

Avoid unnecessary infrastructure.

Do not add Redis yet unless a concrete phase requires it.

### P1.3 Settings

Create central application settings.

All environment-specific values must come from env/config.

Required minimum:

```env
DATABASE_URL=
APP_ENV=
LOG_LEVEL=
USER_AGENT_EMAIL=
FRED_API_KEY=
ADMIN_API_KEY=
CORS_ORIGINS=
WATCHDOG_HISTORY_DIR=
```

No personal paths/emails as production defaults.

### P1.4 DB package

Suggested structure:

```text
watchdog/
  db/
    base.py
    session.py
    models/
    repositories/
```

If introducing a new package root would be too disruptive, document the chosen alternative.

### P1.5 Initial migrations

Create Alembic setup and initial schema.

### P1.6 DB lifecycle tests

Test:

- migrate empty DB to head;
- create core entities;
- constraints;
- uniqueness;
- FK behavior;
- rollback strategy;
- migration rerun safety.

## Independent review focus

Reviewer asks:

- Are constraints strong enough for idempotency?
- Are source IDs modelled correctly?
- Are nullable relationships realistic?
- Is JSONB being overused?
- Are temporal fields preserved?
- Are database defaults timezone-safe?
- Is schema future-proof but not over-engineered?

## Gate P1

Pass only if:

- fresh PostgreSQL can migrate to head;
- test DB suite is green;
- no current pipeline behavior is broken;
- secrets/local paths are centrally configurable;
- architectural ADRs are approved.

---

# 9. PHASE 2 — DOMAIN SERVICES AND REPOSITORY LAYER

## Goal

Create persistence interfaces before refactoring scrapers.

## Lead agents

- Domain Model Builder
- Repository Builder
- Reviewer
- QA

## Required components

### P2.1 Repository interfaces

Create repositories/services for at least:

- Person
- Alias
- ExternalIdentity
- Organization
- Security
- SourceDocument
- Event
- Coverage
- IngestionRun

### P2.2 Idempotent upserts

Define natural uniqueness per source.

Examples:

```text
(source_id, source_record_id)
(provider, external_id)
(person_id, normalized_alias, source)
```

Do not use mutable fields like scrape timestamp as dedupe keys.

### P2.3 Transaction boundaries

One ingestion batch should have explicit transaction strategy.

Clarify behavior on partial failure:

- rollback whole filing?
- save successful records and mark run partial?
- retry failed document?

Document per connector type.

### P2.4 Normalized DTOs

Create typed normalized models between parser and repository.

Example conceptual pipeline:

```text
HTTP source document
    ↓
parser
    ↓
NormalizedTradeDTO
    ↓
identity linker
    ↓
repository.upsert_trade()
```

Scraper parsers should not import FastAPI or UI code.

### P2.5 Static exporter abstraction

Create an exporter boundary but do not necessarily switch all JSON generation yet.

## Required tests

- repeated upsert;
- concurrent duplicate attempt;
- conflicting external identity;
- event update vs duplicate;
- transaction rollback;
- source document dedupe.

## Gate P2

Pass only if repository behavior is demonstrably idempotent and existing pipeline remains intact.

---

# 10. PHASE 3 — ENTITY RESOLUTION

## Goal

Make WATCHDOG capable of understanding that strings refer to canonical entities.

This is a critical correctness phase.

## Lead agents

- Entity Resolution Builder
- Data Quality Agent
- Reviewer
- QA

## P3.1 Name normalization

Implement deterministic normalization:

- Unicode normalization;
- case-folding;
- punctuation normalization;
- whitespace;
- common suffix handling;
- inverted-name handling only as candidate logic;
- preserve original names.

Never destroy original source strings.

## P3.2 Exact local lookup

Order:

1. verified external identity;
2. exact canonical normalized name;
3. exact alias;
4. deterministic known transformations;
5. fuzzy candidates.

## P3.3 pg_trgm candidate search

Fuzzy matching generates candidates.

It must never auto-merge by similarity score alone.

## P3.4 Candidate scoring

Candidate evidence may include:

- alias match;
- birth date;
- country;
- organization;
- role/title;
- SEC CIK;
- Bioguide ID;
- FEC candidate ID;
- Wikidata ID;
- source-provided relationship.

Define explainable match reasons.

## P3.5 Ambiguity state

If two plausible candidates exist:

```text
resolution_status = ambiguous
```

Do not choose silently.

Persist candidate review data.

## P3.6 Manual overrides

Support verified manual linkage/merge/split decisions.

Every manual decision must be auditable.

## P3.7 Merge policy

A canonical person merge requires strong evidence.

Create tests for homonyms.

## Required adversarial tests

- same person, capitalization difference;
- surname-first names;
- middle initials;
- suffix Jr/Sr;
- diacritics;
- same exact name, different people;
- SEC owner alias;
- candidate/politician cross-source identity;
- incorrect fuzzy near-match;
- manual override.

## Gate P3

Pass only if Data Quality Agent signs off on low false-merge risk.

False negatives are acceptable early.

False positive identity merges are not.

---

# 11. PHASE 4 — MIGRATE EXISTING CONNECTORS TO DATABASE

This phase should be split into separate PRs and builder agents.

## Common connector contract

Each connector should expose conceptually:

```text
discover()
fetch()
parse()
normalize()
persist()
update_coverage()
finish_ingestion_run()
```

HTTP fetch and parsing should be separable for fixture-based tests.

## P4.A SEC INSIDERS

### Goals

Refactor Form 3/4/5 ingestion.

### Requirements

- retain existing XML parser behavior;
- persist source documents;
- link reporting owner to Person;
- link issuer to Organization/Security;
- preserve transaction code;
- preserve filing date;
- preserve event/known date;
- remove silent complete-mode `MAX_FILINGS=400` truncation;
- add pagination/watermarks;
- record partial run if limited.

### Tests

- fixture parse;
- multiple transactions in one filing;
- repeated filing;
- amended/repeated filing;
- unknown ticker;
- identity linkage;
- pagination.

## P4.B SEC 13D/13G

Requirements:

- source document provenance;
- filer person/org modelling;
- issuer/security linkage;
- beneficial ownership fields;
- amendments;
- complete vs partial mode;
- no silent 250-document truncation.

## P4.C SEC 13F

### Important redesign

Keep curated smart-money universe as a feature, not as global truth.

Need two concepts:

```text
all supported/discovered 13F filers
curated smart_money_universe
```

### Fix stale semantics

States:

```text
current
pending_within_filing_window
late
unavailable
```

Never classify a manager as late merely because another manager filed earlier.

### Holdings completeness

Avoid "top 100 only" for canonical database history unless explicitly marked preview.

Static JSON can still export top N for dashboard.

## P4.D HOUSE PTR

Requirements:

- retain high-confidence explicit ticker parsing;
- persist every filing metadata record;
- persist PDF source document;
- record:
  - parsed;
  - no_transactions;
  - requires_ocr;
  - parse_error.
- do not silently drop scanned PDFs.

OCR is a later optional enhancement.

## P4.E SENATE

Requirements:

- preserve mirror provenance;
- clearly mark non-official mirror when used;
- preserve historical limitations;
- avoid falsely presenting old mirror coverage as current.

## P4.F POLYMARKET

Requirements:

- distinguish trader profile from person/public-figure subject;
- wallet identity is not automatically a famous person's identity;
- prediction markets about a person are separate entities/events;
- retain correct pagination and unbiased closed-position scoring.

## P4.G GDELT

Refactor query service to support:

- security/company news;
- person news;
- canonical name + aliases.

Do not rely only on top signal tickers.

## Common P4 gate

For every connector:

- fixture tests green;
- repeated ingestion produces no duplicates;
- provenance complete;
- coverage status updated;
- error/partial state tested;
- static output compatibility proven where relevant.

---

# 12. PHASE 5 — NEW PERSON-CENTRIC CONNECTORS

Each source is a separate work package/PR.

## P5.A WIKIDATA IDENTITY CONNECTOR

Purpose:

- identity discovery;
- aliases;
- public roles;
- organization relationships;
- useful external IDs.

Not authoritative for financial transactions.

Requirements:

- cache/store resolved IDs;
- provenance;
- rate limiting;
- ambiguity-safe matching.

## P5.B CONGRESS.GOV IDENTITY CONNECTOR

Purpose:

- stable Bioguide identity;
- member metadata;
- congressional role context.

It complements House/Senate financial disclosures.

Do not confuse legislative activity with financial activity.

## P5.C FEC / OPENFEC CONNECTOR

Purpose:

- candidate identity;
- candidate IDs;
- committees;
- campaign finance.

Campaign finance must remain semantically separate from personal portfolio/trading.

Coverage must distinguish:

- candidate found;
- committee found;
- records found;
- no records.

## P5.D OGE CONNECTOR

Purpose:

- Executive Branch public financial disclosure;
- presidential/VP candidate disclosure where publicly available;
- periodic transaction reports where applicable.

Requirements:

- save source document metadata;
- parse only fields supported by evidence;
- if the source is PDF/HTML and parser cannot recover a field, mark it;
- never infer private holdings.

## P5 gate

For a representative sample of public figures, demonstrate:

- entity resolves;
- applicable sources identified;
- unavailable/non-applicable sources are explicit;
- records have provenance;
- no fabricated data.

---

# 13. PHASE 6 — FASTAPI QUERY LAYER

## Goal

Expose stable, versioned, source-of-truth-backed queries.

## Lead agents

- API Builder
- Security Reviewer
- QA
- Data Quality reviewer

## Structure

Suggested:

```text
watchdog/api/
├── main.py
├── dependencies.py
├── errors.py
├── pagination.py
├── schemas/
└── routers/
    ├── health.py
    ├── people.py
    ├── organizations.py
    ├── securities.py
    ├── events.py
    └── admin.py
```

## Required endpoints

### Health

```http
GET /health
GET /ready
```

`/health` means process is alive.

`/ready` means required dependencies such as DB are usable.

### People

```http
GET /v1/people/search?q=
GET /v1/people/{person_id}
GET /v1/people/{person_id}/summary
GET /v1/people/{person_id}/aliases
GET /v1/people/{person_id}/roles
GET /v1/people/{person_id}/coverage
```

### Events/data

```http
GET /v1/people/{person_id}/events
GET /v1/people/{person_id}/trades
GET /v1/people/{person_id}/holdings
GET /v1/people/{person_id}/ownership
GET /v1/people/{person_id}/financial-disclosures
GET /v1/people/{person_id}/sec-filings
GET /v1/people/{person_id}/campaign-finance
GET /v1/people/{person_id}/news
GET /v1/people/{person_id}/prediction-markets
```

### Organizations

```http
GET /v1/organizations/search
GET /v1/organizations/{id}
```

### Securities

```http
GET /v1/securities/search
GET /v1/securities/{ticker}
GET /v1/securities/{ticker}/events
```

### Admin

```http
POST /v1/admin/people/resolve
POST /v1/admin/people/{id}/refresh
POST /v1/admin/ingestion/run
GET  /v1/admin/ingestion/runs/{id}
```

Admin endpoints require authentication.

## Pagination

Use cursor pagination for large time-ordered datasets.

Response concept:

```json
{
  "items": [],
  "next_cursor": "...",
  "has_more": false
}
```

Avoid offset pagination for very large event history.

## API filters

At minimum:

```text
from
to
source
event_type
direction
limit
cursor
```

## API response rules

Responses should include:

- canonical IDs;
- dates;
- source/provenance references;
- confidence;
- coverage/freshness where relevant.

Do not generate unsupported narrative claims.

## Error semantics

Examples:

- 400 invalid filters;
- 404 canonical entity not found;
- 409 ambiguous resolution/admin conflict;
- 422 validation;
- 503 dependency unavailable.

## Security tests

- admin auth;
- SQL injection through filters/search;
- oversized query params;
- CORS;
- rate limiting;
- secret leakage;
- logs;
- error stack leakage.

## Gate P6

A test client must be able to query a person entirely from PostgreSQL while external sources are mocked/offline.

---

# 14. PHASE 7 — HISTORICAL MIGRATION

## Goal

Import existing `WATCHDOG_HISTORY` into the canonical database without losing provenance or creating duplicates.

## Lead agents

- Migration Builder
- Data Quality Agent
- QA

## Importer

Create:

```text
scripts/import_watchdog_history.py
```

Requirements:

- resumable;
- idempotent;
- partition-aware;
- logs counts;
- ingestion run records;
- dry-run mode;
- source-specific mapping;
- bad record quarantine.

## Pre-import inventory

Record:

- record count per source;
- date min/max;
- unique tickers;
- unique actor strings;
- file count;
- malformed lines.

## Import identity strategy

Do not aggressively merge all historical actor names.

Safer order:

1. load raw actor identities;
2. exact/verified external matches;
3. candidate matching;
4. unresolved actors remain unresolved rather than forced.

## Reconciliation report

For each source produce:

```text
input_records
parsed_records
inserted_records
updated_records
duplicate_records
quarantined_records
unresolved_identity_records
date_range_before
date_range_after
```

Counts must explain discrepancies.

## Index replacement

After DB history is trusted, SQL/API can replace:

- `dataset_index.json`
- `ticker_index.json`
- `actor_index.json`

Do not delete old indexes until reconciliation is accepted.

## Gate P7

Data Quality Agent must approve reconciliation.

---

# 15. PHASE 8 — STATIC EXPORTS, INTELLIGENCE AND DASHBOARD MIGRATION

This phase happens only after the database/API are stable.

## P8.1 Static JSON exporter

Implement:

```text
exporters/static_json.py
```

Generate current public artifacts from canonical DB where practical.

Goal:

```text
PostgreSQL
    ↓
export
    ↓
data/public
```

rather than live scrapers directly owning the public contract.

## P8.2 Intelligence migration

Gradually replace internal direct file reads with repository/query interfaces.

Recommended sequence:

1. signals;
2. news/movements;
3. LLM context;
4. market universe lookup;
5. portfolio/risk dependencies if beneficial.

Do not refactor risk/portfolio just because V4 exists.

## P8.3 Dashboard migration

Migrate one tab at a time.

Add a global person search:

```text
Search any person
    ↓
person profile
roles
coverage
financial disclosures
events
campaign finance
news
prediction markets
sources
```

Keep old tabs working during rollout.

## P8.4 Compatibility tests

Snapshot/contract tests compare legacy JSON shape to new exporter.

## Gate P8

Dashboard works with API-backed features and existing critical views remain functional.

---

# 16. PHASE 9 — PRODUCTION HARDENING

## P9.1 Docker

Add:

```text
Dockerfile
docker-compose.yml
```

Minimum services:

```text
api
postgres
```

Optional worker only if required.

## P9.2 Logging

Structured logs with:

- timestamp;
- request ID;
- ingestion run ID;
- source;
- severity.

No secrets.

## P9.3 Observability

At minimum:

- API health;
- DB readiness;
- ingestion status;
- last successful source refresh;
- record counts;
- failed parse counts;
- partial coverage counts.

## P9.4 Backups

Document:

- PostgreSQL backup;
- restore;
- migration recovery;
- source document retention.

Test restore procedure.

## P9.5 Rate limits and source etiquette

Centralize provider-specific rate controls.

## P9.6 Dependency/security audit

Run dependency audit and review attack surface.

## P9.7 Performance

Test representative:

- people search;
- person timeline;
- large event pagination;
- historical security event query.

Add indexes based on measured query plans.

## Gate P9

Production readiness review approved by Security + QA + Release Manager.

---

# 17. PHASE 10 — CI/CD AND GITHUB WORKFLOW TRANSITION

## Goal

Move persistence from git commits toward the database without sudden breakage.

## Transitional state

Current workflow may continue:

```text
scrape
→ current JSON
→ bot commit
```

while parallel V4 jobs test:

```text
ingest
→ PostgreSQL
→ verification
```

## Target state

```text
scheduled ingestion
      ↓
PostgreSQL
      ↓
derived processing
      ↓
static exporter
      ↓
optional data/public commit
```

## CI jobs

Recommended:

```text
lint/type/static checks
unit tests
db migration tests
API tests
connector fixture tests
entity-resolution tests
security checks
integration tests
legacy regression tests
```

Live external-source tests should be separate and not make normal CI flaky.

## Bot/history considerations

Preserve meaningful separation between:

- code commits;
- migration commits;
- generated-data bot commits.

Avoid merging a bot data refresh into feature diffs unless necessary.

## Gate P10

No production data flow is switched until new flow has run successfully in parallel enough times to establish confidence.

---

# 18. PHASE 11 — LEGACY CLEANUP

Only after stable production operation.

Possible cleanup:

- remove direct JSON persistence from old scrapers;
- remove obsolete indexes;
- remove obsolete README architecture descriptions;
- reduce generated data stored in git if desired;
- remove local Drive-specific history assumptions;
- consolidate duplicate connectors;
- deprecate unused workflows.

Every deletion needs proof that no consumer depends on it.

---

# 19. CROSS‑PHASE TEST STRATEGY

Testing must be layered.

## 19.1 Unit

Fast, deterministic.

Covers:

- parsers;
- normalization;
- temporal rules;
- repositories;
- entity scoring;
- API schemas;
- coverage mapping.

## 19.2 Database integration

Real PostgreSQL test service.

Covers:

- migrations;
- indexes;
- constraints;
- transactions;
- upserts;
- concurrency.

## 19.3 Connector fixtures

Store sanitized representative source fixtures.

Test parsing without network.

## 19.4 Live integration

Separate marker/job.

Examples:

```bash
pytest -m live
```

Not required for every PR if external sources are unstable.

## 19.5 Contract tests

Protect:

- public JSON schemas;
- API response schemas;
- important CLI behavior.

## 19.6 Regression tests

Every discovered bug gets a regression test before or with the fix.

## 19.7 Data-quality tests

Examples:

- `known_date >= event_date`;
- source URL/provenance exists;
- no invalid ticker pollution;
- 13F filing window semantics;
- no person merge solely on fuzzy name;
- partial ingestion is marked;
- scanned House PDF remains recorded.

## 19.8 End-to-end personas

Test several classes without asserting unstable live financial values.

Required categories:

1. Executive/candidate-type public figure;
2. member of Congress;
3. SEC corporate insider;
4. institutional manager;
5. public celebrity with little/no mandatory financial disclosure.

Expected behavior:

- identity resolves or ambiguity is explicit;
- source applicability is correct;
- records are real;
- absent records return `no_records`;
- inapplicable sources return `not_applicable`;
- no fabricated holdings.

---

# 20. REVIEW CHECKLIST

Every Code Review Agent checks:

## Architecture

- Does code respect layer boundaries?
- Does API bypass repository?
- Does parser write directly to JSON/DB unexpectedly?
- Is identity logic duplicated?

## Data

- Could records be silently lost?
- Could data be silently truncated?
- Is provenance present?
- Are coverage states accurate?
- Is partial data labelled?

## Identity

- Can two people be incorrectly merged?
- Is fuzzy matching being treated as proof?
- Are external IDs used correctly?

## Database

- Are constraints adequate?
- Is migration safe?
- Is query indexed?
- Is transaction scope clear?

## Reliability

- timeouts?
- retries?
- rate limits?
- partial failures?
- idempotency?

## Compatibility

- current pipeline?
- public JSON?
- dashboard?
- scripts?
- tests?

## Configuration

- no hardcoded secrets?
- no machine-specific paths?
- env documented?

---

# 21. QA EVIDENCE TEMPLATE

The QA Agent must post evidence in every PR:

```markdown
## QA result
PASS / FAIL

## Commit tested
<sha>

## Environment

## Commands run
- ...

## Unit tests
x passed / y failed

## DB migration test
PASS/FAIL

## API tests
PASS/FAIL

## Idempotency test
PASS/FAIL/not applicable

## Backward compatibility
PASS/FAIL/not applicable

## Data quality checks
PASS/FAIL/not applicable

## Manual scenarios
1. ...
2. ...

## Bugs found
- ...

## Residual risk
- ...
```

---

# 22. DEFINITION OF DONE — WORK PACKAGE

A work package is done only when:

- issue scope is satisfied;
- implementation exists;
- code is documented;
- tests exist;
- tests pass;
- reviewer approves;
- QA approves;
- data/security approvals exist where required;
- no unrelated generated-data noise;
- migration/backward-compatibility impact is explicit;
- PR merged;
- post-merge smoke test passes;
- issue closed;
- `STATUS.md` updated.

---

# 23. DEFINITION OF DONE — PHASE

A phase is done only when:

- all required work packages are merged;
- all phase tests pass on `main`;
- phase acceptance criteria are signed off;
- no P0/P1 blocking defect remains;
- documentation reflects current behavior;
- rollback path is understood;
- Orchestrator records phase completion.

---

# 24. FINAL SYSTEM ACCEPTANCE CRITERIA

WATCHDOG V4 is not complete unless all of the following are true.

## Architecture

1. PostgreSQL is the source of truth for the new API.
2. API reads do not depend on `data/public/*.json`.
3. ingestion and query concerns are separate.
4. static JSON is exporter/compatibility output.

## Identity

5. canonical Person exists.
6. aliases exist.
7. external identities exist.
8. organizations and securities are separate entities.
9. entity resolution is ambiguity-safe.
10. fuzzy name match alone cannot merge people.
11. manual resolution overrides are auditable.

## Data

12. provenance exists.
13. source documents are tracked.
14. parse failures are visible.
15. partial ingestions are visible.
16. event/known/scrape temporal semantics are preserved.
17. complete mode does not silently truncate.
18. 13F filing-window logic is correct.
19. House scanned PDFs are not silently discarded.

## API

20. `/v1/people/search` uses PostgreSQL.
21. person detail works.
22. coverage works.
23. events work.
24. filters work.
25. cursor pagination works.
26. campaign finance is separate from personal holdings.
27. prediction markets about a person are semantically separate.
28. provenance is exposed.
29. admin refresh/ingestion is protected.
30. `/docs`/OpenAPI is coherent.

## Historical data

31. existing history can be imported idempotently.
32. reconciliation explains counts.
33. SQL can replace legacy actor/ticker indexes after validation.

## Compatibility

34. current critical pipeline remains working during migration.
35. static public data remains available until explicit deprecation.
36. risk/regime/portfolio/trader do not regress unintentionally.

## Engineering

37. Alembic migrations work from empty DB.
38. Docker local environment works.
39. CI is green.
40. independent reviewer/QA workflow is enforced.
41. secrets are environmental.
42. hardcoded personal machine paths are removed.
43. operational backup/restore is documented and tested.

---

# 25. ORCHESTRATOR STARTUP PROCEDURE

When a new AI agent/team receives this document, the Orchestrator must execute this order.

## Step 1 — Do not code yet

Read:

- this document;
- repository README;
- `PROJECT_CONTEXT.md`;
- `run_all.py`;
- `run_pipeline.py`;
- workflows;
- all current source directories;
- current tests;
- recent git history.

## Step 2 — Verify repository state

Check:

```bash
git status
git fetch origin
git branch -avv
git log --oneline --decorate -n 50
```

Confirm repository ownership/remotes and current `main`.

## Step 3 — Establish baseline

Run current tests.

Record failures before V4 work.

## Step 4 — Create V4 documentation branch

Create:

```text
v4/p0-repo-audit
```

Add `docs/v4/`.

Do not make architecture-changing code in this PR.

## Step 5 — Create GitHub milestone/issues

Create issues for phases/work packages.

Each issue must include:

- scope;
- owned files;
- dependencies;
- acceptance criteria;
- test requirements;
- reviewer type;
- data/security review requirements.

## Step 6 — Complete Phase 0

Merge only audit/docs baseline.

## Step 7 — Begin Phase 1

From that point onward use the mandatory agent loop.

---

# 26. AGENT PROMPT TEMPLATES

## 26.1 Builder prompt

```text
You are the Builder Agent for GitHub issue <ID> in WATCHDOG V4.

Read:
- docs/v4/MASTER_PLAN.md
- docs/v4/STATUS.md
- issue <ID>
- relevant ADRs
- relevant existing source and git history.

Do not broaden scope.

Before editing:
1. fetch origin;
2. inspect branch divergence;
3. inspect relevant file history;
4. run relevant baseline tests.

Implement only the assigned work package.
Preserve backward compatibility required by the issue.
Add deterministic tests.
Do not merge.
Open a PR with the V4 PR template.
Report known limitations truthfully.
```

## 26.2 Reviewer prompt

```text
You are an independent Code Review Agent.
You did not implement this PR.

Review the PR against:
- issue acceptance criteria;
- V4 master plan;
- ADRs;
- backward compatibility;
- idempotency;
- provenance;
- identity safety;
- error handling;
- configuration/secrets.

Do not approve because tests are green.
Find semantic and architectural defects.
Request changes for blocking issues.
Do not perform a large hidden rewrite yourself.
```

## 26.3 QA prompt

```text
You are the independent QA/Test Agent.

Check out the exact PR commit.
Run the required tests and migration/API scenarios.
Add adversarial tests if necessary.
Test repeated ingestion when relevant.
Test failure states, not only success paths.
Verify backward compatibility.
Post the QA evidence template.
Do not approve on builder claims alone.
```

## 26.4 Data Quality prompt

```text
You are the Data Quality/Provenance Agent.

Validate representative source records against normalized DB records.
Check source attribution, temporal fields, identity links, coverage state,
completeness/partial status and absence of silent drops.
Pay special attention to false person merges and unsupported financial claims.
```

## 26.5 Release Manager prompt

```text
You are the Release Manager.

Do not merge until required independent approvals exist and CI is green.
Verify the PR commit reviewed is the commit being merged.
Check migration ordering and rollback.
Merge in dependency order.
Perform post-merge smoke checks and update docs/v4/STATUS.md.
```

---

# 27. SEVERITY AND STOP RULES

Use:

```text
P0 — data corruption, secret leak, destructive migration, identity false merge at scale
P1 — major incorrect data/API behavior, broken migration, major regression
P2 — limited bug/workaround exists
P3 — polish/documentation/non-blocking
```

Rules:

- P0: stop affected phase immediately.
- P1: no phase gate can pass.
- P2: may pass only with explicit debt issue and Orchestrator approval.
- P3: may be scheduled later.

---

# 28. ROLLBACK PRINCIPLES

Before each production-impacting phase:

- DB migrations have recovery plan;
- old JSON pipeline remains available;
- feature flags/config switches are preferred for major consumer transitions;
- API rollout does not require deleting legacy code;
- dashboard migration happens incrementally.

Never make a migration irreversible merely for convenience.

---

# 29. WHAT AGENTS MUST NOT DO

Agents must not:

- rewrite the entire repo in one PR;
- replace working parsers without tests;
- build FastAPI endpoints that just open JSON files and call the job finished;
- hardcode famous people;
- hardcode Trump-specific logic;
- treat Wikidata as authoritative financial data;
- infer private portfolios;
- silently merge people by fuzzy name;
- silently discard unparseable documents;
- silently truncate "complete" ingestion;
- commit secrets;
- use a personal email/path as production fallback;
- force-push `main`;
- merge their own substantial PR without review;
- disable tests to make CI green;
- delete legacy outputs before migration is proven;
- interpret "no record found" as "person not tracked";
- interpret prediction markets about someone as that person's investments.

---

# 30. FINAL PRODUCT BEHAVIOR

When the project is finished, an API client or AI should be able to do:

```text
Search "Person Name"
        ↓
canonical person candidates
        ↓
select person_id
        ↓
GET /coverage
        ↓
see which public sources apply and their state
        ↓
GET events / disclosures / campaign finance / news / markets
        ↓
receive real persisted data + provenance
```

If there is no financial disclosure:

```text
no_records
```

If the source does not apply:

```text
not_applicable
```

If not checked:

```text
not_checked
```

If ingestion is incomplete:

```text
partial
```

If a provider is failing:

```text
source_error
```

The system must prefer an explicit absence of evidence over an invented answer.

---

# 31. SUCCESS CONDITION FOR THE AI TEAM

The AI team is successful when it has not merely "implemented features", but has transformed WATCHDOG through a controlled sequence of independently reviewed and tested changes, all committed and merged through GitHub, with the repository itself containing enough architecture, status, migration and operational documentation for another independent AI team to continue the work safely.

The repository — not an external chat history — must become the durable source of engineering context.

Every important decision therefore ends up in:

- code;
- tests;
- ADRs;
- GitHub issues/PRs;
- migration history;
- `docs/v4/STATUS.md`.

That is the final operating model.
