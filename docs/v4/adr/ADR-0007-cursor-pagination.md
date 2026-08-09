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

A publication unit is an ingestion run or an authenticated resolution-decision run. Each unit starts in `staging`; its documents, factual event/specialized revisions, canonical association/redirect revisions, coverage changes, and response-visible provenance are invisible to ordinary reads. Promotion uses one transaction and a singleton `publication_clock` row:

1. acquire `SELECT ... FOR UPDATE` on the clock row;
2. increment the epoch stored in that row;
3. assign that `publication_epoch` to the complete publication unit and change its state to `published`;
4. commit while still holding the row lock.

The lock is released only by commit/rollback, so a smaller epoch cannot commit after a larger one. A failed promotion rolls back the clock update and leaves the unit invisible. This must not be implemented with only `nextval()`, `created_at`, transaction start time, or an application-generated timestamp because each permits gaps or late commits that do not describe visibility order.

Database constraints require a unique, non-null epoch exactly when a unit is `published`, and no epoch while it is `staging` or failed. Every response-visible revision/association is owned by one unit, so provenance added by a later re-observation or manual decision is excluded from an older watermark. The locked promotion is deliberately small; source fetching, parsing, candidate scoring, and operator input occur before it in staging.

Page 1 reads the maximum committed epoch `W` and returns only rows belonging to published units with `publication_epoch <= W`. Within that boundary and public-time `as_of`, the query selects the newest eligible factual revision, then the effective canonical association revision for each stable relationship key, then the effective canonical redirect chain for its target. A revision-scoped association must reference that selected revision; a logical-fact-scoped association applies across eligible revisions. Person/entity filters operate only on the resolved target and semantic role; no event `person_id` participates. Matching association claims are aggregated as lineage and the result is deduplicated by selected logical fact/revision before keyset ordering, so multiple roles or claims cannot emit the event twice. Later pages use the same `W`, `as_of`, requested entity/role fingerprint, normalized filters/order, and lexicographic “after last row” predicate. An insertion or decision transaction open before page 1 but promoted later receives an epoch greater than `W`; factual corrections, remaps, merges/splits/reversals, and late backfills published after page 1 do too. None can enter or leave the traversal.

All factual, association, and redirect revision fields that affect membership, ordering, filtering, or meaning are immutable. A factual correction creates an event revision; a resolution change creates an association revision; an entity merge/split/reversal creates a redirect revision. Each is published in a later unit and cannot move a row already visible at `W`. A backfill committed before page 1 is part of `W` and appears in its correct sort position; one committed later waits for a new traversal.

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
- The serialized publication clock and immutable revisions prevent late commits, factual corrections, identity remaps, redirects, and backfills from changing an existing traversal.
- Readers must join through published units and choose effective fact, association, and redirect revisions at the cursor watermark; this adds query/index complexity that integration and plan tests must cover.
- Publication is an explicit lifecycle transition. Staging cleanup, failed-run diagnosis, retry, and promotion locking need operational ownership.
- Cursor versions enable later ordering changes without silently reinterpreting old tokens.
- Endpoint-specific cursors may be needed when their canonical ordering differs.

## Compatibility

Existing static JSON arrays remain unpaginated compatibility artifacts. Cursor pagination applies to the new `/v1` API and does not alter current public file shapes.

## Migration and rollback

Introduce the publication clock/unit-state constraints with persistence and pagination helpers with the API phase. Staging rows may be retried or removed only while unpublished; published epochs and all fact, association, redirect, and provenance revisions they expose are retained for audit/as-of behavior. Cursor TTL limits client traversal duration, not revision/decision/redirect retention. A new cursor format increments its version and may support the prior version for a bounded period.

A failed promotion rolls back atomically and exposes nothing. Rolling back an API deploy preserves the clock, publication-unit epochs, and immutable fact/association/redirect revisions; the restored decoder either serves its supported cursor version against the same watermark or returns an explicit invalid/expired response. It never falls back to offset pagination or a newly captured epoch.

Offset pagination may exist only as a temporary, bounded, explicitly documented endpoint contract—not as silent fallback for large history.

## Verification

- Multiple rows with identical known/event dates traverse exactly once using the UUID tie-breaker.
- A transaction starts before page 1, stages an insertion, and commits/promotes after page 1; its later epoch prevents injection into all remaining pages.
- A factual correction published between pages changes an order field through a new event revision; the old-watermark traversal retains the prior revision, while a new traversal selects the correction.
- `unresolved` at W1 becomes linked to Person A at W2, then a manual override links Person B at W3. Person-filtered multipage traversal at each watermark has stable, single membership and full decision lineage.
- Merge redirect A->B at W4 and compensating split/reversal at W5 do not change a W1-W3 traversal; a new traversal applies exactly the redirect revision eligible at its `as_of` and watermark.
- A late backfill after page 1 is excluded; a backfill published before page 1 appears exactly once in its ordered position.
- Filter/order/`as_of`/endpoint changes invalidate the cursor.
- Malformed, oversized, cross-endpoint, and unsupported-version cursors fail safely.
- Expired and future/unknown-watermark cursors fail without recapturing current state.
- Property/integration tests with identical dates compare full traversal against the same watermark's ordered SQL result with no duplicates, omissions, or injections.
- Concurrency tests prove publication epochs follow commit visibility order, including rollback, ingestion versus manual-decision promotion, and two competing promoters; a bare sequence/timestamp implementation must fail the test.
- Query-plan/performance tests verify matching indexes and no large offset scan.
