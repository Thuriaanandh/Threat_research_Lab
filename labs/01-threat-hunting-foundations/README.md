# Lab 01: Threat Hunting Foundations

* **Difficulty**: 🟢 Beginner
* **Estimated Time**: 1.5 Hours
* **Focus**: Hypothesis-Driven Hunting vs IOC Matching, Multi-Source Correlation
* **Telemetry Sources**: Authentication, Process Creation (Sysmon EID 1), DNS (Sysmon EID 22), Network Sockets (Sysmon EID 3)

## Overview
In this foundational lab, you transition from reactive alert-triaging to proactive hypothesis-driven threat hunting. An employee account (`jdoe`) has exhibited subtle anomalies that bypassed traditional signature-based alerting. You will formulate a testable hunting hypothesis, query multi-source telemetry, reconstruct the adversary timeline, extract indicators of compromise, and engineer a behavioral detection.
