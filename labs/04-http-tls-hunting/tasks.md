# Hands-on Investigation Tasks
1. Extract and perform frequency analysis on all `user_agent` strings. Which one is an outlier?
2. Inspect the `ja3` hashes. Identify the unique fingerprint associated with the suspicious connection.
3. Review the certificate issuer details. What flags it as untrusted?
4. Calculate the delta between successive C2 connections. What is the beacon interval and jitter percentage?
5. Author a Sigma rule or Splunk query to alert on anomalous JA3 fingerprints communicating with untrusted certificates.
