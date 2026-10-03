# Tiered Investigation Hints
* Hint 1: Use summarize count() by bin(TimeGenerated, 5m).
* Hint 2: Use join kind=inner to correlate logon failures with success.
* Hint 3: Use make_list to collect distinct destinations.
