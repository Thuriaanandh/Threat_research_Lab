# Tuning Solution: Lab 15
* Initial State: 5,000 alerts (12 TP, 4,988 FP) -> Precision: 0.24%
* Tuned Logic: Excluded SCCM and health check scripts; required suspicious parent or encoded arguments.
* Final State: 12 alerts (12 TP, 0 FP) -> Precision: 100%, Recall: 100%
* False Positive Reduction: 100% of noise eliminated.
