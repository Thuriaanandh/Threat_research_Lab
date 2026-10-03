# Investigation Title: [Incident Name / Identifier]

## Executive Summary
[High-level, non-technical overview of the incident. Describe the core threat, the business or technical systems affected, the root cause vector, and the primary containment actions executed.]

## Scope & Impacted Assets
* **Affected Endpoints**: [e.g., WS-FIN-01 (10.0.1.45), SRV-APP-02 (10.0.2.10)]
* **Compromised Identities**: [e.g., CORP\jdoe, CORP\svc_backup]
* **Impacted Cloud Accounts**: [e.g., AWS Account 123456789012, Entra ID Tenant]
* **Confidentiality / Integrity Impact**: [e.g., Financial spreadsheet exfiltrated; no ransomware encryption observed]

## Initial Threat Hypothesis
[State the testable hunting hypothesis that initiated this inquiry. Example: "An adversary used living-off-the-land utilities (certutil/powershell) to stage second-stage loaders following spearphishing email delivery."]

## Data Sources & Telemetry Queried
* [ ] Windows Sysmon (Process Creation EID 1, Network Sockets EID 3, LSASS EID 10)
* [ ] Windows Security Event Log (Logon 4624/4625, Process 4688, Scheduled Tasks 4698)
* [ ] Linux Auditd (EXECVE, SYSCALL) & `/var/log/auth.log`
* [ ] Network Flow / Proxy Telemetry (Zeek `conn.log`, `http.log`, `ssl.log`, Zscaler Web Logs)
* [ ] Cloud Audit Logs (AWS CloudTrail, Azure Entra ID SigninLogs)

## Investigation Methodology & Pivots
1. **Initial Trigger Triage**: [Detail the alert, anomaly, or intel report that triggered the search]
2. **Process Ancestry Analysis**: [Examine parent-child lineage and command-line parameters]
3. **Network Corroboration**: [Correlate host socket events with perimeter firewall or proxy records]
4. **Persistence & Lateral Movement Checks**: [Inspect registry Run keys, scheduled tasks, and remote logins]

## Chronological Forensic Timeline
| Timestamp (UTC) | Hostname / IP | User / Identity | Activity / Command Line | Telemetry Source | Confidence |
| :--- | :--- | :--- | :--- | :--- | :---: |
| 2026-10-03 14:15:22 | WS-FIN-01 | CORP\jdoe | WINWORD.EXE opened invoice_oct2026.docm | Sysmon EID 1 | High |
| 2026-10-03 14:15:30 | WS-FIN-01 | CORP\jdoe | powershell.exe -enc JAB... (download cradle) | Sysmon EID 1 | High |
| 2026-10-03 14:15:35 | WS-FIN-01 | CORP\jdoe | Socket to 198.51.100.42:443 established | Sysmon EID 3 | High |

## Technical Evidence & Artifact Analysis
### Host Artifacts
[Document process trees, file paths, hashes, registry changes, and memory inspection findings]

### Network Artifacts
[Document IP connections, DNS domain lookups, HTTP User-Agents, JA3/JA4 fingerprints, and byte counts]

## Indicators of Compromise (IOCs)
| Indicator Type | Defanged Value | Context / Role | First Observed (UTC) |
| :--- | :--- | :--- | :--- |
| IPv4 | `198.51.100[.]42` | External C2 Server | 2026-10-03 14:15:35 |
| Domain | `update-telemetry[.]net` | DGA Beaconing Domain | 2026-10-03 14:16:00 |
| SHA256 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Dropped Staging Payload | 2026-10-03 14:15:31 |

## Adversary Behavior & MITRE ATT&CK Mapping
| Tactic | Technique | Sub-Technique | Observed Procedure |
| :--- | :--- | :--- | :--- |
| Initial Access | Phishing | T1566.001 (Spearphishing Attachment) | Malicious macro document sent via email |
| Execution | Command & Scripting | T1059.001 (PowerShell) | Encoded command line executing WebClient download |
| Credential Access | OS Credential Dumping | T1003.001 (LSASS Memory) | Read access into `lsass.exe` |

## Detection Opportunities & Engineered Rules
[Reference and embed Sigma, YARA, KQL, or SPL rules authored to detect this activity]

## False Positive Analysis & Detection Tuning
* **Anticipated False Positives**: [e.g., IT administrative PowerShell scripts running via SCCM]
* **Tuning Logic Implemented**: [e.g., Exclude processes launched by `C:\Windows\CCM\CcmExec.exe`]
* **Validated Precision & Recall**: [Precision: 98.2%, Recall: 100%]

## Remediation & Hardening Recommendations
1. **Immediate Containment**: [Isolate affected hosts, revoke active session tokens, block external IPs]
2. **Short-Term Eradication**: [Delete persistence scheduled tasks, remove staged payloads]
3. **Long-Term Hardening**: [Enforce Attack Surface Reduction (ASR) rules, deploy MFA for all administrative sessions]

## References
* [CISA Advisory / Vendor Report Link]
* [MITRE ATT&CK Technique Reference]
