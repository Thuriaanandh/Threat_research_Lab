# Tiered Investigation Hints
* Hint 1: Trace the sequence: Email -> WINWORD -> PowerShell -> LSASS -> Logon 4624 -> CloudTrail.
* Hint 2: Base64 string `dGVzdC1jMmJlYWNvbg==` decodes to `test-c2beacon`.
