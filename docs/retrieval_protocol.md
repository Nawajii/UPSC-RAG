# UPSC-RAG Retrieval Protocol

## Objective
Turn UPSC-RAG into a usable Source-of-Truth and UPSC-relevance engine.

## Query pipeline
1. Resolve the query to one or more syllabus IDs.
2. Retrieve Source-of-Knowledge material for explanation.
3. Retrieve the highest-authority verified Source-of-Truth material.
4. Retrieve relevant PYQs.
5. Retrieve relevant current affairs from May 2026 onward.
6. Cross-check important factual/current/legal claims.
7. Detect conflicts and preserve competing claims with dates and authority.
8. Produce an adaptive answer.

## Retrieval priority
Factual/current/legal: Tier 1 verified primary source -> Tier 1 cross-check -> Tier 2 explanation -> Tier 3/4 context.
Conceptual teaching: Source of Knowledge -> Source of Truth for definitions/current facts -> PYQs -> current examples.
UPSC-pattern query: PYQs -> recurring themes -> syllabus mapping -> Source of Knowledge -> Source of Truth -> current-affairs linkage.
Current affairs: official development -> primary document -> cross-check -> syllabus mapping -> PYQ linkage -> Prelims/Mains implications.

## Adaptive output
Simple query: answer + authoritative source + syllabus connection.
Topic query: explanation + knowledge source + truth source + relevant PYQs + current affairs.
Broad research: concepts + evidence + changed/competing positions + PYQs + recurring themes + current affairs + Prelims traps + Mains dimensions + Optional linkage.

## Verification rules
Never convert a search snippet into a fact, a news report into a primary fact when the primary source exists, a textbook statement into a current fact, an institution domain into a verified document, or model inference into an official position.

If sources conflict: state the claims, identify sources and dates, prefer the more authoritative/current source, explain the difference when known, and mark unresolved conflicts as CONFLICTING.

## PYQ rule
PYQs define UPSC relevance. A source without PYQ evidence may still matter, but should not be presented as established UPSC priority merely because it exists.

## Current-affairs rule
Formal current-affairs retention starts May 2026. Store only syllabus-linked developments. Do not build a generic news archive.

## Retrieval modes
LEARN | VERIFY | PYQ | CURRENT | PRELIMS | MAINS | OPTIONAL | REVISION

## Example
Query: Explain fiscal deficit.
Resolve to the relevant GS-III economy and Economics Optional Paper-II nodes, plus Prelims economy where applicable.
Retrieve the relevant knowledge source, Budget/Economic Survey/DEA/RBI evidence, fiscal-deficit PYQs, and relevant developments since May 2026.
Then generate the requested learning or testing format.

## Core principle
The system is not trying to retrieve the most documents. It is trying to retrieve the smallest authoritative evidence set sufficient to answer the UPSC question correctly.
