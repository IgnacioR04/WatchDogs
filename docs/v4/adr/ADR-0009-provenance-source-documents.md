# ADR-0009: Mandatory provenance and source-document records

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

The product must return only supported public records and explain coverage. Today provenance varies by dataset; some derived rows omit source URLs or temporal fields, and unparseable House PDFs can disappear without a persisted filing record. A URL alone is not enough to reproduce which response/parser produced a fact, while retaining raw content is not always permitted or practical.

## Decision

Every externally derived canonical fact must carry:

- provider/data-source identity;
- a stable provider/source record identifier or documented deterministic substitute;
- source URL when the provider offers one;
- fetch timestamp and ingestion-run identity;
- parser/normalizer version;
- confidence and the supported relationship to person/organization/security;
- a link to source-document/fetch metadata when a retrievable document or API payload exists.

`source_documents` represents both traditional files and logical fetch artifacts such as an API item/page. It records source, source record ID, URL, `fetched_at`, HTTP status when applicable, content SHA-256 when computable, parser version, parse status, parse error, `requires_ocr`, and provider metadata. Raw bytes may be stored in approved object storage later; if policy/provider limits prevent retention, metadata, hash when possible, and the retention limitation remain recorded.

Document/fetch metadata is persisted before or independently of parsed canonical facts so `parse_error`, `requires_ocr`, `no_transactions`, and unsupported formats remain observable. Documents are immutable fetch observations; a refetch creates a new version/observation or preserves version history rather than overwriting evidence silently.

Derived products keep lineage to their canonical input IDs/export run. They must not replace primary-source attribution with the derived artifact's URL.

## Alternatives considered

- **Store source URL only:** URLs can change and do not identify response content, fetch time, or parser behavior.
- **Store raw bytes only:** raw content without searchable metadata/status does not explain failures or relationships and may violate retention constraints.
- **Keep provenance only in logs:** logs are not relational, durable fact-level evidence and are unsuitable for API responses/reconciliation.
- **Persist only successfully parsed documents:** recreates silent data loss and false `no_records` conclusions.
- **Put all provenance in one JSONB field:** weakens required constraints and makes quality checks inconsistent.

## Consequences

- Storage and retention needs increase; policies must distinguish metadata, hashes, and raw content.
- Parser upgrades can be evaluated against immutable source observations.
- API clients can inspect provenance without accepting unsupported narrative claims.
- Parse/fetch failures contribute to partial/source-error coverage instead of disappearing.
- Sensitive or restricted raw content requires explicit access/retention controls even when its public metadata is retained.

## Compatibility

Existing `source_url` fields remain in static projections. Missing provenance in legacy inputs is reported as a migration limitation; it is not fabricated. New provenance fields are additive only under compatible/versioned contracts.

## Migration and rollback

Connector migration begins by writing document/fetch metadata, then parsed facts. Historical import maps existing source URLs/IDs/hashes where actually available and marks unknown components explicitly. Bad records are quarantined with source lineage.

Rolling back a parser or connector does not delete source documents or errors. Reprocessing uses the retained artifact/metadata and a pinned parser version. Raw-content deletion, if required by policy, keeps a tombstone/hash and reason where legally/contractually allowed.

## Verification

- Constraints require source and source-record identity for external facts and prevent duplicate document versions/natural keys.
- Fixture tests assert URL/fetch/parser/hash/status fields according to source capability.
- Failure tests persist malformed/scanned documents and set parse/error/OCR state without emitting invented events.
- API/exports expose supported provenance and never label source errors as `no_records`.
- Reprocessing tests show parser versions and prior observations remain auditable.
- Data-quality sampling traces representative API facts back to source metadata and canonical relationships.
