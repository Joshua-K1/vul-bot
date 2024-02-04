from fastapi import FastAPI
from helpers.prompts import read_prompts

app = FastAPI()

# GET - API Root
@app.get("/")
def hello():
    return {
        "API Root"
    }

# GET - Take in query string and search
@app.get("/vulnerability-check")
def vul_check(query: str):

    prompt_string = read_prompts("vulnerability-check")
    return {
        "This is the query string: " + query,
        "This is the prompt that will be added: " + prompt_string

    }
