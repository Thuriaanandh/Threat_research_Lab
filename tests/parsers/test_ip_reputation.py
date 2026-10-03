import pytest
from scripts.python.ip_reputation import IPReputation

def test_private_ip():
    res = IPReputation.evaluate("192.168.1.50")
    assert res["verdict"] == "BENIGN_INTERNAL"
    assert res["score"] == 0

def test_known_c2():
    res = IPReputation.evaluate("198.51.100.23")
    assert res["verdict"] == "MALICIOUS"
    assert res["score"] >= 90
    assert res["category"] == "C2_SERVER"
