import os
from logger.logger import event_logger

try:
    # Retrieve the OPENAI_API_KEY from environment variables
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    # Retrieve the SYSTEM_API_KEY from environment variables
    system_api_key = os.environ.get("SYSTEM_API_KEY")
    # Retrieve the AZURE_VAULT_ID from environment variables
    azure_vault_id = os.environ.get("AZURE_VAULT_ID")
    # Retrieve the USE_LOCAL_STORE from envrionment variables
    use_local_store = os.environ.get("USE_LOCAL_STORE")

except:
    event_logger.error(f"Unable to retrieve environment variables. Make sure the .env file exists and has the correct permissions.")
