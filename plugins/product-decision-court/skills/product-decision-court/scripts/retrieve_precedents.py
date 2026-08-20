#!/usr/bin/env python3
"""Retrieve audited and provisional product-decision precedents."""

import argparse
import csv
import json
import math
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references"
TOKEN = re.compile(r"[a-z0-9][a-z0-9_-]+")
STOP = {"the", "and", "for", "that", "with", "this", "from", "into", "when", "what", "why", "how", "our", "your", "are", "was", "were", "but", "not", "have", "has", "had", "will", "would", "should", "could", "product", "decision", "build"}

DECISION_ROUTES = [
    ({"custom", "customer", "enterprise", "request", "whale"}, {"PJ-001", "PJ-002", "PJ-013", "PJ-014", "PJ-015"}, "feature requests prioritization strategy focus reusable platform"),
    ({"growth", "acquisition", "retention"}, {"PJ-003", "PJ-004", "PJ-007", "PJ-008", "PJ-015"}, "retention cohorts distribution product market fit"),
    ({"launch", "delay", "quality", "speed"}, {"PJ-015", "PJ-016", "PJ-017"}, "quality ownership speed cost tradeoff failure risk"),
    ({"ai", "copilot", "autopilot", "agent", "automation"}, {"PJ-015", "PJ-019", "PJ-020"}, "AI reliability evaluation human review failure modes observability"),
    ({"competitor", "copy", "parity", "differentiate"}, {"PJ-001", "PJ-014", "PJ-018"}, "competitor convention mechanism differentiation strategy"),
    ({"price", "pricing", "package", "monetize"}, {"PJ-009", "PJ-010", "PJ-012"}, "pricing value metric positioning monetization strategy"),
]


def terms(text):
    return [t for t in TOKEN.findall(text.lower()) if t not in STOP and len(t) > 2]


def score(query, text):
    q = Counter(terms(query))
    d = Counter(terms(text))
    if not q or not d:
        return 0.0
    overlap = sum(min(v, d[k]) for k, v in q.items())
    phrase_bonus = sum(1.5 for k in q if k in text.lower())
    return (overlap + phrase_bonus) / math.sqrt(sum(q.values()) * sum(d.values()))


def load_rows(path, tier):
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            row["tier"] = tier
            yield row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--limit", type=int, default=12)
    args = parser.parse_args()
    query_tokens = set(terms(args.query))
    routed_ids = set()
    expansions = []
    for triggers, ids, expansion in DECISION_ROUTES:
        if query_tokens & triggers:
            routed_ids.update(ids)
            expansions.append(expansion)
    expanded_query = args.query + " " + " ".join(expansions)
    rows = list(load_rows(REFS / "audited_precedents.csv", "AUDITED_GOLD"))
    rows += list(load_rows(REFS / "provisional_clusters.csv", "PROVISIONAL_CLUSTER"))
    ranked = []
    for row in rows:
        searchable = " ".join(str(v) for v in row.values())
        value = score(expanded_query, searchable)
        if row["tier"] == "AUDITED_GOLD":
            value *= 1.35
        if row.get("id") in routed_ids:
            value += 0.8
        if value:
            ranked.append((value, row))
    ranked.sort(key=lambda item: item[0], reverse=True)
    for value, row in ranked[: args.limit]:
        out = dict(row)
        out["retrieval_score"] = round(value, 4)
        print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
