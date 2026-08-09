# ADR-0006: Generate static JSON through a compatibility exporter

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

`data/public/*` and four legacy `data/*.json` files are real public contracts used by the dashboard, pipeline modules, and potentially unknown external clients. They cannot be deleted during database migration. P0 also found cross-run timestamps/counts because the current publication sequence is not one atomic logical snapshot.

## Decision

After the database and migrated connectors are trusted, produce existing static contracts through a dedicated, read-only exporter:

```text
PostgreSQL -> export query/read models -> versioned projection mapping
           -> staged snapshot -> atomic publication of data/public/*
```

The exporter preserves required filenames, shapes, nested fields, rolling-window/top-N behavior, and public URLs until explicit versioned deprecation. Bounded projections state their window/preview/partial semantics and are never presented as complete canonical history.

One export receives a snapshot/export run identifier and database high-water mark. Files are staged and validated; payloads become visible together as far as the deployment medium permits, with manifest/latest published last and referencing the same lineage. Export code does not become a second business-rule implementation, and the V4 API never reads its output.

## Alternatives considered

- **Remove JSON when the API launches:** rejected because known and unknown compatibility consumers would break.
- **Continue letting each scraper own public files indefinitely:** rejected because it preserves multiple truths, cross-run inconsistency, and coupled publication logic.
- **Have API routes read JSON:** rejected by the PostgreSQL source-of-truth decision and prevents historical/canonical querying.
- **Change all shapes to the new domain model immediately:** rejected; compatibility changes require versioning, consumer migration, and their own gate.

## Consequences

- Projection mappings and snapshot/contract fixtures become maintained code.
- Some canonical detail is intentionally omitted from compatibility views; consumers needing full history use the API.
- Exports can remain GitHub Pages artifacts and bot commits, but generated-data noise stays separate from feature diffs.
- Atomicity and lineage improve, though publication medium limits must be documented honestly.
- Export failure leaves the last known-good complete snapshot in place.

## Compatibility

During P1–P7, the current producers remain authoritative for legacy outputs. P8.1 owns exporter implementation and must compare exact filenames, key shapes, nested structures, semantics, and important consumers documented in `PUBLIC_CONTRACT.md`.

## Migration and rollback

Run the DB exporter in shadow mode, compare results, then cut over one artifact group only after approval. Retain the previous producer/configuration and last known-good artifacts for immediate rollback. A rollback switches publication source; it does not make static JSON canonical or delete database facts.

Legacy files are removed only in P11 after evidence shows no consumer depends on them.

## Verification

- Snapshot/contract tests protect every documented public artifact and nested structure.
- Repeated export from the same DB snapshot is byte-stable apart from explicitly versioned metadata.
- Window/top-N/partial semantics and source provenance survive projection.
- Failure injection proves incomplete staged output does not replace the prior snapshot.
- Manifest, latest, and payloads share an export-run lineage/high-water mark.
- Dashboard and critical pipeline regression tests pass against DB-generated fixtures.
