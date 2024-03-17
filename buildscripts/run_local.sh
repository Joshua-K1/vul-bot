#! /usr/bin/env bash
set -e

# Change current working directory to be the root, regardless of how this script is invoked
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

# Load environment variables from .env file
export $(cat .env | xargs)

# Run the app
cd src || exit 1
uvicorn main:app --host 0.0.0.0 --port 8000