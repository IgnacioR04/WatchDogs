# ADR-0001: PostgreSQL as the V4 source of truth

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

WATCHDOG currently persists public results as generated JSON. Those files support GitHub Pages, the dashboard, intelligence steps, and unknown external consumers, but they provide no transactional constraints, canonical person identity, complete history, reliable cross-artifact lineage, or queryable coverage state. P0 also found non-atomic publication and partial datasets whose limits are not consistently represented.

The V4 API requires canonical, historical, relational queries with auditable provenance and idempotent ingestion. The existing pipeline must continue to work while that path is proven.

## Decision

PostgreSQL will be the canonical store for V4 people, identities, organizations, securities, source documents, factual event/specialized revisions, canonical association/redirect histories, coverage, and publication units. Once the relevant persistence and API gates pass, every `/v1` query reads canonical state through repositories backed by PostgreSQL; it does not read `data/public/*.json`.

During additive migration, the current JSON pipeline remains authoritative for its existing consumers. New ingestion is verified in PostgreSQL without silently changing legacy output. After reconciliation and compatibility approval, static artifacts are generated as projections from PostgreSQL. A dual-run discrepancy is recorded and investigated rather than resolved by an implicit last writer.

## Alternatives considered

- **Keep JSON as canonical storage:** rejected because transactions, constraints, joins, concurrency, history, and coverage queries would have to be reimplemented poorly.
- **SQLite:** useful for small local tools, but not selected as production truth because expected concurrent ingestion/query workloads and PostgreSQL-specific search/indexing are part of the target.
- **Document database:** flexible payloads do not outweigh the need for relational identity, uniqueness, provenance, and typed cross-source relationships.
- **Event stream/object storage as the only truth:** valuable as raw retention, but insufficient alone for the required query model and current operational scope.

## Consequences

- Database availability and operations become production requirements.
- Schema migrations, backups, restore tests, connection management, and query performance require explicit ownership.
- Database constraints can enforce source-natural uniqueness and temporal/relationship integrity.
- Raw/provider extensions may still use JSONB selectively, but canonical relationships remain relational.
- Generated JSON can no longer be treated as a complete backup or canonical reconciliation source.

## Compatibility

This decision is additive until later gates. `run_all.py`, `run_pipeline.py`, the hourly workflow, existing public paths, JSON shapes, dashboard, and intelligence consumers remain unchanged. Unknown external clients retain the current files until an explicit, tested deprecation.

## Migration and rollback

1. Add migrations and repositories without switching consumers.
2. Ingest/reconcile representative and historical data into PostgreSQL.
3. Activate PostgreSQL-backed `/v1` reads behind a reversible deployment/configuration boundary.
4. Dual-run and compare the DB-backed exporter with current artifacts before cutover.
5. Retain the old pipeline until the observation and cleanup gates pass.

Rollback disables the new read/export route and restores the last known-good legacy path. Database rollback uses backups, reviewed migration recovery, or a forward fix; no rollout may depend solely on a lossy downgrade. Canonical DB state is retained for diagnosis.

## Verification

- An empty PostgreSQL instance migrates to Alembic head.
- Repository and repeated-ingestion tests prove constraints and idempotency.
- `/v1` tests fail if code attempts to read static JSON.
- Reconciliation reports counts, duplicates, unresolved identities, date ranges, partial reasons, and lineage.
- Backup/restore and consumer rollback procedures are exercised before production cutover.
