# ADR-0010: Entity resolution never automatically merges people

- Status: **Proposed**
- Date: 2026-08-09
- Issue: [#6](https://github.com/IgnacioR04/WatchDogs/issues/6)

## Context

Names are noisy and non-unique. WATCHDOG will encounter capitalization, inverted names, initials, suffixes, diacritics, aliases, homonyms, and source-specific owner strings. A false merge can attribute financial activity to the wrong public figure, which is substantially worse than temporarily leaving a record unresolved.

## Decision

Candidate discovery and canonical merge are separate operations. The system never automatically merges two canonical people, and fuzzy/name similarity alone never automatically links a source identity or fact to a person.

Resolution evaluates evidence in this order: verified provider identity, exact canonical/alias candidates, deterministic name transformations, then fuzzy candidate generation. A source fact may be linked automatically only by a unique, verified provider identifier or another later-approved deterministic rule with equivalent evidence and an audit reason. Names alone produce candidates, not proof.

When evidence is insufficient or multiple plausible candidates exist, persist `unresolved` or `ambiguous` state plus candidate scores/reasons. The source record/document remains available. A canonical merge, split, or override requires an authenticated explicit decision, reason, actor, timestamp, supporting evidence, and reversible audit trail. Manual decisions override future candidate scoring without erasing original source strings.

False negatives are acceptable during early migration; false-positive financial attribution is not.

## Alternatives considered

- **Auto-merge above a fuzzy threshold:** rejected because thresholds cannot safely distinguish homonyms across populations/sources.
- **Exact normalized-name auto-merge:** rejected because different people can have exactly the same name.
- **Create one canonical person per source string permanently:** safe from false merge but prevents useful verified cross-source identity; unresolved source identities are a temporary state instead.
- **Hardcoded famous-person mapping:** non-general, unauditable, and prohibited by the master plan.
- **Trust one broad knowledge provider for all identity:** no provider is authoritative for every financial/role relationship.

## Consequences

- Some facts and historical actor strings remain unresolved longer, and UI/API must expose that honestly.
- Resolution requires candidate and decision/audit storage plus manual tooling.
- Verified external identities become high-value evidence and need uniqueness constraints.
- Metrics track unresolved/ambiguous rates and false-link review, not only match rate.
- Merges cannot be hidden data-cleanup side effects of ingestion.

## Compatibility

Legacy JSON may continue displaying source-provided actor names without claiming a canonical match. Compatibility exports must not substitute a famous canonical name when linkage is unresolved. Existing pipeline behavior remains unchanged until source-specific migrations are reviewed.

## Migration and rollback

Historical import loads raw identities first, applies verified external matches, creates candidates, and leaves the remainder unresolved. No bulk fuzzy merge is allowed. Merge/split tooling updates references transactionally while preserving supersession and decision history.

An incorrect link or manual merge can be reversed using the audit record: restore distinct canonical IDs/source links, rebuild affected read/export projections, and flag downstream derived artifacts for recomputation. Evidence and original values are never deleted during reversal.

## Verification

- Adversarial tests cover homonyms, initials, inverted names, suffixes, diacritics, near matches, and cross-source roles.
- No fuzzy or exact-name-only score causes a canonical merge.
- Conflicting provider IDs produce ambiguous/conflict state rather than reassignment.
- Unique verified external IDs can link deterministically and record the reason.
- Manual merge/split/override operations are authenticated, audited, and reversible.
- Data-quality review samples high-confidence, ambiguous, and unresolved cases and treats false merge as a blocking defect.
