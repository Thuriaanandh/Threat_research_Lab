# Threat Actor Profile: Volt Typhoon (Vanguard Panda / BRONZE SILHOUETTE)

## 1. Actor Overview
* **Attribution / State Sponsor**: People's Republic of China (PRC) State-Sponsored
* **Target Sectors**: Critical Infrastructure (Energy, Water, Telecommunications, Transportation, Defense Industrial Base)
* **Operational Motivation**: Pre-positioning for disruptive/destructive cyber attacks during geopolitical crises
* **Primary Tactic**: Extreme Living-off-the-Land (LOTL) operational security; minimizing custom malware footprints to blend into legitimate administrative baselines.

---

## 2. Fact vs Analysis vs Hypothesis

| Class | Statement |
| :--- | :--- |
| **FACT** | CISA Advisory AA23-140A confirms Volt Typhoon obtained initial access via zero-day vulnerabilities in SOHO routers and perimeter appliances (Fortinet FortiGuard, Ivanti Connect Secure). |
| **ANALYSIS** | The threat actor relies almost exclusively on built-in Windows administrative utilities (`netsh`, `wmic`, `ntdsutil`, `nltest`, `certutil`) rather than deploying commodity or custom C2 implants, effectively blinding purely signature-based endpoint antivirus. |
| **HYPOTHESIS** | The observed pre-positioning within satellite communications and water systems is intended to establish deterrence or disruption options in the event of regional conflict. |

---

## 3. Adversary TTPs & MITRE ATT&CK Matrix

| Tactic | Technique | Procedure | Hunting Telemetry |
| :--- | :--- | :--- | :--- |
| Initial Access | T1190: Exploit Public-Facing Application | Exploitation of perimeter VPN / edge devices | Edge appliance syslog & flow logs |
| Discovery | T1087: Account Discovery | `net user /domain`, `net group "Domain Admins" /domain` | Windows Security 4688 / Sysmon 1 |
| Discovery | T1018: Remote System Discovery | `ping`, `nltest /dclist:` | Sysmon 1 |
| Credential Access | T1003.003: LSA Secrets / NTDS | `ntdsutil "ac i ntds" "ifm" "create full C:\Windows\Temp\pro" q q` | Process CommandLine containing `ntdsutil` + `ifm` |
| Lateral Movement | T1021.002: SMB/Windows Admin Shares | WMI and PowerShell remote execution | Sysmon 1 / Security 4624 Type 3 |
| Command and Control | T1090.002: External Proxy | Proxying traffic through compromised home SOHO routers (KV-Botnet) | Non-standard ASN traffic, anomalous residential IPs |

---

## 4. Empirical Threat Hunting Strategies
1. **NTDS.dit Extraction Hunting**: Monitor any process execution invoking `ntdsutil.exe` containing strings `ifm` or `create full`.
2. **Netsh Port Proxying**: Hunt for `netsh interface portproxy add v4tov4` commands which Volt Typhoon uses to bridge internal subnets.
