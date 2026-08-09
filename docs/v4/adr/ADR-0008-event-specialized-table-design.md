# ADR-0008: Common event envelope with specialized tables

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

WATCHDOG combines trades, holdings, ownership filings, disclosures, campaign finance, news, and prediction-market information. They share time/provenance and can contain source claims about entities, but they have different meanings and required fields. Current JSON can blur these distinctions—for example, a market about a politician must not look like a position held by that politician.

## Decision

Represent one logical event identity per provider-natural fact key, with append-only factual revisions. Each immutable event revision is the common envelope for one supported source version and stores its logical event ID, revision number, optional `supersedes_revision_id`, event type, event/known/scrape dates, `revision_known_at`, `observed_at`, factual content fingerprint, source-document/parser/run lineage, confidence, and publication lifecycle reference.

Store semantic fields in typed specialized revision tables, including at minimum trades, holdings/snapshots, ownership filings, financial disclosures, campaign-finance records, news mentions, and prediction markets. Each specialized revision has a constrained one-to-one relationship with its event revision (normally the revision ID as PK/FK) and columns/constraints appropriate to its meaning. Event type and specialization must agree.

Event revisions preserve source-native person/organization/security names, provider IDs, wallet/ticker strings, claimed roles, and subject/trader distinctions as evidence. They deliberately contain no authoritative canonical target relationship. Their fingerprint includes the factual values and normalized source-native claims, but excludes canonical association status/target and canonical redirects.

The original revision has no predecessor. The same natural key plus the same factual content fingerprint is a fact-level no-op and may add only immutable re-observation/run lineage. The same natural key plus different factual content inserts a new envelope and specialization together, points to the prior revision, and never updates/deletes old values. A per-logical-fact constraint/lock makes revision numbering and supersession deterministic under concurrent ingestion. Resolving or remapping an unchanged source claim creates only a canonical association revision under ADR-0010, never an event revision.

`known_date` retains the public-known date of the underlying fact. `revision_known_at` is the earliest defensible time the exact version became knowable: use a supported provider correction-publication time, or first WATCHDOG observation for parser/system corrections with no such timestamp. `observed_at` records when WATCHDOG saw or produced the revision. Current reads choose the newest eligible revision at the latest published epoch; `as_of=T` chooses the newest revision with fact and revision known times no later than T. Thus a T2 correction cannot rewrite the result for T1.

People, aliases, roles, organizations, securities, source documents, coverage, publication units, resolution candidates, and canonical association/redirect histories are independent first-class tables, not event JSON. Holdings and reports use an event envelope for the report/snapshot's time and public-known semantics while typed rows preserve snapshot/filing detail.

JSONB is limited to provider-specific extensions or fields not yet promoted after review. Required source-claim, temporal, amount, and provenance fields are columns. An unresolved canonical association does not weaken or block persistence of the factual event revision.

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
- Corrections consume additional rows and require an effective-revision query, but preserve bitemporal auditability and anti-lookahead.
- Factual meaning, source-native claims, and sort fields cannot be edited in place; a factual change is a new event revision. Canonical linking is versioned separately and never changes the factual fingerprint.
- Some joins are required; repositories/read models hide them from routes and exporters.
- New fact types require a migration and explicit semantics rather than an arbitrary JSON payload.
- Campaign finance, personal transactions, subject mentions, and trader behavior cannot share an event type accidentally.

## Compatibility

Compatibility exporters flatten joined canonical rows back to the existing source-specific JSON shapes. No current JSON producer or consumer changes in P1.1. Legacy IDs can remain projection fields while canonical event UUIDs stay stable internally.

## Migration and rollback

Migrate one connector/fact type at a time. Persist source documents first, then establish the logical natural-key identity and insert an event revision plus specialization atomically. Resolution consumes the persisted source claim and appends a separate association decision; it never adds a canonical FK to the event. Historical imports preserve distinguishable source versions and unresolved claims; they do not collapse them into the last observed value. Reconcile each type, duplicate fingerprint, factual revision chain, association chain, and T1/T2 behavior before enabling reads or exports.

Rollback routes that connector/consumer to its legacy path and retains canonical rows for diagnosis. Schema migrations that split/promote a field must preserve original provider metadata until reconciliation proves no loss; destructive column removal requires a later cleanup gate.

## Verification

- Database constraints reject a specialization whose type does not match its event and prevent duplicate specialization rows.
- Repeated and concurrent ingestion of the same natural key/content cannot create duplicate revisions; different content creates exactly one next audited revision.
- A fixture publishes original content in T1 and corrected content in T2 for the same source key. `as_of<T2` returns the original, `as_of>=T2` returns the correction, current returns the correction, and both versions retain exact document/parser/run lineage.
- Repeating the identical T1 or T2 payload is a no-op at the event-revision layer.
- Temporal/provenance rules apply uniformly across every specialization.
- Tests prove campaign-finance and prediction-market subject records cannot be returned as personal trades/holdings.
- An unresolved source claim retains the event/document; resolving or remapping it later leaves the event revision ID/fingerprint unchanged and appends only association history.
- Schema/import tests reject authoritative canonical person/organization/security FKs on event revisions and require person filtering through the association/redirect query path.
- Query and exporter fixtures reproduce required typed semantics and compatibility shapes.
