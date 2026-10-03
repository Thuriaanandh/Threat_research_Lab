# Detection Engineering Principles & Architecture

Detection Engineering is the disciplined software engineering practice of designing, building, testing, tuning, and maintaining automated threat detection logic.

---

## 1. The Pyramid of Pain in Detection Engineering

David Bianco's Pyramid of Pain illustrates the amount of effort required by an adversary to circumvent specific detection mechanisms:

```
                  /                 /  \      TTPs (Behavioral Detection) [Hardest to Evade]
                /                   / Tools\    Tools & Utilities (LOLBAS, Mimikatz, Cobalt Strike)
              /--------             / Network  \  Network Artifacts (C2 URLs, User-Agents, JA3)
            / Domain Names\ Domain Names (DGA, Dynamic DNS)
           /  IP Addresses \ IP Addresses (Easily rotated cloud/proxy IPs)
          / Hash Values     \ Cryptographic Hashes [Trivial to Evade]
         ---------------------
```

* **High-Fidelity Engineering**: Focus detection logic at the **TTP and Tool behavior levels** (e.g., detecting memory injection or parent-process anomalies) rather than fragile hash matching.

---

## 2. Core Detection Metrics

To maintain an effective SOC and avoid alert fatigue, track the following metrics:

$$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$

$$\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$

* **Alert-to-Ticket Ratio**: Target > 85% actionable alerts.
* **Mean Time to Detect (MTTD)**: Time from initial execution to automated detection firing.

---

## 3. High-Fidelity Rule Structure

Every production detection rule must include:
1. **Metadata**: Unique UUID, Title, Author, Date, Severity (Low, Medium, High, Critical).
2. **Behavioral Logic**: Resilient selection criteria based on immutable adversary mechanics.
3. **Exclusions / Baseline Filters**: Explicitly defined legitimate enterprise processes.
4. **Contextual Enrichment**: Hostname, IP, username, MITRE ATT&CK technique tags.
5. **False Positive Documentation**: Anticipated benign business operations that could trigger the rule.
