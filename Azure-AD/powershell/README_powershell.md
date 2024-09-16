# Azure AD Service Account Password Rotation (PowerShell)

This PowerShell script automates the process of rotating a service account's password in Azure Active Directory using the AzureAD PowerShell module.

## Prerequisites

- AzureAD PowerShell module installed (`Install-Module -Name AzureAD`).
- Admin access to Azure AD and permissions to reset user passwords.

## Script Details

- **rotate_service_account_password.ps1**: This PowerShell script connects to Azure AD, generates a new password for the specified service account, and updates the account with the new password.

### Usage:

1. Install the AzureAD module if it's not already installed:
   
   ```powershell
   Install-Module -Name AzureAD
   ```

2. Run the script and log in to Azure AD:
   
   ```powershell
   ./rotate_service_account_password.ps1
   ```

3. The script will generate a new password for the specified service account and output the new password.

## Security Considerations

- Always store sensitive information securely. Avoid hardcoding sensitive values like passwords in scripts.
- You can modify the script to pull passwords from a secure vault or environment variables.

