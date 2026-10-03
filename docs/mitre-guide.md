# MITRE ATT&CK Operationalization Guide

A comprehensive guide to applying the MITRE ATT&CK Enterprise Matrix (v14+) to threat hunting, telemetry assessment, and detection engineering.

---

## 1. Matrix Hierarchy: Tactics vs Techniques vs Procedures

* **Tactic (The "Why")**: The adversary's tactical goal (e.g., `TA0001: Initial Access`, `TA0006: Credential Access`, `TA0010: Exfiltration`).
* **Technique (The "What")**: The general method used to achieve the goal (e.g., `T1059: Command and Scripting Interpreter`).
* **Sub-Technique (The "Specific Mechanism")**: The specific flavor of the technique (e.g., `T1059.001: PowerShell`).
* **Procedure (The "Exact Implementation")**: The precise adversary command or malware code observed in an incident (e.g., `powershell.exe -w hidden -enc JAB...`).

---

## 2. ATT&CK Data Sources & Data Components

Modern detection engineering maps directly to ATT&CK **Data Components**:

| Tactic | Technique | Sub-Technique | Required Data Component | Telemetry Provider |
| :--- | :--- | :--- | :--- | :--- |
| Execution | T1059 | T1059.001 (PowerShell) | `Process: Process Creation` | Sysmon EID 1 / Win 4688 |
| Defense Evasion | T1055 | T1055.001 (Process Injection) | `Process: Process Access` | Sysmon EID 8 / EID 10 |
| Credential Access | T1003 | T1003.001 (LSASS Memory) | `Process: Process Access` | Sysmon EID 10 |
| Persistence | T1053 | T1053.005 (Scheduled Task) | `Scheduled Job: Scheduled Job Creation` | Security 4698 / Sysmon EID 1 |
| Command and Control | T1071 | T1071.004 (DNS) | `Network Traffic: DNS Query` | Sysmon EID 22 / Zeek `dns.log` |
| Exfiltration | T1567 | T1567.002 (Cloud Storage) | `Cloud Storage: Object Modification` | AWS CloudTrail `PutObject` |

---

## 3. ATT&CK Heatmap & Defensive Gap Analysis

By cataloging hunting hypotheses and deployed detections against the ATT&CK matrix, security teams can pinpoint defensive blind spots:
* **Uncovered Tactics**: E.g., zero visibility into `TA0008: Lateral Movement` due to lack of RPC/SMB flow telemetry.
* **Telemetry Deficits**: Missing Sysmon EID 10 (ProcessAccess) prevents detecting LSASS dumping.
