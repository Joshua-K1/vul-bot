from fastapi import FastAPI
from logger.logger import event_logger
from helpers.prompts import read_prompts
from helpers.open_ai import call_openai

app = FastAPI()

# GET - API Root
@app.get("/")
def hello():
    event_logger.info("API Root Called")
    return {
        "API Root"
    }

# GET - Take in query string and search for vulnerabilities
@app.get("/vulnerability-check")
def vul_check(query: str):
    event_logger.info("Vulnerability Check Called")
    prompt_dict = read_prompts("vulnerability-check")
    response = call_openai(prompt_dict["system"], prompt_dict["user"], query)

    if response is not None:
        return {
            "This is the query string: " + query,
            "System Prompt: " +  prompt_dict["system"],
            "User Prompt: " +  prompt_dict["user"],
            response
        }

# GET - Take in query string and search for any relevant information
@app.get("/info-check")
def info_check(query: str):
    event_logger.info("Information Check Called")
    prompt_dict = read_prompts("info-check")
    response = call_openai(prompt_dict["system"], prompt_dict["user"], query)

    if response is not None:
        return {
            "This is the query string: " + query,
            "System Prompt: " +  prompt_dict["system"],
            "User Prompt: " +  prompt_dict["user"],
        }
