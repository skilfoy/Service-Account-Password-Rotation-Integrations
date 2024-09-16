
# PowerShell Script to Rotate Azure AD Service Account Password
# This script rotates the password for a specified service account in Azure AD using the AzureAD PowerShell module.

# Install the AzureAD module if it's not already installed
# Install-Module -Name AzureAD

# Connect to Azure AD (requires login)
Connect-AzureAD

# Define the user (service account) whose password we want to rotate
$UserPrincipalName = "service-account@yourdomain.com"

# Generate a new password (you can customize the password generation logic as needed)
$NewPassword = "NewPassword-123!" + (Get-Random -Minimum 1000 -Maximum 9999)

# Set the new password for the user account
Set-AzureADUserPassword -ObjectId $UserPrincipalName -Password $NewPassword

# Enforce password change on next login (optional)
Set-AzureADUser -ObjectId $UserPrincipalName -PasswordPolicies DisablePasswordExpiration

Write-Output "Password rotated successfully for service account $UserPrincipalName"
Write-Output "New password is: $NewPassword"
