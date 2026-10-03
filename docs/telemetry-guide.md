# Security Telemetry Taxonomy & Field Guide

Comprehensive reference guide for endpoint, network, identity, and cloud telemetry sources utilized throughout the research laboratory.

---

## 1. Windows Endpoint Telemetry

### 1.1 Microsoft Sysmon (System Monitor)
Sysmon provides high-fidelity kernel-level endpoint activity monitoring.

| Event ID | Event Name | Core Investigation Value | Critical Fields |
| :---: | :--- | :--- | :--- |
| **1** | Process Creation | Primary telemetry for execution, CLI arguments, process ancestry | `Image`, `CommandLine`, `ParentImage`, `ParentCommandLine`, `User`, `Hashes` |
| **3** | Network Connection | Correlates endpoint process execution directly to outbound sockets | `Image`, `SourceIp`, `DestinationIp`, `DestinationPort`, `Protocol` |
| **7** | Image Loaded | Detects DLL side-loading, injected modules, reflective DLL loading | `Image`, `ImageLoaded`, `Hashes`, `Signed`, `SignatureStatus` |
| **8** | CreateRemoteThread | Detects process injection, thread hijacking, shellcode injection | `SourceImage`, `TargetImage`, `NewThreadId`, `StartAddress` |
| **10** | ProcessAccess | Uncovers credential dumping (e.g., reading LSASS memory) | `SourceImage`, `TargetImage`, `GrantedAccess`, `CallTrace` |
| **11** | FileCreate | Identifies dropped payloads, staging directories, web shells | `TargetFilename`, `Image`, `CreationUtcTime` |
| **12/13**| RegistryEvent | Tracks persistence mechanisms (Run keys, Winlogon, Services) | `EventType`, `TargetObject`, `Details` |
| **22** | DNSEvent | Correlates host process directly with DNS domain resolutions | `Image`, `QueryName`, `QueryStatus`, `QueryResults` |

### 1.2 Windows Security Event Logs
Standard Active Directory and Windows workstation security audit log.

* **4624 (Successful Logon)**: Inspect `LogonType` (Type 2: Interactive, Type 3: Network, Type 10: RemoteInteractive/RDP).
* **4625 (Failed Logon)**: Identify brute force or password spraying attempts via `FailureReason` and `Status`.
* **4672 (Special Privileges Assigned)**: Detects elevated administrative token assignment upon logon.
* **4688 (Process Creation)**: Standard audit log; requires "Include command line in process creation events" GPO enabled.
* **4698 (Scheduled Task Created)**: Tracks adversary persistence via Windows Task Scheduler.
* **7045 (Service Installed)**: System event log indicating new Windows service registration (e.g., PsExec, lateral movement).

---

## 2. Linux Telemetry & Auditd

Linux kernel auditing via `auditd` captures low-level syscalls:

* **SYSCALL (`type=SYSCALL`)**: Records execution context, UID, GID, syscall number (e.g., `execve`, `ptrace`, `connect`).
* **EXECVE (`type=EXECVE`)**: Captures complete command line arguments passed to executed binaries (`a0`, `a1`, `a2`).
* **PROCTITLE (`type=PROCTITLE`)**: The full title of the executing command.
* **`auth.log` / `secure`**: Tracks SSH authentications (`Accepted password`, `Failed password`), PAM session openings, and `sudo` command executions.

---

## 3. Network Telemetry

### 3.1 Zeek (Bro) Network Analysis Framework
* **`conn.log`**: Protocol-agnostic session records. Crucial fields: `id.orig_h`, `id.resp_h`, `id.resp_p`, `proto`, `duration`, `orig_bytes`, `resp_bytes`, `conn_state`, `history`.
* **`dns.log`**: DNS requests and resolutions. Crucial fields: `query`, `qtype_name`, `rcode_name`, `answers`, `TTLs`.
* **`http.log`**: Unencrypted HTTP metadata. Crucial fields: `method`, `host`, `uri`, `user_agent`, `status_code`, `response_body_len`.
* **`ssl.log`**: TLS handshake telemetry. Crucial fields: `server_name` (SNI), `subject`, `issuer`, `ja3`, `ja3s`, `cipher`.

---

## 4. Cloud & Identity Telemetry

### 4.1 AWS CloudTrail
JSON-structured API activity records:
* `eventName`: API action (e.g., `ConsoleLogin`, `CreateAccessKey`, `GetObject`, `PutBucketPolicy`).
* `userIdentity`: ARN, principal ID, account ID, access key ID.
* `sourceIPAddress`: Client IP initiating the API call.
* `requestParameters`: Detailed arguments (e.g., targeted S3 bucket, IAM policy document).

### 4.2 Microsoft Entra ID (Azure AD)
* `SigninLogs`: UserPrincipalName, IPAddress, Location (City, Country), ConditionalAccessStatus, DeviceDetail, RiskLevel.
* `AuditLogs`: Administrative changes to roles, enterprise applications, and service principals.
