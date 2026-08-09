# ADR-0004: Separate repositories from application services

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

Today source modules commonly fetch, normalize, deduplicate, and write files in one flow, while downstream modules open those files directly. Carrying that coupling into V4 would let HTTP routes, parsers, and business rules depend on ORM details and make transaction, idempotency, and test behavior inconsistent.

## Decision

Define domain-facing repository and unit-of-work interfaces, implemented by SQLAlchemy persistence adapters. Repositories encapsulate durable access for aggregates such as Person, Alias, ExternalIdentity, Organization, Security, SourceDocument, Event, Coverage, and IngestionRun. They own persistence operations and query composition, but not provider HTTP, presentation, or cross-aggregate policy.

Application services orchestrate use cases, identity decisions, validation, transaction boundaries, coverage transitions, and calls to one or more repositories. A service opens the unit of work and decides commit/rollback behavior; repositories never commit autonomously. Read/query services return DTOs/read models rather than ORM instances.

Routes, exporters, and source adapters depend on service/query interfaces. Domain and service code do not depend on concrete SQLAlchemy classes.

## Alternatives considered

- **Active Record/ORM calls throughout the application:** concise initially, but couples policy and delivery code to session state and makes transaction ownership unclear.
- **Routes and parsers execute SQL directly:** rejected because it duplicates query/idempotency rules and bypasses testable boundaries.
- **One generic CRUD repository:** rejected because it hides domain-specific uniqueness, locking, and query semantics behind untyped operations.
- **Services that merely mirror every repository method:** rejected; services exist for use-case policy and are omitted when a read repository is sufficient.

## Consequences

- More interfaces and mapping code are required.
- Unit tests can use fakes at service boundaries, while PostgreSQL integration tests verify actual constraints and SQL behavior.
- Transaction and retry policy become visible and reviewable.
- ORM lazy-loading cannot be relied on outside a unit of work.
- Repository APIs should express domain intent (`upsert_source_record`, candidate search, timeline query) rather than leak arbitrary session access.

## Compatibility

The new layers are additive. Existing scrapers and pipeline modules continue their current file behavior until migrated one work package at a time. No big-bang wrapper or rewrite is required, and risk/portfolio code is not moved merely because the boundary exists.

## Migration and rollback

Introduce ports with the first DB/domain package, then move each connector and consumer behind them under its own issue. Keep legacy adapters callable during dual-run. If a migrated consumer regresses, route that consumer back to its prior file path while retaining the database for reconciliation.

A future persistence replacement implements the same ports. Rollback does not permit routes or parsers to bypass the repository temporarily; the legacy implementation is an explicit adapter.

## Verification

- Architecture/import tests or review show domain modules do not import FastAPI, SQLAlchemy, scraper, dashboard, or exporter modules.
- Routes and parsers contain no direct session/table access.
- Service tests cover transaction commit, rollback, partial failure, and retry policy.
- PostgreSQL repository tests cover uniqueness, concurrency, and idempotent upserts.
- Tests confirm ORM objects do not escape after session closure.
