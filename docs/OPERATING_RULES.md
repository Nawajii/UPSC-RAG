# UPSC-RAG Operating Rules

## 1. Master index

Every retained knowledge record should map to the official UPSC syllabus wherever a meaningful mapping exists.

The syllabus determines scope. A source does not create scope merely because it contains interesting material.

## 2. Source of Knowledge vs Source of Truth

**Source of Knowledge:** material selected to teach a concept.

**Source of Truth:** authoritative evidence used to verify what is correct, current or officially established.

Books are learning benchmarks. Primary institutions establish authoritative/current facts.

## 3. Verification

Important claims should be verified against the highest available authority, especially:

- statistics
- constitutional/legal claims
- government policy and schemes
- RBI decisions
- court judgments
- economic data
- international commitments
- rankings and indices
- scientific claims
- disputed historical claims
- dates and institutional facts

A source saying X is not itself equivalent to X being established fact.

## 4. Conflicts

Never silently overwrite a meaningful conflict.

Record competing claims, sources, dates, authority, historical context and current status. The final retrieval layer should distinguish:

- source-reported claim
- established/authoritative fact
- unresolved disagreement

## 5. Versioning

Preserve historical versions when a change could affect UPSC understanding, especially laws, schemes, RBI policy, statistics, regulations, international agreements and institutional structures.

## 6. Current affairs

Formal current-affairs coverage starts **May 2026**.

A current-affairs item is retained only if it materially improves UPSC preparation and can be connected to the static syllabus.

Preferred chain:

EVENT → STATIC TOPIC → SOURCE OF TRUTH → PRELIMS → MAINS → OPTIONAL (if applicable) → PYQ → POSSIBLE QUESTION

## 7. PYQs

Actual UPSC questions must never be mixed with generated questions.

PYQ records should preserve their official provenance. Analytical fields such as difficulty and concept classification are explicitly our analysis, not UPSC classifications.

## 8. Retrieval

Retrieval should be adaptive.

Simple factual query:
authoritative fact + strongest source.

Research/knowledge-map query:
facts + learning sources + source of truth + PYQs + current affairs + UPSC relevance.

## 9. No premature vector RAG

Use structured metadata, IDs, tags and full-text search first.

Introduce embeddings/vector search only after documenting a concrete retrieval failure that structured retrieval cannot reasonably solve.

## 10. Quality gates

Before a record becomes VERIFIED:

- source identity is known
- provenance is recorded
- relevant date/version is recorded where applicable
- syllabus mapping is valid
- factual claims have appropriate authority
- conflicts are represented where material

## 11. Time discipline

Do not expand preparation merely because additional documents exist. The useful question is:

> Does this materially improve the probability of answering a UPSC question correctly?

If not, exclude it.
