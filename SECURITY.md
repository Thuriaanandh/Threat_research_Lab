# Security Policy

## Responsible Disclosure

The **Threat Research & Hunting Detection Lab** is an educational and defensive engineering platform. If you discover a security vulnerability in this repository (e.g., an unintended command injection vulnerability in a helper script or exposed sensitive data):

1. **Do NOT** open a public GitHub issue.
2. Email your findings directly to the repository maintainer or utilize GitHub Private Vulnerability Reporting.
3. Include detailed steps to reproduce the issue.

We strive to review and address all valid reports promptly.

---

## Safe Environment Usage

All scripts, datasets, and detection rules in this repository are intended for execution in:
* Local development environments
* Isolated virtual machines
* Containerized Docker sandboxes

Do not run automated ingestion scripts against sensitive production networks without prior authorization.
