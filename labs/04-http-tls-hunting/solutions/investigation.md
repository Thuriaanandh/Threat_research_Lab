# Investigation Solution: Lab 04
* **Outlier User-Agent**: `CustomC2/2.1 (Implant)`
* **Adversary JA3 Fingerprint**: `6734f3743167022204a700501aabc052`
* **Adversary Infrastructure**: `198.51.100.99:443` (SNI: `telemetry-cloud-sync.com`)
* **Beacon Profile**: ~31-second interval with +/- 5% jitter.
* **Architectural Insight**: Deploying TLS/SSL inspection (e.g. via Zscaler ZIA) enables the inspection of the decrypted HTTP request, stripping the TLS evasion shield.
