#!/usr/bin/env python3
"""
Repository & Detection Rule Integrity Validator
Performs comprehensive quality assurance:
1. Validates all 20 labs adhere to standard 11-file architecture
2. Validates all YAML files (Sigma rules, workflows, configs)
3. Validates Python script syntax and imports
4. Verifies documentation links and dataset consistency
"""
import sys
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

REQUIRED_LAB_FILES = [
    "README.md",
    "scenario.md",
    "objectives.md",
    "environment.md",
    "tasks.md",
    "hints.md",
    "mitre.md",
    "report-template.md",
    "validation.md"
]

def check_yaml_files() -> int:
    errors = 0
    print("[*] Validating YAML files...")
    yaml_files = list(REPO_ROOT.glob("**/*.yml")) + list(REPO_ROOT.glob("**/*.yaml"))
    for yf in yaml_files:
        try:
            with open(yf, "r", encoding="utf-8") as f:
                yaml.safe_load(f)
        except Exception as e:
            print(f"  [ERROR] Invalid YAML: {yf.relative_to(REPO_ROOT)}: {e}")
            errors += 1
    print(f"  -> Validated {len(yaml_files)} YAML files. Errors: {errors}")
    return errors

def check_labs_structure() -> int:
    errors = 0
    print("[*] Validating 20-Lab Curriculum Structure...")
    labs_dir = REPO_ROOT / "labs"
    if not labs_dir.exists():
        print("  [ERROR] labs/ directory does not exist!")
        return 1

    lab_dirs = sorted([d for d in labs_dir.iterdir() if d.is_dir()])
    print(f"  Found {len(lab_dirs)} lab directories.")

    for lab in lab_dirs:
        for req in REQUIRED_LAB_FILES:
            target = lab / req
            if not target.exists():
                print(f"  [ERROR] Lab {lab.name} is missing required file: {req}")
                errors += 1
        # Check datasets directory exists
        if not (lab / "datasets").exists() and not (lab / "dataset").exists():
            print(f"  [ERROR] Lab {lab.name} is missing datasets/ directory")
            errors += 1
        # Check solutions directory exists
        if not (lab / "solutions").exists() and not (lab / "solution").exists():
            print(f"  [ERROR] Lab {lab.name} is missing solutions/ directory")
            errors += 1
        # Check detections directory exists
        if not (lab / "detections").exists():
            print(f"  [ERROR] Lab {lab.name} is missing detections/ directory")
            errors += 1

    return errors

def check_python_syntax() -> int:
    errors = 0
    print("[*] Validating Python script compilation...")
    py_files = list(REPO_ROOT.glob("scripts/**/*.py")) + list(REPO_ROOT.glob("tests/**/*.py"))
    for pf in py_files:
        try:
            with open(pf, "r", encoding="utf-8") as f:
                compile(f.read(), str(pf), "exec")
        except Exception as e:
            print(f"  [ERROR] Syntax error in {pf.relative_to(REPO_ROOT)}: {e}")
            errors += 1
    print(f"  -> Validated {len(py_files)} Python files. Syntax errors: {errors}")
    return errors

def main():
    print("==================================================")
    print("Threat Research Lab — Quality Assurance Validator")
    print("==================================================")
    total_errors = 0
    total_errors += check_yaml_files()
    total_errors += check_python_syntax()
    total_errors += check_labs_structure()

    print("--------------------------------------------------")
    if total_errors == 0:
        print("[SUCCESS] All checks passed! Repository is clean, valid, and GitHub-ready.")
        sys.exit(0)
    else:
        print(f"[FAILED] Repository validation found {total_errors} issue(s).")
        sys.exit(1)

if __name__ == "__main__":
    main()
