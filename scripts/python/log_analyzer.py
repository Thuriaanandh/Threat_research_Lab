#!/usr/bin/env python3
"""
Log Analyzer & Long-Tail Outlier Detector
Analyzes security event logs (CSV, JSON, Line-delimited), calculates field frequencies,
and surfaces rare long-tail anomalies.
"""
import csv
import json
import argparse
from collections import Counter
from typing import List, Dict, Any

class LogAnalyzer:
    @staticmethod
    def load_csv(filepath: str) -> List[Dict[str, Any]]:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            reader = csv.DictReader(f)
            return list(reader)

    @staticmethod
    def load_json(filepath: str) -> List[Dict[str, Any]]:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and "events" in data:
                return data["events"]
            return [data]

    @classmethod
    def frequency_analysis(cls, records: List[Dict[str, Any]], field: str) -> Counter:
        values = [r.get(field) for r in records if r.get(field) is not None]
        return Counter(values)

    @classmethod
    def find_outliers(cls, records: List[Dict[str, Any]], field: str, max_frequency: int = 1) -> List[Dict[str, Any]]:
        counts = cls.frequency_analysis(records, field)
        rare_values = {val for val, count in counts.items() if count <= max_frequency}
        return [r for r in records if r.get(field) in rare_values]

def main():
    parser = argparse.ArgumentParser(description="Security Log Frequency & Outlier Analyzer")
    parser.add_argument("-f", "--file", required=True, help="Path to CSV or JSON log file")
    parser.add_argument("--field", required=True, help="Target field to analyze (e.g., Image, User, Domain)")
    parser.add_argument("--top", type=int, default=10, help="Display top N frequent occurrences")
    parser.add_argument("--outliers", action="store_true", help="Display rare long-tail occurrences (count = 1)")
    parser.add_argument("--threshold", type=int, default=1, help="Frequency threshold for outliers")
    args = parser.parse_args()

    records = []
    if args.file.endswith(".csv"):
        records = LogAnalyzer.load_csv(args.file)
    elif args.file.endswith(".json"):
        records = LogAnalyzer.load_json(args.file)
    else:
        print("Unsupported file format. Please provide .csv or .json")
        return

    print(f"Loaded {len(records)} log events from {args.file}")
    counts = LogAnalyzer.frequency_analysis(records, args.field)

    if args.outliers:
        outliers = LogAnalyzer.find_outliers(records, args.field, max_frequency=args.threshold)
        print(f"=== Long-Tail Outliers for '{args.field}' (Count <= {args.threshold}) ===")
        print(f"Found {len(outliers)} anomalous events.")
        for item in outliers[:15]:
            print(f"  -> {item.get(args.field)} | Event: {item}")
    else:
        print(f"=== Top {args.top} Most Frequent '{args.field}' Values ===")
        for val, count in counts.most_common(args.top):
            print(f"  {count:6d} : {val}")

if __name__ == "__main__":
    main()
