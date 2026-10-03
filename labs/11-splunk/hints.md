# Tiered Investigation Hints
* Hint 1: Use rex field=CommandLine to extract regex patterns.
* Hint 2: Use streamstats current=f window=1 last(_time) to calculate time deltas.
* Hint 3: Use eval bytes_mb = bytes_out / 1024 / 1024.
