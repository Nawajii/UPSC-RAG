#!/usr/bin/env python3
"""Lightweight integrity checks for the UPSC-RAG repository.

No external dependencies required.
"""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "docs/OPERATING_RULES.md",
    "docs/RETRIEVAL_PROTOCOL.md",
    "schema/record_schema.json",
    "taxonomy/upsc_master_index.yaml",
    "sources/registry.yaml",
    "pyqs/index.yaml",
    "current_affairs/index.yaml",
    "relations/index.yaml",
    "manifests/corpus.yaml",
]

def main():
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        print("MISSING:")
        for p in missing:
            print(f"  - {p}")
        return 1

    schema = json.loads((ROOT / "schema/record_schema.json").read_text())
    assert schema["title"] == "UPSC-RAG Record"

    taxonomy = (ROOT / "taxonomy/upsc_master_index.yaml").read_text()
    assert "formal_current_affairs_start: \"2026-05-01\"" in taxonomy

    manifest = (ROOT / "manifests/corpus.yaml").read_text()
    assert "deferred:" in manifest
    assert "embeddings" in manifest

    print(f"UPSC-RAG integrity check passed: {len(REQUIRED)} required files present.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
