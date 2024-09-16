
import requests
import json

# BeyondTrust API Configuration
beyondtrust_url = "https://your-beyondtrust-instance/api/public/v3/accounts"
client_id = "your_client_id"
client_secret = "your_client_secret"
access_token = None

# Authenticate to BeyondTrust API
def authenticate():
    global access_token
    auth_url = "https://your-beyondtrust-instance/oauth2/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    
    response = requests.post(auth_url, data=payload)
    if response.status_code == 200:
        access_token = response.json().get('access_token')
    else:
        raise Exception(f"Authentication failed: {response.status_code} - {response.text}")

# Rotate the password for a service account
def rotate_password(account_id, new_password):
    global access_token
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Define the payload for password rotation
    payload = {
        "newPassword": new_password
    }
    
    # Send request to rotate the password
    response = requests.put(f'{beyondtrust_url}/{account_id}/password', headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print(f"Password rotated successfully for account ID {account_id}")
    else:
        print(f"Error rotating password: {response.status_code} - {response.text}")

# Main function to execute the rotation
if __name__ == "__main__":
    authenticate()
    rotate_password("123456789", "new-strong-password-456!")
