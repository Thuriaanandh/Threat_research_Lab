# Scenario: Compromise on the Web Tier
An external-facing Apache web server (SRV-WEB-02) hosting a legacy customer portal exhibited unusual outbound socket connections. Preliminary alerts from the host-based audit daemon (auditd) show www-data executing interactive bash commands, modifying /etc/sudoers, and creating a persistent systemd service unit.
