#! /usr/bin/env bash
set -e

# Change current working directory to be the root, regardless of how this script is invoked
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

# Load environment variables from .env file
export $(cat .env | xargs)

# Stop any current running and remove existing containers
docker stop vul-bot || true && docker rm vul-bot || true

# Run the app
docker run --name vul-bot --rm -e OPENAI_API_KEY=${OPENAI_API_KEY} -e SYSTEM_API_KEY=${SYSTEM_API_KEY} -e AZURE_VAULT_ID=${AZURE_VAULT_ID} -p 8000:8000 -v ${PWD}/logs:/app/logs vul-bot 
