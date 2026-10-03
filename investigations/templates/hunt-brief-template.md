# Threat Hunt Brief: [Hunt Operation Name]

## 1. Hunt Hypothesis
**Hypothesis Statement**: 
*"Adversaries may execute [specific utility/technique] under the guise of [benign appearance] in order to achieve [tactical objective] on [target asset class]."*

## 2. Trigger & Threat Intelligence
* **Source Intelligence**: [e.g., Mandiant APT29 Report, ThreatLabz Emerging Threat Advisory]
* **Target Adversary / Malware**: [e.g., Volt Typhoon, BlackCat Ransomware]
* **Target Environment / Subnets**: [e.g., Internal Server Subnet 10.100.0.0/16]

## 3. Required Telemetry & Data Sources
* **Telemetry Source**: [e.g., Sysmon Process Creation EID 1]
* **Required Fields**: `Image`, `CommandLine`, `ParentImage`, `User`, `UtcTime`
* **Retention Window**: 30 Days

## 4. Query & Hunting Logic
```sql
-- KQL or SPL query implementation
```

## 5. Baselines & Long-Tail Outliers
* **Baseline Normal**: [Describe frequent benign matches to be stacked out]
* **Outlier Criteria**: [Describe criteria distinguishing anomalous behavior]

## 6. Findings Summary
* **Total Hosts Scanned**: [e.g., 1,450]
* **Candidate Anomalies Isolated**: [e.g., 3]
* **Confirmed Malicious Incidents**: [e.g., 1]
* **New Detections Engineered**: [Sigma Rule Link]
