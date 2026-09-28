# UPSC-RAG Source Registry

## Purpose

This registry is the Source of Truth layer of UPSC-RAG.

It is intentionally separate from the conventional book corpus, which remains the Source of Knowledge.

## Source hierarchy

1. UPSC / Constitution / Acts / Courts / Parliament / constitutional bodies
2. Union ministries, departments, regulators and statutory bodies
3. Official Indian government datasets and statistics
4. Authoritative international organisations
5. Selected research institutions and policy organisations
6. Books and coaching material — Source of Knowledge, not default Source of Truth

## Registry status — 28 September 2026

- 175 source institutions
- 875 source-family records
- 195 records directly verified during this build
- 680 records marked REQUIRES_REVIEW
- 0 unresolved records are silently discarded

The registry deliberately exceeds the original 400+ target because the source model records both institutions and their major source families:

- reports
- statistics
- laws/notifications
- policy/programmes
- current updates

A source-family record is not a claim that a separate URL exists for every family. Retrieval must descend into the institution's actual publication/data/document page.

## Verification rule

VERIFIED means the official source/domain was directly established from authoritative web evidence during the build.

REQUIRES_REVIEW means the candidate belongs in the source architecture but has not yet received sufficient direct verification.

REQUIRES_REVIEW sources must not be silently promoted to Source of Truth.

## Discovery backbone

The Integrated Government Online Directory (IGOD) is the discovery backbone for Indian government websites.

## Current implementation

- sources/source_registry.json — master registry
- sources/unresolved_sources.json — explicit verification queue
- sources/upsc_official.json — UPSC baseline source
- taxonomy/master_index.json — syllabus taxonomy
- pyqs/paper_index.json — PYQ provenance index

## Retrieval rule

When answering a UPSC question:

retrieve → prefer highest-authority verified source → cross-check important claims → record conflicts → cite the actual source.

Books may explain a concept, but they do not override an authoritative primary source when the question concerns current facts, law, policy, statistics or institutional position.

## Next maintenance rule

When a REQUIRES_REVIEW record is verified, change only that record's verification state and evidence. Do not bulk-promote candidates merely because their domains look official.
