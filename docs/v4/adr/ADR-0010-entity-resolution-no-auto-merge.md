# ADR-0010: Entity resolution never automatically merges people

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

Names are noisy and non-unique. WATCHDOG will encounter capitalization, inverted names, initials, suffixes, diacritics, aliases, homonyms, and source-specific owner strings. A false merge can attribute financial activity to the wrong public figure, which is substantially worse than temporarily leaving a record unresolved.

## Decision

Candidate discovery, canonical association, and canonical entity redirect are separate operations. The system never automatically merges two canonical people, and fuzzy/name similarity alone never automatically links a source identity or fact to a person. Event revisions retain only factual/source-native claims; **canonical association revisions are the sole authority for a fact-to-person/organization/security relationship**.

A stable canonical-association identity is keyed by:

```text
subject_scope + subject_id + semantic_role + source_claim_key + target_entity_type
```

`subject_scope` is either `logical_fact` or `event_revision` and is fixed by the connector contract; it cannot change between revisions. The connector registry has a uniqueness rule that permits exactly one subject scope for each provider fact type/source-claim key and rejects definitions that could create both identities for the same claim. `source_claim_key` identifies the stable provider claim slot such as reporting owner, issuer, candidate subject, market subject, or trader. The target UUID is excluded from the key so `unresolved -> A` and `A -> B` remain revisions of one relationship.

Each immutable association revision records association ID/revision number, nullable target UUID, status (`unresolved`, `ambiguous`, `linked`, `rejected`), typed evidence references, decision authority/rule version/actor/reason, canonical fingerprint, `supersedes_association_revision_id`, `revision_known_at`, `observed_at`, publication unit, and publication epoch. `linked` requires one target of the key's entity type; unresolved/ambiguous/rejected has no effective target. The fingerprint covers status, target, normalized evidence set, authority/rule version, and decision reason, but excludes observation time/run so exact replay is a no-op. Different content appends under a lock on the association identity. Revision number and predecessor are unique; a stale-parent concurrent writer fails/re-evaluates instead of last-write-win.

For an association or redirect, `revision_known_at` is the effective time of the exact automated/manual decision, never backdated to older source evidence; `observed_at` records when the deciding evidence/action entered WATCHDOG. A successor must have non-decreasing decision/observation time and a later publication epoch than its predecessor. This ensures a relationship decided at T2 cannot appear in `as_of=T1`, even when its source evidence was published earlier.

Resolution evidence precedence is explicit:

1. an active authenticated manual association override wins;
2. otherwise a unique verified provider identifier or later-approved deterministic rule may produce `linked` with an audit reason;
3. exact/normalized/fuzzy name evidence produces candidates only, leaving `unresolved` or `ambiguous`;
4. automated processing may add candidates/evidence but cannot supersede an active manual override. A conflicting equal-priority decision is recorded for review and does not silently change the effective target.

Canonical entity evolution uses a separate append-only redirect identity keyed by `(entity_type, source_entity_id)`. Redirect revisions contain nullable target, `active`/`reversed` status, evidence/actor/reason/fingerprint, predecessor, `revision_known_at`, `observed_at`, publication unit, and publication epoch. After selecting the effective association, queries resolve its target through the eligible redirect chain. Redirects cannot create a relationship or change its semantic role; they only canonicalize an already-linked target. Cycles and cross-type redirects are rejected, and terminal resolution is deterministic.

Current reads use the latest eligible association and redirect revisions at the latest published epoch. Public-time `as_of=T` requires each selected decision's `revision_known_at <= T`; reproducible reads additionally require `publication_epoch <= W`. A revision-scoped association is eligible only for the selected event revision, while a logical-fact-scoped association applies across eligible revisions of that fact. The effective source order is therefore: source-native event claim as evidence -> association revision as relationship authority -> redirect revision as canonical-target authority. Person-filtered endpoints and exporters use only this resolved target, deduplicate output by the selected logical fact/revision, and aggregate multiple matching role/claim decisions as lineage so one fact is never attributed twice.

Concrete transitions are append-only:

- T1/W1 `unresolved` -> T2/W2 `linked:A`: append an association revision; the event is unchanged.
- T2/W2 `linked:A` -> T3/W3 manual override `linked:B`: append a manual association revision that supersedes the link to A.
- T4/W4 merge A -> B: append an active redirect revision; eligible associations still store their historical A target but resolve to B at/after T4/W4.
- T5/W5 split/reversal: append a compensating `reversed` redirect revision so A resolves to itself again. Any subset that should remain/move elsewhere receives explicit new association revisions; no prior association or redirect is edited/deleted.

