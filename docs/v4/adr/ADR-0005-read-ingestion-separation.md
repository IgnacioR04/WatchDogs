# ADR-0005: Separate query reads from ingestion

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

WATCHDOG sources have independent latency, availability, rate limits, pagination, and parsing failure modes. A person query that synchronously fans out to SEC, Congress, FEC, OGE, Wikidata, GDELT, or market providers would be slow, nondeterministic, hard to secure, and unable to distinguish provider failure from a genuine absence of records.

## Decision

Use two explicit execution paths:

1. scheduled or authenticated manual ingestion discovers/fetches/parses sources and writes PostgreSQL, source-document, coverage, and ingestion-run state;
2. ordinary API/query requests read persisted PostgreSQL state only.

An ordinary GET cannot fetch a provider, invoke a scraper, mutate coverage, or start ingestion as a side effect. Administrative refresh/run endpoints are authenticated commands: they validate scope, create or dispatch an ingestion run, and return a durable run identifier/status. They do not disguise a live provider fan-out as a query response.

The initial scheduler/worker implementation can remain simple and process-based. A queue or Redis requires a later evidence-backed decision.

## Alternatives considered

- **Fetch on cache miss:** rejected because a read's meaning and latency would depend on external availability, and failures could be mistaken for `no_records`.
- **Always fan out in parallel during search:** rejected for provider etiquette, cost, timeout, provenance, and repeatability reasons.
- **One combined service method for query/refresh:** rejected because authorization and transaction semantics become ambiguous.
- **Adopt a distributed queue immediately:** premature without throughput/reliability evidence; the separation does not depend on queue technology.

## Consequences

- Queries may return stale/not-checked coverage rather than silently refreshing; the response can explain freshness and expose an authorized refresh workflow.
- API latency and availability are isolated from providers and parser failures.
- Ingestion needs scheduling, checkpoints, retries, and observable runs.
- Read replicas/caching can be introduced later without changing ingestion contracts.
- Administrative commands have a larger attack surface and require auth, validation, rate control, and audit logs.

## Compatibility

Existing CLI/workflow scraping continues while migration is additive. This ADR constrains the new V4 API, not the current batch entry points. The dashboard remains on static files until its planned incremental migration.

## Migration and rollback

Build persisted ingestion and coverage before enabling `/v1` reads. During dual-run, legacy scheduled jobs and V4 ingestion can run independently with reconciliation; avoid uncoordinated dual writes to one canonical fact.

If the new query path fails, disable it or restore consumers to the legacy static path. Provider ingestion can be paused without making the API execute live scrapers; reads report stale/source-error state based on persisted evidence.

## Verification

- Unit/architecture tests fail if query routes import or invoke provider clients/scrapers.
- API tests use no network and return persisted coverage states deterministically.
- Admin endpoints require authentication and return an ingestion run identifier.
- Provider timeouts and parser errors produce run/coverage state without changing a read into `no_records`.
- Load tests show query latency does not scale with the number of external providers.
