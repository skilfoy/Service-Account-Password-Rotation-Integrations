# Azure AD Service Principal Password Rotation

This example demonstrates how to rotate the password (client secret) for an Azure Active Directory service principal using the Microsoft Graph API.

## Prerequisites

- Access to Azure AD with permissions to manage service principals.
- A registered application in Azure AD with the necessary API permissions for Microsoft Graph.
- Python installed with `requests` library (`pip install requests`).

## Script Details

- **rotate_service_principal_password.py**: This Python script authenticates to the Microsoft Graph API, generates a new client secret for a service principal, and updates Azure AD with the new secret.

### Usage:

1. Clone this repository or download the script.
2. Update the script with your Azure AD tenant ID, client ID, client secret, and the service principal ID.
3. Run the script:

```bash
python rotate_service_principal_password.py
```

4. The script will output the new client secret, which can be used in your applications.

## Security Considerations

- Do not hardcode sensitive values such as client secrets in the script. Use environment variables or secure vaults.
- Ensure that the permissions granted to the Azure AD app are minimal, following the principle of least privilege.

