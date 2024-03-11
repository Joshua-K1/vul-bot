import helpers.config as config
from fastapi import FastAPI, Header, HTTPException
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from starlette.requests import Request
from starlette.responses import Response
from logger.logger import event_logger

async def authenticate(request: Request, call_next):
    x_api_consumer = request.headers.get('X-API-CONSUMER')
    x_api_key = request.headers.get('X-API-KEY')

    try:
        if x_api_consumer == 'system':
            if x_api_key == config.system_api_key:
                event_logger.info(f"Authenticated system consumer.")
                response = await call_next(request)
                return response
        else:
            # Lookup the consumer id against Azure Key Vault to get the key
            consumer_key = lookup_consumer_key(x_api_consumer)
            if x_api_key == consumer_key:
                event_logger.info(f"Authenticated consumer {x_api_consumer}.")
                response = await call_next(request)
                return response
    except:
        event_logger.warning(f"Failed to authenticate consumer {x_api_consumer}.")
        return Response(status_code=401)

# Get the consumer key from Azure Key Vault
def lookup_consumer_key(consumer_id):
    # Create a DefaultAzureCredential object
    credential = DefaultAzureCredential()

    # Create a SecretClient object
    secret_client = SecretClient(vault_url=config.azure_vault_id, credential=credential)

    # Get the secret value from Azure Key Vault
    secret_name = f"{consumer_id}"
    secret_value = secret_client.get_secret(secret_name).value

    return secret_value