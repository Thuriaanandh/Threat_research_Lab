import pytest
import yaml
from pathlib import Path

def test_sigma_rule_structure():
    sigma_files = list(Path("detections/sigma").glob("*.yml"))
    assert len(sigma_files) >= 5, "Expected at least 5 baseline Sigma rules"
    required_keys = {"title", "id", "status", "description", "logsource", "detection", "level"}
    for sf in sigma_files:
        with open(sf, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            missing = required_keys - set(data.keys())
            assert not missing, f"Rule {sf.name} is missing required fields: {missing}"
