# Environment & Telemetry Dictionary

* **Rogue Host**: `192.168.10.45`
* **Internal Subnet**: `192.168.10.0/24`
* **Dataset**: `datasets/zeek_conn_flows.csv`

### Zeek Flow Schema
* `ts`: Epoch timestamp
* `id_orig_h`, `id_orig_p`: Source IP and port
* `id_resp_h`, `id_resp_p`: Destination IP and port
* `proto`, `service`: Protocol and detected application service
* `duration`: Session duration in seconds
* `orig_bytes`, `resp_bytes`: Payload bytes transferred
* `conn_state`: Connection status (`S0`=SYN attempt without reply, `SF`=Normal completion)
* `history`: TCP flag history
