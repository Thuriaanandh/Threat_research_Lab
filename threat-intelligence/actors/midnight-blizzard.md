# Threat Actor Profile: Midnight Blizzard (APT29 / Cozy Bear / Nobelium)

## 1. Actor Overview
* **Attribution**: Russian Foreign Intelligence Service (SVR)
* **Target Sectors**: Government, Think Tanks, Defense Contractors, Cloud Providers, Cybersecurity Vendors
* **Operational Motivation**: Long-term foreign policy intelligence gathering and espionage
* **Primary Tactic**: Sophisticated cloud and identity attacks, password spraying, OAuth app manipulation, token theft.

---

## 2. Key Adversary Mechanics
* **Password Spraying**: Distributed, low-volume password spraying originating from residential proxy pools to evade IP-based velocity rate-limits.
* **Service Principal & OAuth Compromise**: Gaining control over highly privileged legacy application registrations within Microsoft Entra ID to establish persistent API access without needing interactive user MFA.
* **Cloud Storage Exfiltration**: Direct querying of Microsoft Graph API to extract executive email communications.

---

## 3. High-Value Hunting Telemetry
* **Entra ID SigninLogs**: Correlate User-Agent signatures with rare ASNs; hunt for single failed attempts distributed across thousands of user accounts within a narrow time window.
* **Entra ID AuditLogs**: Monitor `Add service principal credentials`, `Consent to application`, and `Add member to role` events where the initiator is not an authorized cloud administrator.
