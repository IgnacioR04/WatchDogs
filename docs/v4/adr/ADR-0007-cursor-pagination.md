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

The UUID is a deterministic tie-breaker, not a time surrogate. The first response captures a database `snapshot_at` boundary. Its cursor encodes at least a schema/version marker, snapshot boundary, normalized filter/order fingerprint, and last sort tuple. Later pages repeat the same filters, enforce `created_at <= snapshot_at`, and apply lexicographic “after last row” predicates.

Cursors are opaque client tokens, strictly decoded/validated, and contain no secret or raw SQL. They are not an authorization boundary; every page re-applies authorization/scope. Mismatched filters, malformed data, unsupported versions, or expired retention policy return a documented 400-class error. `limit` is bounded server-side and responses return `items`, `next_cursor`, and `has_more`.

Small bounded administrative lists may use a separately documented strategy; public event history does not use unbounded offsets.

## Alternatives considered

- **Offset/limit:** simple but degrades and becomes unstable under concurrent insertion.
- **Date-only cursor:** rejected because many records share dates and would be skipped/duplicated.
- **UUID-only cursor:** UUIDv4 has no chronological meaning.
- **Database snapshot transaction held across requests:** consistent but operationally unsafe and stateful for normal HTTP pagination.
- **Expose raw sort fields as query parameters:** leaks implementation and makes validation/versioning harder.

## Consequences

- Clients cannot jump directly to arbitrary page numbers.
- Query indexes must match endpoint filters and order; performance is verified with representative plans.
- A snapshot boundary prevents new inserts appearing midway through traversal. Updates to ordering fields should be rare/audited; immutable revision/history design is preferred for corrections.
- Cursor versions enable later ordering changes without silently reinterpreting old tokens.
- Endpoint-specific cursors may be needed when their canonical ordering differs.

## Compatibility

Existing static JSON arrays remain unpaginated compatibility artifacts. Cursor pagination applies to the new `/v1` API and does not alter current public file shapes.

## Migration and rollback

Introduce pagination helpers and contract tests with the API phase. A new cursor format increments its version and may support the prior version for a bounded period. Rolling back the API deploy restores its prior cursor decoder/queries; clients receive an explicit invalid/expired cursor error rather than incorrect data.

Offset pagination may exist only as a temporary, bounded, explicitly documented endpoint contract—not as silent fallback for large history.

## Verification

- Multiple rows with identical known/event dates traverse exactly once using the UUID tie-breaker.
- Inserts between page requests do not duplicate, skip, or inject rows into the captured snapshot.
- Filter/order changes invalidate the cursor.
- Malformed, oversized, cross-endpoint, and unsupported-version cursors fail safely.
- Property/integration tests compare full cursor traversal with the same snapshot's ordered SQL result.
- Query-plan/performance tests verify matching indexes and no large offset scan.
