import pytest
from scripts.python.ioc_parser import IOCParser

def test_ioc_parser_extraction():
    sample = """
    Malicious host 198.51.100.42 connected to https://malicious-c2.org/download.exe
    Sha256 hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    Vulnerability referenced: CVE-2021-44228
    """
    res = IOCParser.parse_text(sample, defang=False)
    assert "198.51.100.42" in res["ipv4"]
    assert "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" in res["sha256"]
    assert "CVE-2021-44228" in res["cves"]
    assert "https://malicious-c2.org/download.exe" in res["urls"]

def test_ioc_parser_defanging():
    sample = "198.51.100.42 and domain c2.net"
    res = IOCParser.parse_text(sample, defang=True)
    assert "198[.]51[.]100[.]42" in res["ipv4"]
    assert "c2[.]net" in res["domains"]
