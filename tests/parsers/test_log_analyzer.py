import pytest
from scripts.python.log_analyzer import LogAnalyzer

def test_frequency_analysis():
    records = [
        {"User": "alice", "Action": "login"},
        {"User": "bob", "Action": "login"},
        {"User": "alice", "Action": "login"},
        {"User": "charlie", "Action": "login"},
    ]
    counts = LogAnalyzer.frequency_analysis(records, "User")
    assert counts["alice"] == 2
    assert counts["bob"] == 1
    assert counts["charlie"] == 1

def test_outlier_detection():
    records = [
        {"Process": "svchost.exe"},
        {"Process": "svchost.exe"},
        {"Process": "svchost.exe"},
        {"Process": "mimikatz.exe"},
    ]
    outliers = LogAnalyzer.find_outliers(records, "Process", max_frequency=1)
    assert len(outliers) == 1
    assert outliers[0]["Process"] == "mimikatz.exe"
