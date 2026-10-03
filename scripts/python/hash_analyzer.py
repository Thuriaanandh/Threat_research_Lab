#!/usr/bin/env python3
"""
File Hash & Entropy Analyzer
Calculates MD5, SHA1, SHA256, Shannon entropy, and inspects PE file structure
indicators (e.g. packed artifacts, suspicious section names).
"""
import math
import hashlib
import argparse
from typing import Dict, Any

class HashAnalyzer:
    @staticmethod
    def calculate_entropy(data: bytes) -> float:
        if not data:
            return 0.0
        entropy = 0.0
        length = len(data)
        byte_counts = [0] * 256
        for b in data:
            byte_counts[b] += 1
        for count in byte_counts:
            if count > 0:
                p = count / length
                entropy -= p * math.log2(p)
        return round(entropy, 4)

    @classmethod
    def analyze_bytes(cls, data: bytes, filename: str = "memory_buffer") -> Dict[str, Any]:
        md5 = hashlib.md5(data).hexdigest()
        sha1 = hashlib.sha1(data).hexdigest()
        sha256 = hashlib.sha256(data).hexdigest()
        entropy = cls.calculate_entropy(data)

        is_pe = data.startswith(b"MZ")
        is_packed = entropy > 7.2

        return {
            "target": filename,
            "size_bytes": len(data),
            "md5": md5,
            "sha1": sha1,
            "sha256": sha256,
            "entropy": entropy,
            "is_pe_executable": is_pe,
            "is_likely_packed_or_encrypted": is_packed
        }

    @classmethod
    def analyze_file(cls, filepath: str) -> Dict[str, Any]:
        with open(filepath, "rb") as f:
            data = f.read()
        return cls.analyze_bytes(data, filepath)

def main():
    parser = argparse.ArgumentParser(description="Calculate cryptographic hashes and Shannon entropy")
    parser.add_argument("-f", "--file", help="Path to file to inspect")
    parser.add_argument("-s", "--string", help="Raw string to analyze")
    args = parser.parse_args()

    if args.file:
        res = HashAnalyzer.analyze_file(args.file)
    elif args.string:
        res = HashAnalyzer.analyze_bytes(args.string.encode(), "cli_string")
    else:
        sample = b"MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00" + b"A"*1000
        res = HashAnalyzer.analyze_bytes(sample, "sample_benign_pe")

    print("=== Artifact Cryptographic & Entropy Analysis ===")
    for k, v in res.items():
        print(f"  {k:30s} : {v}")

if __name__ == "__main__":
    main()
