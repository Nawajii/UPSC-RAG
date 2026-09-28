# Data Model

## Core entities

### Topic
A stable node in the UPSC syllabus taxonomy.

### Source
A source with authority, provenance, URL, date and role.

### Claim
A factual proposition supported by one or more sources.

### PYQ
An actual UPSC question with official provenance plus our analytical metadata.

### Current Affair
A dated development linked to one or more syllabus topics and authoritative evidence.

### Relation
A lightweight edge between records.

### Document
Metadata for a large document stored outside GitHub, normally in the ChatGPT Project.

## Why claims are separate

A source is not a fact. A claim record allows us to track:

- what is being asserted
- who says it
- when it was valid
- whether another authoritative source conflicts
- whether it is current

This is essential for changing policy, law, statistics and contested claims.

## Status semantics

- VERIFIED: sufficient authoritative evidence
- PROVISIONAL: useful but evidence incomplete
- CONFLICTING: material disagreement remains
- OUTDATED: historical record no longer current
- REQUIRES_REVIEW: consequential uncertainty

## Dates

Use ISO 8601 dates.

For time-sensitive records, always preserve the source publication/update date and the date we last verified the record.
