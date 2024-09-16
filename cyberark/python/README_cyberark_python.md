# CyberArk Password Rotation (Python)

This Python script automates the process of rotating a service account password using the CyberArk REST API.

## Prerequisites

- Access to CyberArk API credentials (client ID, client secret).
- The `requests` Python library installed (`pip install requests`).
- Permissions to manage accounts in CyberArk.

## Script Details

- **rotate_password_cyberark.py**: This script connects to the CyberArk API, authenticates, and rotates the password for a specified service account.

### Usage:

1. Install the required Python libraries:
   ```bash
   pip install requests
   ```

2. Update the script with your CyberArk instance URL, client ID, client secret, and the account ID.

3. Run the script:
   ```bash
   python rotate_password_cyberark.py
   ```

4. The script will output the status of the password rotation.

## Security Considerations

- Always store sensitive information securely. Avoid hardcoding sensitive values like passwords in scripts.
- You can modify the script to pull passwords from a secure vault or environment variables.

