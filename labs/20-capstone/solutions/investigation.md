# Capstone Investigation Dossier: Operation NightHawk

## 1. Executive Summary
On 2026-10-03 at 02:10 UTC, a spearphishing email delivered `invoice_2026.docm` to `cfo@corp.com`. Office macro execution spawned an obfuscated PowerShell cradle, which dumped LSASS memory on `WS-EXEC-01` to harvest `DomainAdmin_SVC` credentials. The adversary used Type 3 network logon to pivot laterally to Domain Controller `SRV-DC-01`, established covert DNS C2 communication (`system-core-update.net`), compromised cloud administrative credentials (`aws-admin-backup`), and exfiltrated `q3_ledger.csv` from S3 bucket `corp-financial-records-2026`.

## 2. Complete Forensic Chronology
| Timestamp (UTC) | Layer | Host / Identity | Action & Parameters | Telemetry Source | MITRE ATT&CK |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 02:10:00 | Email | cfo@corp.com | Phishing attachment delivered | Email Gateway | T1566.001 |
| 02:14:15 | Endpoint | WS-EXEC-01 | WINWORD.EXE spawned PowerShell cradle | Sysmon EID 1 | T1059.001 |
| 02:15:00 | Credential | WS-EXEC-01 | PowerShell accessed LSASS (0x1010) | Sysmon EID 10 | T1003.001 |
| 02:16:30 | Identity | SRV-DC-01 | Lateral logon via DomainAdmin_SVC | Security 4624 | T1021.002 |
| 02:18:00 | Network | WS-EXEC-01 | DNS TXT C2 beacon query | Sysmon EID 22 | T1071.004 |
| 02:22:00 | Cloud | aws-admin-backup | ConsoleLogin without MFA from 198.51.100.99 | CloudTrail | T1078.004 |
| 02:25:00 | Exfiltration | aws-admin-backup | GetObject on q3_ledger.csv | CloudTrail | T1530 |
