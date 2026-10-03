# Changelog

All notable changes to the **Threat Research & Hunting Detection Lab** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-10-03
### Added
- **Complete 20-Lab Curriculum**:
  - Phase 1: Threat Hunting Foundations (Labs 01-04)
  - Phase 2: Telemetry & Endpoint Hunting (Labs 05-07)
  - Phase 3: Frameworks & Query Mastery (Labs 08-11: ATT&CK, Threat Intel, KQL, Splunk)
  - Phase 4: Detection Engineering & Validation (Labs 12-15: Detection Eng, Sigma, YARA, Tuning)
  - Phase 5: Advanced & Zero Trust Hunting (Labs 16-19: Python, Cloud, Zscaler, Detection-as-Code)
  - Phase 6: Capstone Mega-Investigation (Lab 20: Operation NightHawk)
- **Standardized Lab Architecture**: All 20 labs include README, scenario, objectives, environment, datasets, tasks, hints, solutions, detections, mitre, report-template, and validation files.
- **Python Security Automation Toolkit**:
  - `ioc_parser.py`: Regex-based indicator extraction and defanging
  - `log_analyzer.py`: Multi-format log frequency and anomaly detection
  - `ip_reputation.py`: Mock threat intelligence scoring and geo-enrichment
  - `hash_analyzer.py`: File entropy and PE anomaly assessment
  - `dns_investigator.py`: Shannon entropy and DGA detection engine
- **Automated Testing & CI/CD**:
  - GitHub Actions workflows for Python test execution and Detection-as-Code validation
  - Full `pytest` test suite for scripts, Sigma rules, and repo integrity
- **Enterprise Documentation Guides**:
  - Methodological hunting guides, telemetry taxonomy, investigation playbook, and MITRE mapping standard.
