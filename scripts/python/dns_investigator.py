#!/usr/bin/env python3
"""
DNS Covert Channel & DGA Detection Engine
Calculates domain name Shannon entropy, consonant-to-vowel ratios,
length distributions, and flags DNS tunneling patterns.
"""
import math
import argparse
from typing import Dict, Any, List

class DNSInvestigator:
    VOWELS = set("aeiou")
    SUSPICIOUS_TLDS = {".xyz", ".top", ".cc", ".biz", ".tk", ".club", ".work"}

    @staticmethod
    def calculate_entropy(domain: str) -> float:
        # Evaluate root hostname without TLD
        parts = domain.lower().split('.')
        target = parts[0] if parts else domain
        if not target:
            return 0.0
        entropy = 0.0
        length = len(target)
        counts = {}
        for c in target:
            counts[c] = counts.get(c, 0) + 1
        for count in counts.values():
            p = count / length
            entropy -= p * math.log2(p)
        return round(entropy, 4)

    @classmethod
    def analyze_domain(cls, domain: str) -> Dict[str, Any]:
        clean_domain = domain.strip().lower()
        parts = clean_domain.split('.')
        subdomain = parts[0] if len(parts) > 1 else clean_domain
        entropy = cls.calculate_entropy(subdomain)

        # Character ratio analysis
        letters = [c for c in subdomain if c.isalpha()]
        vowel_count = sum(1 for c in letters if c in cls.VOWELS)
        consonant_count = len(letters) - vowel_count
        ratio = round(consonant_count / (vowel_count + 1e-5), 2)

        has_suspicious_tld = any(clean_domain.endswith(tld) for tld in cls.SUSPICIOUS_TLDS)
        is_high_entropy = entropy > 3.8 and len(subdomain) > 12
        is_dga_candidate = is_high_entropy or (ratio > 5.0 and len(subdomain) > 10)
        is_tunneling_candidate = len(clean_domain) > 50 or (len(parts) > 4 and is_high_entropy)

        return {
            "domain": clean_domain,
            "subdomain": subdomain,
            "length": len(clean_domain),
            "entropy": entropy,
            "consonant_vowel_ratio": ratio,
            "has_suspicious_tld": has_suspicious_tld,
            "is_dga_candidate": is_dga_candidate,
            "is_tunneling_candidate": is_tunneling_candidate
        }

def main():
    parser = argparse.ArgumentParser(description="DNS Domain Entropy & DGA Detection Tool")
    parser.add_argument("-d", "--domain", help="Domain name to evaluate")
    parser.add_argument("-f", "--file", help="File containing list of domain names")
    args = parser.parse_args()

    domains = []
    if args.domain:
        domains.append(args.domain)
    elif args.file:
        with open(args.file, "r") as f:
            domains = [line.strip() for line in f if line.strip()]
    else:
        domains = [
            "www.google.com",
            "microsoft.com",
            "xj93kdfm93kdls93.dga-net.xyz",
            "dGVzdC1kYXRhLWV4ZmlsdHJhdGlvbi1zZXNzaW9u.tunnel.c2server.org"
        ]

    print("=== DNS Covert Channel & DGA Analysis ===")
    for d in domains:
        res = DNSInvestigator.analyze_domain(d)
        flag = " [!] ALERT" if (res["is_dga_candidate"] or res["is_tunneling_candidate"]) else " [OK]"
        print(f"{flag} {res['domain']:45s} | Entropy: {res['entropy']:<6} | DGA: {res['is_dga_candidate']} | Tunnel: {res['is_tunneling_candidate']}")

if __name__ == "__main__":
    main()
