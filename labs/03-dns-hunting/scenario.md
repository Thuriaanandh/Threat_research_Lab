# Scenario: Whispers in the Recursive Resolver

Internal recursive DNS logs indicate an abnormal volume of TXT queries directed towards subdomains of an external apex domain `tunnel.c2server.org`. Additionally, several workstations are generating repeated `NXDOMAIN` query failures to high-entropy `.xyz` domains. You must inspect the DNS query telemetry, decode covert payloads, and differentiate tunneling from benign CDN or antivirus telemetry.
