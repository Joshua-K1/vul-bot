include .env

.PHONY: all

build-local:
	pip install -r requirements.txt

build:
	docker build -t vul-bot -f Dockerfile .

run-local:
	export $(cat .env | xargs)
	uvicorn main:app --host 0.0.0.0 --port 8000

run:
	export $(cat .env | xargs)
	docker stop vul-bot || true && docker rm vul-bot || true
	docker run --name vul-bot --rm -e OPEN_AI_API_KEY=${OPEN_AI_API_KEY} -e SYSTEM_API_KEY=${SYSTEM_API_KEY} -e AZURE_VAULT_ID=${AZURE_VAULT_ID} -p 8000:8000 -v ${PWD}/logs:/app/logs vul-bot 