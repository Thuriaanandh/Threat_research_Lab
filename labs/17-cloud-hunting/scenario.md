# Scenario: Breach in the Cloud Tenant
An attacker compromised credentials for AWS IAM user `dev-intern`. CloudTrail logs reveal the user created new programmatic access keys, modified bucket policies, and invoked `GetObject` on sensitive financial spreadsheets. Simultaneously, Azure Entra ID recorded impossible travel sign-ins from an offshore IP address.
