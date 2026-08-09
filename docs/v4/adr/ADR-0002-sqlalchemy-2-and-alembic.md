# ADR-0002: SQLAlchemy 2 and Alembic for persistence

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

The repository has no database package or migration framework. V4 needs explicit transactions, portable testable repositories, PostgreSQL types and constraints, and a durable record of schema evolution. The current pipeline is synchronous and there is no measured need for two database access modes.

## Decision

Use SQLAlchemy 2.x declarative mappings and 2.x query/session APIs with the PostgreSQL psycopg driver. Begin with synchronous `Session` usage and explicit unit-of-work transaction scopes; do not mix synchronous and asynchronous persistence paths without a later ADR supported by measurements.

Alembic is the only production schema-evolution mechanism. Application startup must not call `metadata.create_all()` as a substitute for migrations. Revisions use deterministic names for important constraints/indexes, are reviewed with their models, and support upgrading an empty database to head.

ORM models stay inside the persistence adapter. Domain DTOs, API schemas, and parser outputs are separate types.

## Alternatives considered

- **Raw SQL only:** can express PostgreSQL fully, but would duplicate mapping/session patterns and make broad repository evolution more costly.
- **Django ORM:** rejected because WATCHDOG is not a Django application and should not adopt that framework solely for persistence.
- **SQLModel:** convenient for small APIs but couples validation/API and persistence models more tightly than the selected boundaries allow.
- **Automatic schema creation or handwritten migration scripts:** lacks a consistent ordered revision graph and reliable empty-to-head testing.
- **Async SQLAlchemy from day one:** adds lifecycle and test complexity without current load evidence; it can be reconsidered behind repository ports.

## Consequences

- P1.2 must constrain compatible SQLAlchemy, Alembic, psycopg, and test dependencies.
- Session ownership and transaction boundaries must be explicit in services and tests.
- Developers must avoid legacy SQLAlchemy APIs and prevent ORM objects from leaking across boundaries.
- PostgreSQL-specific behavior is accepted where it supports correctness, including UUID, JSONB, indexes, and search extensions.
- Migration review becomes a required part of schema changes.

## Compatibility

No current scraper, pipeline, or static consumer imports SQLAlchemy. The new package is additive. Legacy JSON execution remains usable without a database until the separately scoped transition says otherwise.

## Migration and rollback

Start with an Alembic baseline for a fresh V4 schema; do not stamp an unverified pre-existing schema. Each production migration documents data risk, forward recovery, and whether downgrade is lossless. Downgrade is exercised on disposable/test databases where supported. Production recovery prefers a forward correction or tested backup restore when a downgrade would destroy data.

Removing the V4 persistence path does not require removing legacy files or commands. Repository ports isolate a future driver/access-mode change.

## Verification

- Dependency checks confirm supported SQLAlchemy 2/Alembic/psycopg versions.
- CI upgrades a fresh PostgreSQL database from base to head.
- Migration rerun is safe and the revision graph has one expected head.
- Lifecycle tests cover commit, rollback, connection cleanup, FK behavior, uniqueness, and at least one supported downgrade/recovery scenario.
- Static checks or review confirm routes/parsers do not import ORM models directly.