A factual source correction may append an event revision and provide new evidence, but it changes canonical membership only if a separate association revision is published. False negatives are acceptable during early migration; false-positive financial attribution is not.

## Alternatives considered

- **Auto-merge above a fuzzy threshold:** rejected because thresholds cannot safely distinguish homonyms across populations/sources.
- **Exact normalized-name auto-merge:** rejected because different people can have exactly the same name.
- **Create one canonical person per source string permanently:** safe from false merge but prevents useful verified cross-source identity; unresolved source identities are a temporary state instead.
- **Hardcoded famous-person mapping:** non-general, unauditable, and prohibited by the master plan.
- **Trust one broad knowledge provider for all identity:** no provider is authoritative for every financial/role relationship.
- **Embed authoritative canonical targets in event revisions:** rejected because factual corrections and resolution decisions have different evidence, idempotency, concurrency, and temporal lifecycles; embedding creates two authorities or needless factual revisions.
- **Mutable join table:** rejected because an override/merge could rewrite prior as-of results and cursor membership.
- **Let embedded links and association rows coexist:** rejected because endpoints/exporters could select different authorities. Event claims are evidence only and association history is authoritative.

## Consequences

- Some facts and historical actor strings remain unresolved longer, and UI/API must expose that honestly.
- Resolution requires candidate and decision/audit storage plus manual tooling.
- Verified external identities become high-value evidence and need uniqueness constraints.
- Metrics track unresolved/ambiguous rates and false-link review, not only match rate.
- Merges cannot be hidden data-cleanup side effects of ingestion.
- Query services must compose event, association, and redirect revisions under the same public/system-time boundary; this costs joins/indexes but gives one deterministic person filter.
- Manual decision runs participate in the same serialized publication clock as ingestion, so operational tooling must support staging, conflict, promotion, and compensating decisions.

## Compatibility

Legacy JSON may continue displaying source-provided actor names without claiming a canonical match. Compatibility exports must not substitute a famous canonical name when linkage is unresolved and, after migration, must use the same effective association/redirect query as the API. Existing pipeline behavior remains unchanged until source-specific migrations are reviewed.

## Migration and rollback

Historical import loads factual source claims first, creates one stable association identity per connector-defined claim slot, applies only verified deterministic matches, creates candidates, and appends explicit unresolved/ambiguous decisions for the remainder. No bulk fuzzy merge is allowed. Association identities and redirect sources are locked independently; uniqueness/fingerprint/predecessor constraints prevent duplicate revisions and forks.

Automated ingestion and authenticated manual resolution each create a `staging` publication unit. Association and redirect decisions become visible only when that unit is promoted through the same serialized publication clock as facts. Rollback before promotion deletes/retries staging only. After publication, correction or reversal is a new compensating revision; prior association/redirect rows and their evidence are never restored by update or deleted.

An incorrect link A->B is corrected by a new association revision. A merge A->B is reversed by a compensating redirect revision; a split requiring reassignment of only some facts adds per-association decisions. Read/export projections are rebuilt at a new epoch, and downstream derived artifacts are flagged for recomputation. Cursor TTL never authorizes deletion of published association/redirect history.

## Verification

- Adversarial tests cover homonyms, initials, inverted names, suffixes, diacritics, near matches, and cross-source roles.
- No fuzzy or exact-name-only score causes a canonical merge.
- Conflicting provider IDs produce ambiguous/conflict state rather than reassignment.
- Unique verified external IDs can link deterministically and record the reason.
- Schema tests prove event revisions have no authoritative canonical target; connector claim definitions cannot register both subject scopes; association/redirect keys, target/status checks, fingerprint/predecessor uniqueness, cycle/type rejection, and per-identity locking are enforced.
- Exact decision replay is a no-op; different concurrent decisions serialize or return stale-parent conflict without a silent winner. Active manual override cannot be superseded by automation.
- T1/W1 unresolved -> T2/W2 A -> T3/W3 manual B tests verify current and `as_of` selection, exact evidence/actor/run lineage, and unchanged event revision/fingerprint.
- T4/W4 merge A->B and T5/W5 split/reversal tests verify redirect precedence and compensating append-only history. Subset reassignment requires explicit association revisions and never rewrites prior rows.
- Person-A/Person-B filtered multipage tests at T1/W1 through T5/W5 prove an old cursor retains exact membership and a new cursor reflects the effective association/redirect once, with no double attribution, omission, or injection.
- Factual correction plus concurrent resolution tests prove the event and association locks/fingerprints remain independent and both become visible only through their publication units.
- Manual merge/split/override/reversal operations are authenticated, audited, time-versioned, published, and reversible by compensation.
- Data-quality review samples high-confidence, ambiguous, and unresolved cases and treats false merge as a blocking defect.
