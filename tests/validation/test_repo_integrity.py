import pytest
from pathlib import Path

def test_all_20_labs_exist():
    labs_dir = Path("labs")
    assert labs_dir.exists()
    subdirs = sorted([d.name for d in labs_dir.iterdir() if d.is_dir()])
    assert len(subdirs) == 20, f"Expected 20 lab directories, found {len(subdirs)}"
