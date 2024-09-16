
import requests
import json

# BeyondTrust API Configuration
beyondtrust_url = "https://your-beyondtrust-instance/api/public/v3/accounts"
client_id = "your_client_id"
client_secret = "your_client_secret"
access_token = None

# ServiceNow API Configuration (mock setup, adjust as needed)
servicenow_url = "https://your-servicenow-instance/api"
servicenow_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_servicenow_token'
}

# Authenticate to BeyondTrust API
def authenticate_beyondtrust():
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

# Rotate the password for a service account in BeyondTrust
def rotate_password_beyondtrust(account_id, new_password):
    global access_token
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "newPassword": new_password
    }
    
    response = requests.put(f'{beyondtrust_url}/{account_id}/password', headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print(f"Password rotated successfully for account ID {account_id}")
        return True
    else:
        print(f"Error rotating password: {response.status_code} - {response.text}")
        return False

# Log the result in ServiceNow
def log_in_servicenow(account_id, success):
    data = {
        "account_id": account_id,
        "rotation_status": "success" if success else "failed"
    }
    
    response = requests.post(f"{servicenow_url}/log_rotation", headers=servicenow_headers, data=json.dumps(data))
    if response.status_code == 200:
        print(f"Logged result in ServiceNow for account ID {account_id}")
    else:
        print(f"Failed to log result in ServiceNow: {response.text}")

# Main function for integrating ServiceNow and BeyondTrust
def integrate_servicenow_beyondtrust(account_id, new_password):
    authenticate_beyondtrust()
    success = rotate_password_beyondtrust(account_id, new_password)
    log_in_servicenow(account_id, success)

# Example usage
if __name__ == "__main__":
    integrate_servicenow_beyondtrust("123456789", "new-strong-password-456!")
