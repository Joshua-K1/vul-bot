#! /usr/bin/env bash
set -e

# Change current working directory to be the root, regardless of how this script is invoked
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

# Go to terraform directory
cd terraform/envs/stable 

# Destroy terraform
terraform destroy -auto-approve -var="OPENAI_API_KEY=${OPENAI_AI_API_KEY}" -var="openai_api_url=${OPENAI_API_URL}" -var="system_api_key=${SYSTEM_API_KEY}" -var="azure_vault_id=${AZURE_VAULT_ID}"