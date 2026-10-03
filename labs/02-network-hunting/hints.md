# Tiered Investigation Hints
* **Hint 1**: In Zeek, `conn_state == 'S0'` indicates a SYN packet sent without a SYN-ACK returned, characteristic of closed ports during a port scan.
* **Hint 2**: To calculate beaconing intervals in Python: compute the difference between sorted connection timestamps: `diffs = [t[i+1] - t[i] for i in range(len(t)-1)]`.
* **Hint 3**: A low standard deviation in connection deltas indicates automated programmatic beaconing rather than human interaction.
