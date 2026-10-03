# Hands-on Investigation Tasks

1. **Hypothesis Formulation**: Write a 2-sentence hypothesis detailing the suspected adversary execution vector.
2. **Authentication Audit**: Filter `event_id == 4624` to find all user logins outside regular office hours (08:00 - 18:00 UTC).
3. **Execution Triage**: For the suspicious session, list all child processes executed in chronological order.
4. **Command De-obfuscation**: Extract the Base64 string from the PowerShell command line and decode it. What is its intent?
5. **Network Corroboration**: Find the DNS domain resolved by PowerShell and the corresponding external destination IP and port.
6. **Timeline Assembly**: Construct a complete 5-step timeline of the compromise.
7. **Detection Engineering**: Author a Sigma rule detecting PowerShell spawned with `-NoP` and `-Enc`.
