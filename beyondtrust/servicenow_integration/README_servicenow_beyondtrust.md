# ServiceNow-BeyondTrust Integration for Password Rotation

This Python script demonstrates how to integrate ServiceNow with BeyondTrust's Password Safe to automate service account password rotations and log the results in ServiceNow.

## Prerequisites

- Access to both BeyondTrust and ServiceNow APIs.
- The `requests` Python library installed (`pip install requests`).
- API credentials and appropriate permissions in both systems.

## Script Details

- **servicenow_beyondtrust_integration.py**: This script rotates passwords in BeyondTrust and logs the result in ServiceNow.

### Usage:

1. Install the required Python libraries:
   ```bash
   pip install requests
   ```

2. Update the script with your BeyondTrust and ServiceNow instance URLs, API tokens, and account ID.

3. Run the script:
   ```bash
   python servicenow_beyondtrust_integration.py
   ```

4. The script will rotate the password in BeyondTrust and log the outcome in ServiceNow.

## Security Considerations

- Store sensitive information such as API keys securely, using environment variables or a secret management system.
- Ensure that API tokens have the minimum necessary permissions to perform these actions.

