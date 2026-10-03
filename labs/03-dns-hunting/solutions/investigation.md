# Investigation Solution: Lab 03
## 1. Exfiltrated Data Reconstructed
1. `c2VjcmV0LWtleS0wMQ==` -> `secret-key-01`
2. `YWRtaW46cGFzc3dvcmQxMjM=` -> `admin:password123`
3. `ZGF0YS1zdGFnaW5nLWNvbXBsZXRl` -> `data-staging-complete`

## 2. Threat Analysis
The endpoint `192.168.10.88` used DNS TXT queries to bypass standard egress proxy filtering, exfiltrating administrative credentials. Following exfiltration, fallback DGA resolution was initiated.
