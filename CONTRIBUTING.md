# Contributing to Threat Research Lab

Thank you for your interest in contributing to the **Threat Research & Hunting Detection Lab**. This repository is maintained as a professional research and training platform.

---

## Core Contribution Standards

We welcome contributions that enhance the realism, technical rigor, and pedagogical value of the lab:

1. **Empirical Realism**: Scenarios, logs, and telemetry must reflect authentic enterprise environments and documented adversary TTPs.
2. **Standardized Lab Architecture**: Any newly proposed lab must include all standard files:
   - `README.md`
   - `scenario.md`
   - `objectives.md`
   - `environment.md`
   - `datasets/`
   - `tasks.md`
   - `hints.md`
   - `solutions/`
   - `detections/`
   - `mitre.md`
   - `report-template.md`
   - `validation.md`
3. **Detection Rule Quality**:
   - Sigma rules must conform to the official SigmaHQ specification and pass `pySigma` validation.
   - YARA rules must include metadata, clear strings, and avoid overly broad conditions (e.g., matching common PE headers alone).
   - Rules must be accompanied by both positive (malicious) and negative (benign baseline) test cases.
4. **Code Quality**:
   - Python code must adhere to PEP 8, include type annotations, and pass automated `pytest` unit tests.
   - All scripts must include CLI help via `argparse` or `click`.
5. **No Live Malware**: Never commit live, weaponized malware binaries, unencrypted payloads, or active exploit code. Use safe synthetic artifacts or hashes.
6. **No Hardcoded Secrets**: Ensure no real API keys, credentials, or private organizational data are included.

---

## Development Workflow

1. Fork the repository and create a descriptive feature branch:
   ```bash
   git checkout -b feature/lab-enhancement-sigma
   ```
2. Make your additions or enhancements.
3. Validate code and detections locally:
   ```bash
   pytest tests/ -v
   python scripts/utilities/validate_repo.py
   ```
4. Commit your changes with clear, structured commit messages:
   ```bash
   git commit -m "feat(sigma): add behavioral rule for rundll32 ADS execution"
   ```
5. Push to your fork and submit a Pull Request against `main`.
