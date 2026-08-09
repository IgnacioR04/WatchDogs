# ADR-0003: UUID canonical identity with Person at the center

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

Current records identify actors with provider strings, CIKs, wallet addresses, tickers, or deterministic event hashes. The same person can have many name forms and provider IDs, while two people can share the same name. Provider identifiers also differ by role and can change or be absent. None is a safe cross-source canonical key.

## Decision

Use immutable UUID primary keys for canonical `Person`, `Organization`, `Security`, source document, event, coverage-run, and other aggregate identities. UUIDv4 is the initial generation strategy because it is provider-independent and available before persistence; changing UUID generation strategy later must not change existing IDs.

Model identity person-centrically:

- names and normalized aliases are separate records linked to `person_id`;
- provider identifiers are typed external-identity records with provider-scoped uniqueness and evidence;
- roles connect people to organizations and time ranges;
- securities and organizations have their own UUID identities; ticker and CIK are attributes/external IDs, not primary keys;
- source facts may remain unlinked when the person is unresolved or ambiguous;
- a wallet/trader identity and a prediction-market subject relationship are distinct.

UUIDs identify canonical records; provider-natural keys still enforce ingestion idempotency.

## Alternatives considered

- **Canonical name as key:** rejected because names are mutable, non-unique, localized, and inconsistently formatted.
- **One provider ID such as SEC CIK or Wikidata QID:** rejected because no provider covers all entity classes and a provider ID is not authoritative across every domain.
- **Auto-increment integer:** technically viable, but less suitable for independently ingested records and external-safe identifiers; it also invites accidental exposure of row ordering.
- **Deterministic UUID derived from normalized name:** rejected because it encodes the same unsafe name-equality assumption and cannot handle homonyms safely.

## Consequences

- Joins and indexes are wider than integer keys, but IDs are stable across APIs and ingestion workers.
- APIs expose canonical UUIDs and preserve provider IDs as attributed evidence.
- Identity merges/splits need audited operations; changing display names never changes identity.
- Unresolved records are expected and preferable to false links.
- Legacy event IDs and provider keys can remain in compatibility exports even when a canonical UUID is added later.

## Compatibility

Existing JSON identifiers, filenames, and fields are not replaced during additive migration. A canonical UUID may be added only where a versioned contract permits it. Export mappings preserve legacy IDs/shapes until P8 compatibility approval.

## Migration and rollback

Historical import creates canonical UUIDs only after verified/deterministic linkage; unresolved actor strings remain source-linked records or candidates. Merges preserve an audit trail and redirect/supersession information rather than reusing an ID for another person.

Rollback of a consumer cutover restores the legacy identifier view. Canonical UUID assignments and manual identity evidence are retained; rolling back must not recreate new UUIDs for the same canonical row.

## Verification

- Database tests prove UUID primary/FK behavior and provider-scoped external-ID uniqueness.
- Homonym and alias tests show that equal/similar names do not imply equal UUIDs.
- Repeated source ingestion resolves to the same canonical record when verified evidence is unchanged.
- API contract tests use canonical UUIDs while compatibility snapshots preserve required legacy IDs.
- Merge/split/manual-override tests preserve audit history and references.
