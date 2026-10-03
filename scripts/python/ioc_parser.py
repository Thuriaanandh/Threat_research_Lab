#!/usr/bin/env python3
"""
IOC Parser & Defanging Engine
Extracts and normalizes Indicators of Compromise (IPs, domains, hashes, URLs, CVEs)
from unstructured text, logs, and threat intelligence reports.
"""
import re
import json
import argparse
from typing import Dict, List, Set

class IOCParser:
    IPV4_PATTERN = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    MD5_PATTERN = r'\b[a-fA-F0-9]{32}\b'
    SHA1_PATTERN = r'\b[a-fA-F0-9]{40}\b'
    SHA256_PATTERN = r'\b[a-fA-F0-9]{64}\b'
    CVE_PATTERN = r'\bCVE-\d{4}-\d{4,7}\b'
    URL_PATTERN = r'https?://[\w\-\.\~\:\?\#\[\]\@\!\$\&\'\(\)\*\+\,\;\=\/\%]+'
    DOMAIN_PATTERN = r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b'

    @staticmethod
    def defang_ip(ip: str) -> str:
        return ip.replace('.', '[.]')

    @staticmethod
    def defang_domain(domain: str) -> str:
        return domain.replace('.', '[.]')

    @staticmethod
    def defang_url(url: str) -> str:
        return url.replace('http://', 'hxxp://').replace('https://', 'hxxps://').replace('.', '[.]')

    @classmethod
    def parse_text(cls, text: str, defang: bool = False) -> Dict[str, List[str]]:
        ips = sorted(list(set(re.findall(cls.IPV4_PATTERN, text))))
        sha256s = sorted(list(set(refindall := re.findall(cls.SHA256_PATTERN, text))))
        
        # Exclude sha256 matches when checking sha1 and md5
        remaining_text = text
        for s in sha256s:
            remaining_text = remaining_text.replace(s, '')
            
        sha1s = sorted(list(set(re.findall(cls.SHA1_PATTERN, remaining_text))))
        for s in sha1s:
            remaining_text = remaining_text.replace(s, '')
            
        md5s = sorted(list(set(re.findall(cls.MD5_PATTERN, remaining_text))))
        cves = sorted(list(set(re.findall(cls.CVE_PATTERN, text))))
        urls = sorted(list(set(re.findall(cls.URL_PATTERN, text))))
        
        # Domains: exclude URLs and IPs
        raw_domains = set(re.findall(cls.DOMAIN_PATTERN, text))
        domains = sorted(list({d for d in raw_domains if not re.match(cls.IPV4_PATTERN, d) and not any(d in u for u in urls)}))

        if defang:
            ips = [cls.defang_ip(ip) for ip in ips]
            domains = [cls.defang_domain(d) for d in domains]
            urls = [cls.defang_url(u) for u in urls]

        return {
            'ipv4': ips,
            'sha256': sha256s,
            'sha1': sha1s,
            'md5': md5s,
            'cves': cves,
            'urls': urls,
            'domains': domains
        }

def main():
    parser = argparse.ArgumentParser(description="Extract and defang IOCs from text files.")
    parser.add_argument("-i", "--input", help="Path to input text or report file")
    parser.add_argument("-t", "--text", help="Direct text string to parse")
    parser.add_argument("-d", "--defang", action="store_true", help="Defang indicators (e.g., 1.1.1[.]1)")
    parser.add_argument("-j", "--json", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    content = ""
    if args.input:
        with open(args.input, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    elif args.text:
        content = args.text
    else:
        content = "Sample C2: 198.51.100.42 and domain c2-update.net, SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

    results = IOCParser.parse_text(content, defang=args.defang)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print("=== Extracted Indicators of Compromise ===")
        for k, v in results.items():
            print(f"[{k.upper()}] ({len(v)}):")
            for item in v:
                print(f"  - {item}")

if __name__ == "__main__":
    main()
