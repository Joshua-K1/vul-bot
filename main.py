from fastapi import FastAPI

app = FastAPI()

# GET - API Root
@app.get("/")
def hello():
    return {
        "API Root"
    }

# GET - Take in query string and search
@app.get("/vulnerability-check")
def vul_check(query_string: str):
    return {
        "This is the query string: " + query_string

    }
