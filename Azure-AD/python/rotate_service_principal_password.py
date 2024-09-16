import requests
import json
import datetime

# Azure AD and Microsoft Graph API configuration
tenant_id = 'your_tenant_id'
client_id = 'your_client_id'
client_secret = 'your_client_secret'
service_principal_id = 'your_service_principal_id'

# Authenticate to Microsoft Graph API
def authenticate():
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    body = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(url, headers=headers, data=body)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception(f"Authentication failed: {response.status_code} - {response.text}")

# Generate a new service principal password (client secret)
def rotate_service_principal_password():
    access_token = authenticate()
    url = f"https://graph.microsoft.com/v1.0/servicePrincipals/{service_principal_id}/addPassword"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Define the new password validity period and properties
    new_password = "new-strong-password-789!"
    expiration_date = (datetime.datetime.now() + datetime.timedelta(days=365)).isoformat()

    payload = {
        "passwordCredential": {
            "displayName": "Automated Password Rotation",
            "secretText": new_password,
            "endDateTime": expiration_date
        }
    }
    
    # Send request to add the new password (client secret)
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 204:
        print(f"Password successfully rotated for service principal ID {service_principal_id}")
        return new_password
    else:
        print(f"Error rotating password: {response.status_code} - {response.text}")
        return None

# Execute the password rotation
if __name__ == "__main__":
    try:
        new_secret = rotate_service_principal_password()
        if new_secret:
            # Application-specific actions (e.g., updating configuration files) can go here
            print(f"New client secret: {new_secret}")
    except Exception as e:
        print(f"Error: {e}")
