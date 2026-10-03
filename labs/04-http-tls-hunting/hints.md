# Tiered Investigation Hints
* **Hint 1**: Standard enterprise browsers share predictable JA3 hashes. Rare JA3 hashes associated with minimal traffic volumes warrant immediate investigation.
* **Hint 2**: Self-signed certificates (`CN=Untrusted Root CA`) in conjunction with custom User-Agents are typical of default Cobalt Strike or Metasploit configurations.
