# Threat Research & Hunting Curriculum Roadmap

This roadmap outlines structured learning pathways designed for aspiring **Threat Researchers**, **Managed Threat Hunters**, and **Detection Engineers**.

---

## 🧭 Learning Tracks

### Track 1: Threat Hunting Mastery (Focus: Empirical Discovery)
1. **Foundations**: Lab 01 (Hypothesis-Driven Hunting), Lab 08 (MITRE ATT&CK), Lab 09 (Threat Intelligence)
2. **Network Investigation**: Lab 02 (Network Hunting), Lab 03 (DNS Hunting), Lab 04 (HTTP/TLS Hunting)
3. **Host & OS Telemetry**: Lab 05 (Windows Telemetry & Sysmon), Lab 06 (Linux Telemetry), Lab 07 (Advanced Endpoint)
4. **Analytical Querying**: Lab 10 (KQL Masterclass), Lab 11 (Splunk SPL Masterclass)
5. **Modern Perimeters**: Lab 17 (Cloud Hunting), Lab 18 (Zscaler Zero Trust Model)
6. **Culmination**: Lab 20 (Capstone: Operation NightHawk)

### Track 2: Detection Engineering & Detection-as-Code (Focus: High-Fidelity Logic)
1. **Foundations**: Lab 05 (Windows Sysmon), Lab 08 (MITRE ATT&CK Data Components)
2. **Detection Core**: Lab 12 (Detection Engineering Principles), Lab 13 (Sigma Rule Engineering), Lab 14 (YARA Hunting)
3. **Optimization**: Lab 15 (Detection Tuning & Noise Reduction)
4. **Automation**: Lab 16 (Python Security Automation), Lab 19 (Detection-as-Code CI/CD Pipeline)

---

## 📅 Recommended 12-Week Study Schedule

| Week | Focus Area | Hands-on Labs | Key Deliverable |
| :---: | :--- | :--- | :--- |
| **1** | Hunting Foundations & ATT&CK | Labs 01, 08 | First hypothesis formulation & ATT&CK matrix mapping |
| **2** | Network Flows & Traffic Analysis | Lab 02 | Zeek flow triage & beaconing detection report |
| **3** | DNS Covert Channels & DGA | Lab 03 | High-entropy DNS hunting script & investigation |
| **4** | Encrypted Traffic & TLS Anomalies | Lab 04 | JA3/JA4 fingerprinting & proxy analysis |
| **5** | Windows Telemetry & Sysmon Deep Dive | Lab 05 | Process creation lineage & LSASS dumping detection |
| **6** | Linux Auditing & Privilege Escalation | Lab 06 | Auditd rule creation & web shell investigation |
| **7** | Threat Intelligence & Diamond Model | Lab 09 | Adversary dossier deconstruction (Volt Typhoon) |
| **8** | Query Mastery (KQL & SPL) | Labs 10, 11 | 30 completed operational hunting queries |
| **9** | Detection Engineering & Sigma | Labs 12, 13 | 5 production Sigma rules with regression tests |
| **10** | YARA & Detection Tuning | Labs 14, 15 | Noise reduction from 96% to <1% FP rate |
| **11** | Cloud & Zero Trust Security | Labs 16, 17, 18 | CloudTrail triage & Zscaler ZIA/ZPA telemetry hunt |
| **12** | Detection-as-Code & Capstone | Labs 19, 20 | Complete CI/CD deployment & Capstone Investigation Dossier |
