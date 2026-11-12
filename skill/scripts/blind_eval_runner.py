#!/usr/bin/env python3
"""Minimal blind-review evaluation runner for pre-labeled chart cases.

Input CSV columns: case_id,split,reviewer_verdict,reference_verdict
Use split values development, validation, or test. This runner summarizes verdict
agreement only; it does not backtest trading performance or prove an edge.
"""
import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ALLOWED = {"ENTER", "WATCH", "NO_TRADE"}
SPLITS = {"development", "validation", "test"}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input_csv")
    p.add_argument("--out", default="blind_eval_summary.json")
    args = p.parse_args()
    rows = list(csv.DictReader(Path(args.input_csv).open(newline="", encoding="utf-8")))
    required = {"case_id", "split", "reviewer_verdict", "reference_verdict"}
    if not rows or not required.issubset(rows[0]):
        raise SystemExit(f"CSV needs columns: {', '.join(sorted(required))}")
    seen, by_split = set(), defaultdict(Counter)
    for row in rows:
        case_id = row["case_id"].strip()
        split = row["split"].strip().lower()
        a, b = row["reviewer_verdict"].strip().upper(), row["reference_verdict"].strip().upper()
        if not case_id or case_id in seen:
            raise SystemExit(f"Blank or duplicate case_id: {case_id!r}")
        if split not in SPLITS or a not in ALLOWED or b not in ALLOWED:
            raise SystemExit(f"Invalid split/verdict in case {case_id}")
        seen.add(case_id)
        by_split[split]["total"] += 1
        by_split[split]["exact_agreement"] += int(a == b)
        by_split[split][f"reference_{b}"] += 1
        by_split[split][f"reviewer_{a}"] += 1
    result = {
        "metric": "verdict agreement only; not strategy profitability",
        "case_count": len(rows),
        "splits": {
            split: {
                **dict(counts),
                "agreement_rate": round(counts["exact_agreement"] / counts["total"], 4),
            }
            for split, counts in by_split.items()
        },
        "limitations": [
            "Reference labels need independent review and a documented rubric.",
            "Do not tune on the test split and report it as independent.",
            "Agreement is not proof of profitability or execution quality.",
        ],
    }
    Path(args.out).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
