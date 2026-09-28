# UPSC-RAG

A lightweight, source-of-truth and retrieval system for UPSC Civil Services Examination (CSE) 2027 preparation.

## Purpose

UPSC-RAG is not a classroom and not a software project for its own sake. It is the structured verification and retrieval layer supporting the UPSC CSE 2027 study system.

Core chain:

**Syllabus → Source of Knowledge → Source of Truth → PYQs → Current Affairs → Testing → Revision**

## Design principles

1. Accuracy first.
2. The official UPSC syllabus is the master taxonomy.
3. Primary/authoritative sources outrank secondary sources.
4. Learning books and authoritative truth are separate layers.
5. PYQs are a core relevance signal.
6. Current affairs begin formally in May 2026 and are retained only when syllabus-relevant.
7. Historical versions are preserved where UPSC-relevant.
8. Uncertainty is explicit; conflicts are not silently overwritten.
9. No vector database or paid infrastructure initially.
10. Complexity must be earned by a demonstrated retrieval problem.
11. The repository stores structured knowledge and metadata, not the user's entire book/PDF corpus.
12. Large source documents remain in the ChatGPT Project.

## Repository map

- `schema/` — machine-readable data contracts
- `taxonomy/` — UPSC master syllabus taxonomy
- `sources/` — source registry and source-of-truth records
- `pyqs/` — verified PYQ metadata and question records
- `current_affairs/` — syllabus-linked current-affairs records from May 2026 onward
- `relations/` — lightweight knowledge relationships
- `manifests/` — corpus and update manifests
- `scripts/` — validation and maintenance utilities
- `docs/` — operating rules and retrieval conventions

## Status model

Records may be:

- `VERIFIED`
- `PROVISIONAL`
- `CONFLICTING`
- `OUTDATED`
- `REQUIRES_REVIEW`

## Source hierarchy

### Tier 1 — Primary / authoritative
UPSC, Constitution, Acts/rules, Supreme Court, Government of India, RBI, Economic Survey, Union Budget, official statistics, NITI Aayog, Parliament, official international institutions and equivalent primary authorities.

### Tier 2 — Standard learning material
NCERT, Laxmikanth, Spectrum, G.C. Leong, Ramesh Singh, Ahuja, IGNOU and other established textbooks.

### Tier 3 — Academic/reference
Recognised academic publications, university material, research papers and reputable open educational resources.

### Tier 4 — Secondary/current-affairs
The Hindu, Indian Express, Business Standard, Down To Earth and other reputable journalism.

Secondary sources are primarily discovery/context sources. Important claims should be traced to Tier 1 where reasonably possible.

## Cost policy

Target recurring infrastructure cost: **₹0**.

No paid vector database, cloud server, embedding API, LLM API or scraping service is required for the initial architecture.

## Scope

The repository is intentionally small. It should help Nawaz prepare for CSE 2027, not become a separate RAG engineering project.
