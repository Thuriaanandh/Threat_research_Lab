# Scenario: Operation NightHawk
At 02:00 UTC, a sophisticated threat actor executed a multi-stage intrusion against the enterprise. The campaign began with an executive spearphishing email, progressed to in-memory credential theft, lateral movement via WMI across the internal network, covert DNS command-and-control, pivot into the corporate cloud environment, and exfiltration of sensitive financial databases.

Telemetry has been collected across all 4 operational planes:
1. Endpoint: Sysmon Event Logs
2. Network: DNS and Proxy Traffic
3. Identity: Active Directory Kerberos and Logon Audits
4. Cloud: AWS CloudTrail API Records

You must conduct a complete forensic investigation WITHOUT pre-disclosed answers. Reconstruct the end-to-end timeline, pinpoint all adversary TTPs, map them to MITRE ATT&CK, extract IOCs, engineer detection rules, and produce a professional Investigation Report.
