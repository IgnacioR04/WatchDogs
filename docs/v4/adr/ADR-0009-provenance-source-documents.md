# ADR-0009: Mandatory provenance and source-document records

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

The product must return only supported public records and explain coverage. Today provenance varies by dataset; some derived rows omit source URLs or temporal fields, and unparseable House PDFs can disappear without a persisted filing record. A URL alone is not enough to reproduce which response/parser produced a fact, while retaining raw content is not always permitted or practical.

## Decision

Every externally derived canonical fact revision must carry:

- provider/data-source identity;
- a stable provider/source record identifier or documented deterministic substitute;
- source URL when the provider offers one;
- fetch timestamp and ingestion-run identity;
- parser/normalizer version;
- confidence plus the source-native person/organization/security claim and role actually present in the provider material;
- a link to source-document/fetch metadata when a retrievable document or API payload exists.

`source_documents` represents both traditional files and logical fetch artifacts such as an API item/page. It records source, source record ID, URL, `fetched_at`, HTTP status when applicable, content SHA-256 when computable, parser version, parse status, parse error, `requires_ocr`, and provider metadata. Raw bytes may be stored in approved object storage later; if policy/provider limits prevent retention, metadata, hash when possible, and the retention limitation remain recorded.

Document/fetch metadata is persisted before or independently of parsed canonical facts so `parse_error`, `requires_ocr`, `no_transactions`, and unsupported formats remain observable. Documents are immutable fetch observations; a refetch creates a new version/observation or preserves version history rather than overwriting evidence silently.

Canonical factual records are immutable revisions, not mutable “latest” rows. Every event revision links the exact source observation, parser/normalizer version, ingestion run, factual fingerprint, `revision_known_at`, and `observed_at` that support it. A new source observation with the same natural key and identical factual fingerprint produces no new event revision, although the re-observation remains auditable. Different factual content appends a revision with a supersession pointer; the previous envelope, specialized values, source-native claims, and lineage remain unchanged. Canonical target UUIDs and resolution status are excluded from this fingerprint and live only in the separate association history.

When a provider publishes a correction, its supported publication time becomes `revision_known_at`. When a parser/system correction changes factual interpretation without a distinct provider correction time, first observation of that interpretation is the conservative revision-known time. This prevents a T2 interpretation from appearing in a T1 public-time query.

Association and redirect revisions have their own mandatory provenance: stable relationship/redirect key, evidence references to the exact source claim/event revision or authenticated manual decision, rule/actor/reason, content fingerprint, predecessor, `revision_known_at`, `observed_at`, publication unit, and publication epoch. Derived products keep lineage to the selected event, association, and redirect revision IDs, publication watermark, and export run. They must not replace primary-source attribution with the derived artifact's URL.

## Alternatives considered

- **Store source URL only:** URLs can change and do not identify response content, fetch time, or parser behavior.
- **Store raw bytes only:** raw content without searchable metadata/status does not explain failures or relationships and may violate retention constraints.
- **Keep provenance only in logs:** logs are not relational, durable fact-level evidence and are unsuitable for API responses/reconciliation.
- **Persist only successfully parsed documents:** recreates silent data loss and false `no_records` conclusions.
- **Put all provenance in one JSONB field:** weakens required constraints and makes quality checks inconsistent.

## Consequences

- Storage and retention needs increase; policies must distinguish metadata, hashes, and raw content.
- Parser upgrades can be evaluated against immutable source observations.
- Canonical corrections and parser reinterpretations increase storage, but no later correction can replace the revision eligible at an earlier revision-known time; pinning the publication watermark additionally reproduces the complete system-visible result in the presence of late backfill.
- API clients can inspect both factual and resolution-decision provenance without accepting unsupported narrative claims.
- Parse/fetch failures contribute to partial/source-error coverage instead of disappearing.
- Sensitive or restricted raw content requires explicit access/retention controls even when its public metadata is retained.

## Compatibility

Existing `source_url` fields remain in static projections. Missing provenance in legacy inputs is reported as a migration limitation; it is not fabricated. New provenance fields are additive only under compatible/versioned contracts.

## Migration and rollback

Connector migration begins by writing document/fetch metadata, then logical fact identities and immutable factual revisions. Resolution decisions are imported/appended separately and must point to their exact source claim/evidence. Historical import maps existing source URLs/IDs/hashes and distinguishable versions where actually available, marks unknown components explicitly, and never fabricates correction/decision times. Bad records are quarantined with source lineage.

Rolling back a parser, connector, or resolver does not delete source documents, errors, event revisions, association/redirect decisions, or supersession history. Reprocessing uses retained evidence and a pinned version; a changed interpretation/decision appends another revision rather than restoring values in place. Raw-content deletion, if required by policy, keeps a tombstone/hash and reason where legally/contractually allowed.

## Verification

- Constraints require source and source-record identity for external facts and prevent duplicate document versions/natural keys.
- Fixture tests assert URL/fetch/parser/hash/status fields according to source capability.
- The same source key/content repeated is a canonical no-op, while different content appends exactly one revision linked to its predecessor and exact source/parser/run.
- T1 original/T2 correction tests prove pre-T2 as-of reads retain the original, post-T2/current reads select the correction, and both revision lineages remain independently traceable.
- Unresolved, linked, remapped, merge/split, and compensating-reversal fixtures trace every effective person result to exact event claim plus association/redirect decision lineage at the requested `as_of` and watermark.
- Failure tests persist malformed/scanned documents and set parse/error/OCR state without emitting invented events.
- API/exports expose supported provenance and never label source errors as `no_records`.
- Reprocessing tests show parser versions and prior observations remain auditable.
- Data-quality sampling traces representative API facts back to source metadata and canonical relationships.
