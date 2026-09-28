# UPSC-RAG Build Status

**As of 2026-09-28**

## Built

- Master repository structure
- UPSC-oriented taxonomy
- Source hierarchy
- Source registry
- Source-of-Knowledge registry
- Generic record schema
- PYQ metadata model and registry
- Current-affairs model
- Lightweight relationship model
- Status/versioning conventions
- Retrieval protocol
- Zero-dependency integrity validation
- Roadmap

## Verified external anchors

The official UPSC website currently exposes:
- Civil Services (Main) Examination 2026 materials, including GS I-IV, Essay and Economics Optional papers.
- Previous Year Question Papers, including CSE Prelims and Mains papers.

The CSE 2027 notification/syllabus should supersede the 2026 anchor when UPSC publishes it.

## Not yet populated

- Full verified PYQ question corpus
- Topic-by-topic source-of-truth records
- May 2026 onward current-affairs records
- Registered copies/metadata for user-uploaded learning books

These are deliberately separate from the architecture. Empty registries mean the evidence has not yet been ingested, not that the topic is absent.

## Next evidence-building sequence

1. Lock the applicable CSE 2027 syllabus when officially published.
2. Populate verified PYQ metadata/question records from official UPSC papers.
3. Register uploaded Source-of-Knowledge documents as they appear.
4. Build high-value Source-of-Truth records by syllabus domain.
5. Add syllabus-linked current affairs from May 2026 onward.
6. Benchmark retrieval before considering embeddings.
