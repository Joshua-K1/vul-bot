#! /usr/bin/env bash
set -e

# Change current working directory to be the root, regardless of how this script is invoked
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

# Add a command-line argument for the local flag
while getopts l: flag
do
    case "${flag}" in
        l) local=${OPTARG};;
    esac
done

# If the local flag is set to true then check if a user is already logged in
if [ "${local}" = "true" ]; then
  if az account show &> /dev/null; then
    echo "User is already logged in"
  else
    az login
  fi
fi

# Load environment variables from .env file
export $(cat .env | xargs)

# Change to the terraform directory
cd terraform/envs/latest 

# Plan terraform output
terraform plan -var="OPENAI_API_KEY=${OPENAI_AI_API_KEY}" -var="openai_api_url=${OPEN_AI_API_URL}" -var="system_api_key=${SYSTEM_API_KEY}" -var="azure_vault_id=${AZURE_VAULT_ID}" -out=out.tfplan