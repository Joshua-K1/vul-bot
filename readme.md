Python API to ask ChatGPT about vulnerabilities and other fun stuff for DevOps.

## Usage

## Authentication
The authentication middleware works in two ways:
1. If the API is running locally, you can use the `.env` file to set the 'system' user API key.
   1. If the X-API-CONSUMER is 'system' then the local API key will be used.
2. If the API is running in Azure, it will use the Azure Key Vault to get the API key.
   1. If the X-API-CONSUMER is anything other than 'system' then the Azure Key Vault will be used.
   2. A lookup will be used to get the API key from the Key Vault using the X-API-CONSUMER as the identifier.


## Local Development
### Secrets setup
To run the API locally, you will need to create a `.env` file in the root of the project with the following content:
```
OPEN_AI_API_KEY=<your_openai_api_key>
SYSTEM_API_KEY=<your_system_api_key>
AZURE_VAULT_ID=<your_azure_key_vault_id>
```

### Local Setup
To run the API locally, you can use the following commands:

#### Requirements
To install the requirements:
```
make build-local
```

This installs:
```
-- fastapi
-- uvicorn
-- requests
-- pytest
-- openai
-- python-dotenv
-- azure-identity
-- azure-keyvault-secrets
-- starlette
```

#### Start Server
```
make run-local
```

### Docker
To run the API using Docker, you can use the following commands:

#### Build and Run
```
make build
make run
```


