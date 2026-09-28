#!/usr/bin/env python3
"""Lightweight offline integrity checks for UPSC-RAG JSON layers."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    with open(ROOT / path, encoding="utf-8") as f:
        return json.load(f)

def main():
    manifest = load("manifests/corpus_manifest.json")
    taxonomy = load("taxonomy/master_index.json")
    sources = load("sources/source_registry.json")
    ca = load("current_affairs/2026.json")
    tests = load("tests/retrieval_cases.json")

    source_ids = {x["source_id"] for x in sources["records"]}
    assert len(source_ids) == len(sources["records"]), "duplicate source_id"
    assert ca["coverage_start"] == "2026-05-01", "current-affairs coverage start changed"
    missing = []
    for record in ca["records"]:
        for sid in record.get("primary_source_ids", []):
            if sid not in source_ids:
                missing.append(sid)
    assert not missing, f"missing primary source IDs: {sorted(set(missing))}"
    assert tests["cases"], "no retrieval acceptance tests"
    assert manifest["layers"]["taxonomy"]["status"] == "READY"
    assert manifest["layers"]["source_of_knowledge"]["status"] == "READY"
    print("UPSC-RAG integrity checks: PASS")
    print(f"source records: {len(sources['records'])}")
    print(f"current-affairs records: {len(ca['records'])}")
    print(f"retrieval acceptance cases: {len(tests['cases'])}")
    print(f"taxonomy sections: {len(taxonomy)}")

if __name__ == "__main__":
    main()
