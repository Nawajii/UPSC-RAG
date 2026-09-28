# Ingestion Rules

## Source documents in the ChatGPT Project

When a user uploads a legitimate learning document:

1. Register it in `sources/knowledge_sources.yaml`.
2. Assign a stable source ID.
3. Record edition/year when known.
4. Map it to relevant syllabus IDs.
5. Do not copy the book into GitHub.
6. Use the Project document as the learning source.
7. Use authoritative external sources for verification.

## Official web sources

For a source-of-truth record:

1. identify the institution
2. open the underlying official document/page
3. record canonical URL
4. record publication/update date
5. record access/verification date
6. map to syllabus
7. create claim records only for UPSC-useful facts
8. preserve historical versions when relevant

## Current affairs

Do not ingest an article simply because it is recent.

Retain it only when:
- it connects to the syllabus
- it contains a development with UPSC value
- a primary source can be identified where appropriate

## PYQs

Only ingest questions whose official UPSC provenance can be established. Secondary compilations may help discover or classify questions, but the official UPSC paper remains the provenance anchor.
