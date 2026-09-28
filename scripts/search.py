#!/usr/bin/env python3
"""Tiny zero-dependency retrieval helper.

Searches repository text and JSONL records. This is intentionally not a vector database.
Usage:
    python scripts/search.py fiscal deficit
    python scripts/search.py "monetary policy"
"""

from pathlib import Path
import sys
import re

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git"}

def files():
    for p in ROOT.rglob("*"):
        if p.is_file() and not any(part in SKIP for part in p.parts):
            if p.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".jsonl", ".txt"}:
                yield p

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/search.py <query>")
        return 2
    query = " ".join(sys.argv[1:]).lower()
    terms = [t for t in re.findall(r"[a-z0-9]+", query) if len(t) > 1]
    if not terms:
        return 2

    hits = []
    for p in files():
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        low = text.lower()
        score = sum(low.count(t) for t in terms)
        if score:
            hits.append((score, p))

    for score, p in sorted(hits, key=lambda x: (-x[0], str(x[1])))[:25]:
        print(f"{score:>4}  {p.relative_to(ROOT)}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
