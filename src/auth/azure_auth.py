from fastapi import Request, HTTPException, Depends
from azure.identity import ClientSecretCredential
from azure.core.exceptions import AzureError
from config.loader import config

# Load tenant_id, client_id, and client_secret from config
tenant_id = config["azure"]["tenant_id"]
client_id = config["azure"]["client_id"]
client_secret = config["azure"].get("client_secret")  # Ensure this is added to your config if needed

def verify_azure_identity(request: Request):
    # Get the Authorization token from the request header
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

    # Extract the actual token
    token = token.split("Bearer ")[1]

    # Authenticate the token using Azure credentials
    try:
        credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
        # Validate the token (this is a placeholder; actual validation depends on your use case)
        access_token = credential.get_token(f"https://management.azure.com/.default")
        if not access_token:
            raise HTTPException(status_code=401, detail="Invalid token")
    except AzureError as e:
        raise HTTPException(status_code=500, detail=f"Azure authentication failed: {str(e)}")

    return True