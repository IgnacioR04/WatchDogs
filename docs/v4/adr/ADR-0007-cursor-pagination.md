# ADR-0007: Cursor/keyset pagination for ordered history

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

V4 must query growing event history while ingestion can add new records. Offset pagination becomes slower at large offsets and can duplicate or skip rows when inserts shift positions. Event dates alone are not unique, and anti-lookahead queries care about when records became known.

## Decision

Use opaque, versioned cursor/keyset pagination for large chronological API collections. The default event order is:

```text
known_date DESC, event_date DESC, id DESC
```

The UUID is a deterministic tie-breaker, not a time surrogate. Cursor membership is frozen by a PostgreSQL publication watermark, not by `created_at`, a sequence value, or a wall-clock timestamp.

Each ingestion run starts in `staging`; its documents, event revisions, specialized revisions, coverage changes, and associations are invisible to ordinary reads. Promotion uses one transaction and a singleton `publication_clock` row:

1. acquire `SELECT ... FOR UPDATE` on the clock row;
2. increment the epoch stored in that row;
3. assign that `publication_epoch` to the complete ingestion run and change its state to `published`;
4. commit while still holding the row lock.

The lock is released only by commit/rollback, so a smaller epoch cannot commit after a larger one. A failed promotion rolls back the clock update and leaves the run invisible. This must not be implemented with only `nextval()`, `created_at`, transaction start time, or an application-generated timestamp because each permits gaps or late commits that do not describe visibility order.

Database constraints require a unique, non-null epoch exactly when a run is `published`, and no epoch while it is `staging` or failed. Every response-visible revision and association is owned by a run, so provenance added by a later re-observation is also excluded from an older watermark. The locked promotion is deliberately small; source fetching and parsing occur before it in staging.

Page 1 reads the maximum committed epoch `W` and returns only rows belonging to published runs with `publication_epoch <= W`. Within that boundary and the requested public-time `as_of`, the query selects the newest eligible immutable revision for each logical fact before applying filters and order. Later pages use the same `W`, `as_of`, normalized filters/order, and lexicographic “after last row” predicate. An insertion transaction open before page 1 but promoted later receives an epoch greater than `W`; corrections and late backfills published after page 1 do too. None can enter the traversal.

All revision fields that affect membership, ordering, filtering, or meaning—including dates and canonical entity links—are immutable. A correction creates a new revision in a later published run; it never moves a row already visible at `W`. A backfill committed before page 1 is part of `W` and appears in its correct sort position; one committed later waits for a new traversal.

Cursors are opaque, integrity-protected client tokens and contain no secret or raw SQL. They encode the cursor schema version, endpoint/order identifier, publication watermark, public-time `as_of`, normalized filter fingerprint, expiry, and last sort tuple. They are not an authorization boundary; every page re-applies authorization/scope. Mismatched endpoint/filter/order/`as_of`, malformed or oversized tokens, unsupported versions, impossible/future watermarks, and expired cursors return a documented 400/410-class error. Expiry never silently substitutes a current watermark. `limit` is bounded server-side and responses return `items`, `next_cursor`, and `has_more`.

Small bounded administrative lists may use a separately documented strategy; public event history does not use unbounded offsets.

## Alternatives considered

- **Offset/limit:** simple but degrades and becomes unstable under concurrent insertion.
- **Date-only cursor:** rejected because many records share dates and would be skipped/duplicated.
- **UUID-only cursor:** UUIDv4 has no chronological meaning.
- **Database snapshot transaction held across requests:** consistent but operationally unsafe and stateful for normal HTTP pagination.
- **`created_at <= snapshot_at` or a bare sequence high-water:** rejected because a transaction can obtain the value, remain invisible to page 1, and commit between later pages.
- **Materialize every result ID set:** provides stability but creates avoidable write/storage/cleanup cost for ordinary queries; it remains an option for exceptional exports or reports.
- **Expose raw sort fields as query parameters:** leaks implementation and makes validation/versioning harder.

## Consequences

- Clients cannot jump directly to arbitrary page numbers.
- Query indexes must match endpoint filters and order; performance is verified with representative plans.
- The serialized publication clock and immutable revisions prevent late commits, corrections, and backfills from changing an existing traversal.
- Readers must join through published ingestion runs and choose the effective revision at the cursor watermark; this adds query/index complexity that integration and plan tests must cover.
- Publication is an explicit lifecycle transition. Staging cleanup, failed-run diagnosis, retry, and promotion locking need operational ownership.
- Cursor versions enable later ordering changes without silently reinterpreting old tokens.
- Endpoint-specific cursors may be needed when their canonical ordering differs.

## Compatibility

Existing static JSON arrays remain unpaginated compatibility artifacts. Cursor pagination applies to the new `/v1` API and does not alter current public file shapes.

## Migration and rollback

Introduce the publication clock/run-state constraints with persistence and pagination helpers with the API phase. Staging rows may be retried or removed only while unpublished; published epochs and the revisions they expose are retained for audit/as-of behavior. Cursor TTL limits client traversal duration, not canonical revision retention. A new cursor format increments its version and may support the prior version for a bounded period.

A failed promotion rolls back atomically and exposes nothing. Rolling back an API deploy preserves the clock, run epochs, and immutable revisions; the restored decoder either serves its supported cursor version against the same watermark or returns an explicit invalid/expired response. It never falls back to offset pagination or a newly captured epoch.

Offset pagination may exist only as a temporary, bounded, explicitly documented endpoint contract—not as silent fallback for large history.

## Verification

- Multiple rows with identical known/event dates traverse exactly once using the UUID tie-breaker.
- A transaction starts before page 1, stages an insertion, and commits/promotes after page 1; its later epoch prevents injection into all remaining pages.
- A correction published between pages changes an order/filter field through a new immutable revision; the old-watermark traversal retains the prior revision, while a new traversal selects the correction.
- A late backfill after page 1 is excluded; a backfill published before page 1 appears exactly once in its ordered position.
- Filter/order/`as_of`/endpoint changes invalidate the cursor.
- Malformed, oversized, cross-endpoint, and unsupported-version cursors fail safely.
- Expired and future/unknown-watermark cursors fail without recapturing current state.
- Property/integration tests with identical dates compare full traversal against the same watermark's ordered SQL result with no duplicates, omissions, or injections.
- Concurrency tests prove publication epochs follow commit visibility order, including rollback and two competing promoters; a bare sequence/timestamp implementation must fail the test.
- Query-plan/performance tests verify matching indexes and no large offset scan.
