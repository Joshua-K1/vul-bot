from fastapi import FastAPI

app = FastAPI()


@app.get("/get-api")
def hello():
    return {

        "GET - Hello world!"
    }
