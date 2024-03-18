import helpers.config as config
from helpers import azure
from fastapi import Depends, FastAPI, Header, HTTPException
from starlette.requests import Request
from starlette.responses import Response
from logger.logger import event_logger
from key_store import retieve_secret_local


async def authenticate(request: Request, call_next):
    x_api_consumer = request.headers.get('X-API-CONSUMER')
    x_api_key = request.headers.get('X-API-KEY')

    try:
        if x_api_consumer == retieve_secret_local("system"):
            if x_api_key == config.system_api_key:
                event_logger.info(f"Authenticated system consumer.")
                response = await call_next(request)
                return response
        else:
            # Lookup the consumer id against Azure Key Vault to get the key
            consumer_key = lookup_consumer_key(x_api_consumer)
            if x_api_key == consumer_key and consumer_key is not None:
                event_logger.info(f"Authenticated consumer {x_api_consumer}.")
                response = await call_next(request)
                return response
    except:
        event_logger.warning(f"Failed to authenticate consumer {x_api_consumer}.")
        return Response(status_code=401)

# Get the consumer key from Azure Key Vault
def lookup_consumer_key(consumer_id):
    secret_client = azure.build_secret_client() 
    # Get the secret value from Azure Key Vault
    secret_name = f"{consumer_id}"
    if secret_client:
        secret_value = secret_client.get_secret(secret_name).value

        return secret_value
    else: 

        return None
