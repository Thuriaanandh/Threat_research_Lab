# Investigation Solution: Lab 02
* **Target IP**: `192.168.10.10`
* **Open Ports Identified**: 80, 445, 3389
* **Brute Force**: 25 SMB connections executed across 5 seconds (5 attempts/sec) indicating automated credential spraying.
* **Beaconing Analysis**: 10 outbound SSL connections to `198.51.100.23:443` with an average interval of 30.25 seconds and variance < 0.3s. High-confidence C2 beacon.
