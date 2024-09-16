
import boto3
import json

# Rotate a service account password in AWS Secrets Manager
def rotate_secret(secret_id, new_password):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_id)
    secret = json.loads(response['SecretString'])
    
    # Update the password for the service account
    secret['password'] = new_password
    
    # Update the secret in AWS Secrets Manager
    client.put_secret_value(
        SecretId=secret_id,
        SecretString=json.dumps(secret)
    )
    print(f"Password rotated for {secret_id}")

# Trigger a password rotation
if __name__ == "__main__":
    rotate_secret('my-service-account-secret-id', 'new-strong-password123!')
