from fastapi import FastAPI
from logger.logger import event_logger
from helpers.prompts import read_prompts

app = FastAPI()

# GET - API Root
@app.get("/")
def hello():
    event_logger.info("API Root Called")
    return {
        "API Root"
    }

# GET - Take in query string and search
@app.get("/vulnerability-check")
def vul_check(query: str):
    event_logger.info("Vulnerability Check Called")
    prompt_string = read_prompts("vulnerability-check")
    return {
        "This is the query string: " + query,
        "This is the prompt that will be added: " + prompt_string

    }

@app.get("/info-check")
def info_check(query: str):
    event_logger.info("Information Check Called")
    prompt_string = read_prompts("info-check")
    return {
        "This is the query string: " + query,
        "This is the prompt that will be added: " + prompt_string

    }
