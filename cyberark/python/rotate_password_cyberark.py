
import requests
import json

# CyberArk API Configuration
cyberark_url = "https://your-cyberark-instance/api/accounts"
client_id = "your_client_id"
client_secret = "your_client_secret"
access_token = None

# Authenticate to CyberArk API
def authenticate():
    global access_token
    auth_url = "https://your-cyberark-instance/oauth2/token"
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

# Rotate the password for a service account in CyberArk
def rotate_password(account_id, new_password):
    global access_token
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "newPassword": new_password
    }
    
    response = requests.put(f'{cyberark_url}/{account_id}/password', headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print(f"Password rotated successfully for account ID {account_id}")
    else:
        print(f"Error rotating password: {response.status_code} - {response.text}")

# Main function to execute the password rotation
if __name__ == "__main__":
    authenticate()
    rotate_password("123456789", "new-strong-password-456!")
