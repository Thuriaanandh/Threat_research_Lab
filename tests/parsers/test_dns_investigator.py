import pytest
from scripts.python.dns_investigator import DNSInvestigator

def test_benign_domain():
    res = DNSInvestigator.analyze_domain("www.google.com")
    assert res["is_dga_candidate"] is False
    assert res["is_tunneling_candidate"] is False

def test_dga_detection():
    res = DNSInvestigator.analyze_domain("xj93kdfm93kdls93.dga-net.xyz")
    assert res["is_dga_candidate"] is True
    assert res["has_suspicious_tld"] is True

def test_dns_tunneling_detection():
    long_domain = "dGVzdC1kYXRhLWV4ZmlsdHJhdGlvbi1zZXNzaW9uLWluZm9ybWF0aW9u.tunnel.c2server.org"
    res = DNSInvestigator.analyze_domain(long_domain)
    assert res["is_tunneling_candidate"] is True
