# Environment & Telemetry Dictionary

* **Target Host**: `WS-FIN-01` (IP: `10.0.1.45`)
* **Domain Controller**: `DC-01` (IP: `10.0.1.5`)
* **Suspect User**: `CORP\jdoe`
* **Log File**: `datasets/multi_source_telemetry.csv`

### Telemetry Field Schema
| Field Name | Type | Description |
| :--- | :--- | :--- |
| `timestamp` | ISO-8601 | High-precision UTC timestamp |
| `event_source` | String | Windows Security / Sysmon |
| `event_id` | Integer | Event ID (4624, 1, 3, 22) |
| `hostname` | String | Target workstation name |
| `user` | String | User principal or service account |
| `process_image` | String | Executing binary path |
| `command_line` | String | Full CLI command arguments |
| `dest_ip` | String | Destination IP address (if network event) |
| `dest_port` | Integer | Destination port |
| `query_name` | String | DNS domain queried (if DNS event) |
