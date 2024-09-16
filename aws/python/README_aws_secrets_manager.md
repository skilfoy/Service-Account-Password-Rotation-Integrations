# AWS Secrets Manager Password Rotation (Python)

This Python script automates the rotation of service account passwords stored in AWS Secrets Manager.

## Prerequisites

- Access to AWS Secrets Manager.
- The `boto3` Python library installed (`pip install boto3`).
- Appropriate IAM permissions to manage secrets in AWS.

## Script Details

- **rotate_secrets_manager.py**: This script retrieves a service account secret, updates the password, and stores the updated secret back in AWS Secrets Manager.

### Usage:

1. Install the required Python libraries:
   ```bash
   pip install boto3
   ```

2. Update the script with your AWS Secrets Manager secret ID and the new password.

3. Run the script:
   ```bash
   python rotate_secrets_manager.py
   ```

4. The script will update the password stored in AWS Secrets Manager.

## Security Considerations

- Store sensitive information such as passwords and secret IDs securely, using environment variables or secret management systems.
- Ensure that the IAM permissions for managing secrets follow the principle of least privilege.

