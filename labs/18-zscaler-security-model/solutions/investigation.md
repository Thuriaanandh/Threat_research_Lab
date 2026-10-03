# Zero Trust Investigation Solution: Lab 18
1. **ZIA Threat Block**: Trojan.CobaltStrike blocked from `update-service-c2.net/payload.exe` via SSL inspection.
2. **ZPA Policy Enforcement**: Compromised host attempted lateral RDP connection to `App-Server-Prod.internal:3389`; ZPA blocked the request because the user was not in the authorized Access Policy group.
3. **Architecture Impact**: Micro-segmentation prevented lateral expansion into production tier despite endpoint compromise.
