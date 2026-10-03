#!/usr/bin/env python3
"""
IP Reputation & Threat Assessment Tool
Evaluates IP addresses against simulated and public threat intelligence feeds,
determining classification (C2, Tor exit, Scanner, Benign) and threat score.
"""
import re
import json
import argparse
from typing import Dict, Any

class IPReputation:
    # Known simulated high-confidence malicious and infrastructure ranges
    MOCK_THREAT_DATABASE = {
        "198.51.100.23": {"score": 95, "category": "C2_SERVER", "actor": "Volt Typhoon", "country": "NL"},
        "198.51.100.42": {"score": 90, "category": "COBALT_STRIKE_BEACON", "actor": "APT29", "country": "RU"},
        "203.0.113.88": {"score": 88, "category": "EXTERNAL_PROXY", "actor": "UNC3944", "country": "RO"},
        "185.220.101.5": {"score": 75, "category": "TOR_EXIT_NODE", "actor": "Anonymous", "country": "DE"},
        "45.33.32.156": {"score": 60, "category": "INTERNET_SCANNER", "actor": "Shadowserver", "country": "US"},
        "8.8.8.8": {"score": 0, "category": "BENIGN_RESOLVER", "actor": "Google", "country": "US"},
        "1.1.1.1": {"score": 0, "category": "BENIGN_RESOLVER", "actor": "Cloudflare", "country": "US"},
    }

    @staticmethod
    def is_private(ip: str) -> bool:
        parts = [int(p) for p in ip.split('.')]
        if parts[0] == 10:
            return True
        if parts[0] == 172 and 16 <= parts[1] <= 31:
            return True
        if parts[0] == 192 and parts[1] == 168:
            return True
        if parts[0] == 127:
            return True
        return False

    @classmethod
    def evaluate(cls, ip: str) -> Dict[str, Any]:
        if cls.is_private(ip):
            return {
                "ip": ip,
                "score": 0,
                "verdict": "BENIGN_INTERNAL",
                "category": "RFC1918_PRIVATE_IP",
                "details": "Internal private address space; not routable on public internet."
            }

        if ip in cls.MOCK_THREAT_DATABASE:
            entry = cls.MOCK_THREAT_DATABASE[ip]
            return {
                "ip": ip,
                "score": entry["score"],
                "verdict": "MALICIOUS" if entry["score"] >= 70 else "SUSPICIOUS",
                "category": entry["category"],
                "actor": entry.get("actor", "Unknown"),
                "country": entry.get("country", "Unknown")
            }

        return {
            "ip": ip,
            "score": 10,
            "verdict": "UNKNOWN",
            "category": "UNCLASSIFIED_PUBLIC_IP",
            "details": "No known threat intelligence match in current repository catalog."
        }

def main():
    parser = argparse.ArgumentParser(description="Check IP Reputation & Threat Assessment")
    parser.add_argument("-i", "--ip", help="Single IPv4 address to evaluate")
    parser.add_argument("-f", "--file", help="File containing list of IP addresses")
    parser.add_argument("-j", "--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()

    ips = []
    if args.ip:
        ips.append(args.ip)
    elif args.file:
        with open(args.file, "r") as f:
            ips = [line.strip() for line in f if line.strip()]
    else:
        ips = ["198.51.100.23", "192.168.1.1", "185.220.101.5", "8.8.8.8"]

    results = [IPReputation.evaluate(ip) for ip in ips]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print("=== IP Threat Reputation Assessment ===")
        for r in results:
            print(f"[{r['verdict']}] {r['ip']} | Score: {r['score']}/100 | Category: {r['category']}")

if __name__ == "__main__":
    main()
