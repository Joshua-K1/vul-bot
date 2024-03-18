from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import helpers.config as config

# Build Key Vault Secret Client Object
def build_secret_client():
    if config.azure_vault_id is not None:
        credential = DefaultAzureCredential()
        secret_client = SecretClient(vault_url=config.azure_vault_id, credential=credential)

        return secret_client
    else:
        return None
