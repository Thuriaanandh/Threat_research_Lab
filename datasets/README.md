# Enterprise Threat Telemetry Datasets Catalog

This catalog documents the security telemetry datasets utilized across the **Threat Research & Hunting Detection Lab**.

---

## 1. Datasets Directory Structure

```text
datasets/
├── README.md                  # Schema definitions, usage constraints, and source catalog
├── network/                   # Zeek conn/http/ssl logs, NetFlow, Suricata alerts
├── dns/                       # High-entropy DNS, DGA queries, and tunneling traces
├── windows/                   # Sysmon (EID 1, 3, 10, 11), Windows Security Event Logs (4688, 4624)
├── linux/                     # Auditd (SYSCALL, EXECVE) and /var/log/auth.log
├── authentication/            # Active Directory Kerberos/NTLM and Entra ID sign-in events
└── cloud/                     # AWS CloudTrail JSON, Azure Activity, and GCP Audit logs
```

---

## 2. Reputable Public Telemetry Repositories

For extended deep-dive investigations beyond the synthetic datasets provided in each lab module, consult these public repositories:

| Repository Name | Focus Area | Access Link | Recommended Labs |
| :--- | :--- | :--- | :--- |
| **Malware Traffic Analysis** | Real-world PCAP, exploit kit, and malware traffic | [malware-traffic-analysis.net](https://www.malware-traffic-analysis.net/) | Lab 02, Lab 04 |
| **Splunk Boss of the SOC (BOTS)** | Multi-tier enterprise breach telemetry (Win, Net, Cloud) | [github.com/splunk/botsv3](https://github.com/splunk/botsv3) | Lab 11, Lab 20 |
| **Mordor Project (OTRF)** | Pre-recorded security events (Sysmon, Security, Linux) | [mordordesign.com](https://mordordesign.com/) | Lab 05, Lab 06, Lab 07 |
| **EVTX-ATTACK-SAMPLES** | Target EVTX files executing explicit MITRE ATT&CK TTPs | [github.com/sbousseaden/EVTX-ATTACK-SAMPLES](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES) | Lab 08, Lab 13 |
| **Stratosphere IPS / CTU** | Labeled malware and botnet capture datasets | [stratosphereips.org](https://www.stratosphereips.org/datasets-overview) | Lab 02, Lab 03 |
| **CyberDefenders Artifacts** | Curated community challenge dumps and memory images | [cyberdefenders.org](https://cyberdefenders.org/) | Lab 07, Lab 16 |
