import pytest
from scripts.python.hash_analyzer import HashAnalyzer

def test_entropy_calculation():
    # Uniform text has lower entropy than random bytes
    uniform = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    high_ent = bytes(range(256)) * 4
    assert HashAnalyzer.calculate_entropy(uniform) == 0.0
    assert HashAnalyzer.calculate_entropy(high_ent) > 7.5

def test_pe_detection():
    pe_header = b"MZ\x90\x00" + b"\x00"*60
    res = HashAnalyzer.analyze_bytes(pe_header)
    assert res["is_pe_executable"] is True
