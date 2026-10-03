# Investigation Reference: Operation Copper Dagger (APT29 / Midnight Blizzard)

## Executive Summary
During a proactive threat hunt across Active Directory and endpoint telemetry, anomalous living-off-the-land execution was identified originating from workstation `WS-SEC-892` assigned to identity `CORP\admin_mchen`. The threat actor leveraged compromised service account credentials, executed encoded PowerShell via WMI to disable local antivirus telemetry, dumped local credentials via LSASS process access, and established HTTPS C2 persistence to an external cloud infrastructure endpoint. Prompt containment severed the C2 channel and isolated the asset prior to lateral movement into the Domain Controller tier.

## Scope & Impacted Assets
* **Compromised Host**: `WS-SEC-892` (10.14.20.115) - Windows 11 Enterprise
* **Compromised Identity**: `CORP\admin_mchen` (Local Administrator)
* **Affected Service**: `WinRM` / WMI Remote Execution
* **C2 Endpoint**: `203.0.113.88:8443` (Hosted on offshore cloud VPS)

## Initial Threat Hypothesis
*"Adversaries targeting privileged administrative workstations will leverage WMI (`wmic.exe` or `wmiprvse.exe`) to spawn obfuscated scripting interpreters, bypassing standard GUI process creation detections and disabling endpoint protections."*

## Data Sources & Telemetry Queried
* Sysmon Event ID 1 (Process Creation)
* Sysmon Event ID 3 (Network Connection)
* Sysmon Event ID 10 (ProcessAccess - LSASS Target)
* Windows Security Event ID 4624 (Logon Type 3 - Network Logon)
* Perimeter Firewall NetFlow Records

## Chronological Forensic Timeline
| Timestamp (UTC) | Hostname | Identity | Observed Event & Parameters | Source Telemetry | Mitre ATT&CK |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-28 22:11:04 | WS-SEC-892 | CORP\admin_mchen | Type 3 Network Logon from internal pivot 10.14.20.50 | Security 4624 | T1078.002 |
| 2026-09-28 22:11:45 | WS-SEC-892 | CORP\admin_mchen | `wmiprvse.exe` spawns `powershell.exe -NonI -W Hidden -Exec Bypass -enc JAB...` | Sysmon EID 1 | T1047 / T1059.001 |
| 2026-09-28 22:12:10 | WS-SEC-892 | CORP\admin_mchen | `powershell.exe` accesses `lsass.exe` with GrantedAccess `0x1010` | Sysmon EID 10 | T1003.001 |
| 2026-09-28 22:12:35 | WS-SEC-892 | CORP\admin_mchen | Outbound TCP socket established to `203.0.113.88:8443` | Sysmon EID 3 | T1071.001 |
| 2026-09-28 22:13:01 | WS-SEC-892 | CORP\admin_mchen | Registry Run key created: `HKLM\Software\Microsoft\Windows\CurrentVersion\Run\WinTelemetryUpdate` | Sysmon EID 13 | T1547.001 |

## MITRE ATT&CK Mapping
* **Execution**: T1047 (Windows Management Instrumentation), T1059.001 (PowerShell)
* **Credential Access**: T1003.001 (LSASS Memory Dumping)
* **Command and Control**: T1071.001 (Web Protocols: HTTPS)
* **Persistence**: T1547.001 (Registry Run Keys / Startup Folder)

## Engineered Detection Deliverable (Sigma)
```yaml
title: WMI Spawning Obfuscated PowerShell
id: b261a8a2-7fa3-43ce-b7be-81f1d1123f81
status: production
description: Detects WMI service spawning PowerShell with execution bypass and encoded command arguments.
references:
  - https://attack.mitre.org/techniques/T1047/
author: Threat Research Lab
logsource:
  category: process_creation
  product: windows
detection:
  selection_parent:
    ParentImage|endswith: '\wmiprvse.exe'
  selection_child:
    Image|endswith: '\powershell.exe'
    CommandLine|contains:
      - '-enc'
      - '-EncodedCommand'
      - 'Bypass'
      - '-NonI'
  condition: selection_parent and selection_child
falsepositives:
  - Legitimate automated SCCM or Ansible management tasks (tune via service account filtering).
level: high
tags:
  - attack.execution
  - attack.t1047
  - attack.t1059.001
```
