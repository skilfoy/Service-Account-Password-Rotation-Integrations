# Service Account Password Rotation Integrations

This repository contains various examples and scripts for automating service account password rotations across different platforms, including Azure Active Directory, BeyondTrust, CyberArk, and AWS. These integrations demonstrate how to programmatically manage password rotations for service accounts, ensuring security and compliance in automated environments.

## Contents

### 1. Azure Active Directory (Azure AD)
- **Python Example (Microsoft Graph API)**: Automates password rotation for Azure AD service principals using the Microsoft Graph API.
- **PowerShell Script (Azure AD PowerShell Module)**: Rotates passwords for user accounts (service accounts) in Azure AD using the AzureAD PowerShell module.

### 2. BeyondTrust (Password Safe)
- **Python Example (BeyondTrust API)**: Programmatically rotate service account passwords using BeyondTrust's Password Safe API.
- **ServiceNow Integration**: Example integration between ServiceNow and BeyondTrust to trigger password rotations as part of a workflow.

### 3. CyberArk
- **Python Example (CyberArk API)**: Automate password rotation for service accounts using the CyberArk REST API.
- **Cloud Integration (AWS Secrets Manager)**: A custom integration with AWS Secrets Manager to manage service account password rotation for cloud applications.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Service-Account-Password-Rotation-Integrations.git
   ```

2. Navigate to the relevant folder based on the platform or tool you are integrating with.

3. Review the documentation for each example to understand dependencies and prerequisites:
   - **Azure AD**: Requires access to Microsoft Graph API and appropriate permissions.
   - **BeyondTrust**: Requires API credentials and permissions in BeyondTrust Password Safe.
   - **CyberArk**: Requires CyberArk API access and service account permissions.
   - **AWS**: Requires AWS Secrets Manager configuration.

4. Update the script with your environment-specific values (e.g., client IDs, secrets, account IDs).

## Dependencies

Ensure that you have the required libraries and dependencies installed for each integration.

### Python:
- Requests
- Boto3 (for AWS Secrets Manager)

### PowerShell:
- AzureAD PowerShell Module

## Security Considerations

- Always store sensitive information (like client secrets and access tokens) securely. Avoid hardcoding them directly in scripts.
- Ensure the principle of least privilege when configuring API permissions.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

## Contributions

Feel free to open issues or submit pull requests if you have any improvements or additional integrations you'd like to contribute.

---

**Author**: Sean Kilfoy  
**Purpose**: Provide examples for integrating service account password rotation into PAM solutions.
