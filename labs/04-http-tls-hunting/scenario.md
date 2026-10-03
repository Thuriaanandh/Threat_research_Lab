# Scenario: Encrypted Shadows

An advanced implant has established an encrypted HTTPS C2 channel out of workstation `WS-HR-12`. Because the payload is TLS-encrypted, legacy perimeter firewalls saw only HTTPS port 443 traffic. However, your organization captures SSL handshake telemetry (SNI, JA3/JA4, Cipher Suites, Certificate Issuer) and HTTP forward proxy headers. Your task is to hunt down the encrypted C2 channel without needing to decrypt the payload on the wire.
