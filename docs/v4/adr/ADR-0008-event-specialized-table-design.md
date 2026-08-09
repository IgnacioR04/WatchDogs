# ADR-0008: Common event envelope with specialized tables

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

WATCHDOG combines trades, holdings, ownership filings, disclosures, campaign finance, news, and prediction-market information. They share time, provenance, and entity links but have different meanings and required fields. Current JSON can blur these distinctions—for example, a market about a politician must not look like a position held by that politician.

## Decision

Use an `events` table as the common envelope for time-addressable externally supported facts. It stores canonical person/organization/security links where known, event type, event/known/scrape dates, optional direction and amount range, source-natural identity, source-document link, confidence, and lifecycle timestamps.

Store semantic fields in typed specialized tables, including at minimum trades, holdings/snapshots, ownership filings, financial disclosures, campaign-finance records, news mentions, and prediction markets. Each specialized row has a constrained one-to-one event relationship (normally `event_id` as PK/FK) and columns/constraints appropriate to its meaning. Event type and specialization must agree.

People, aliases, roles, organizations, securities, source documents, coverage, ingestion runs, and resolution candidates are independent first-class tables, not event JSON. Holdings and reports use an event envelope for the report/snapshot's time and public-known semantics while typed rows preserve snapshot/filing detail.

JSONB is limited to provider-specific extensions or fields not yet promoted after review. Required query, identity, temporal, amount, and provenance fields are columns. Nullable entity links allow unresolved facts to survive without weakening provenance.

## Alternatives considered

- **One giant event table:** produces many unrelated nullable columns and weak type-specific constraints.
- **One generic event plus all details in JSONB:** flexible but hides schema, breaks efficient validation/querying, and encourages semantic conflation.
- **Only independent specialized tables:** duplicates temporal/provenance logic and makes a unified person timeline difficult.
- **One table per provider:** couples the canonical model to source layouts and prevents cross-source semantics.
- **ORM inheritance as the primary design:** adds mapping complexity without replacing explicit relational constraints.

## Consequences

- Unified timelines and shared anti-lookahead/provenance checks use the event envelope.
- Specialized queries remain typed and can have targeted indexes/constraints.
- Inserting a fact generally touches an event and specialization in one transaction.
- Some joins are required; repositories/read models hide them from routes and exporters.
- New fact types require a migration and explicit semantics rather than an arbitrary JSON payload.
- Campaign finance, personal transactions, subject mentions, and trader behavior cannot share an event type accidentally.

## Compatibility

Compatibility exporters flatten joined canonical rows back to the existing source-specific JSON shapes. No current JSON producer or consumer changes in P1.1. Legacy IDs can remain projection fields while canonical event UUIDs stay stable internally.

## Migration and rollback

Migrate one connector/fact type at a time. Persist source documents first, then insert event and specialization atomically using a provider-natural unique key. Reconcile each type against current output/history before enabling its reads or exports.

Rollback routes that connector/consumer to its legacy path and retains canonical rows for diagnosis. Schema migrations that split/promote a field must preserve original provider metadata until reconciliation proves no loss; destructive column removal requires a later cleanup gate.

## Verification

- Database constraints reject a specialization whose type does not match its event and prevent duplicate specialization rows.
- Repeated and concurrent ingestion cannot create duplicate source facts.
- Temporal/provenance rules apply uniformly across every specialization.
- Tests prove campaign-finance and prediction-market subject records cannot be returned as personal trades/holdings.
- Unresolved person links retain the source fact/document and can be linked later without changing source identity.
- Query and exporter fixtures reproduce required typed semantics and compatibility shapes.
