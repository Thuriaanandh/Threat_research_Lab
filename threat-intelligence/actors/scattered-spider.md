# Threat Actor Profile: Scattered Spider (UNC3944 / Octo Tempest / Starfraud)

## 1. Actor Overview
* **Attribution**: Financially motivated native English-speaking eCrime syndicate
* **Target Sectors**: Telecommunications, BPO, Hospitality, Critical Infrastructure, Technology
* **Operational Motivation**: Extortion, Ransomware deployment (ALPHV/BlackCat affiliate), corporate data theft
* **Primary Tactic**: Aggressive social engineering, IT Helpdesk vishing, SIM swapping, Okta identity compromise.

---

## 2. Key Adversary Mechanics
* **MFA Fatigue & Helpdesk Vishing**: Calling corporate helpdesks impersonating employees to request MFA device resets or password resets.
* **Identity Provider Takeover**: Modifying Okta or Entra ID Identity Providers (IdP) to route enterprise federated authentication through adversary-controlled servers.
* **Cloud Egress**: Utilizing commercial remote management tools (AnyDesk, TeamViewer, Splashtop) and cloud storage sync tools (rclone) to rapidly exfiltrate data.
