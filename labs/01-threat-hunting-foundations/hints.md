# Tiered Investigation Hints

* **Hint 1 (Conceptual)**: Attackers operating after-hours frequently use command-line discovery (`whoami`, `net user`) before establishing outbound connectivity.
* **Hint 2 (Telemetry Pivot)**: Filter by `user == "CORP\\jdoe"` and observe the sequence of `event_id` 1 (Process Creation) immediately following the 03:14:22Z logon.
* **Hint 3 (Query Construction)**: To decode base64 in Python: `import base64; base64.b64decode("JABj...").decode('utf-16le')`. PowerShell encoded commands are UTF-16LE.
