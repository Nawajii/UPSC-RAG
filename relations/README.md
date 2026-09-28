# Lightweight Knowledge Relationships

No graph database initially.

Relationships are stored as structured records:

- topic → source of knowledge
- topic → source of truth
- topic → PYQ
- topic → current affair
- current affair → government policy/scheme/report/judgment
- PYQ → recurring theme
- source → version/replacement
- claim → supporting source
- claim → conflicting source

Use stable IDs so the relationship layer can later be indexed or migrated without redesigning the corpus.
