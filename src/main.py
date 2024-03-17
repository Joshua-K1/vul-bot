from uuid import uuid1, UUID
from fastapi import FastAPI, HTTPException
from pydantic.fields import Field
from logger.logger import event_logger, request_logger
from helpers.prompts import read_prompts
from helpers.open_ai import call_openai
from middleware.auth import authenticate
from pydantic import BaseModel

# Define pydantic model and include unique id per request
class OpenQuery(BaseModel):
    prompt: str
    request_id: UUID = Field(default_factory=uuid1)


app = FastAPI()

# Apply the authentication middleware to the app
app.middleware('http')(authenticate)

# GET - API Root
@app.get("/")
def hello():
    event_logger.info("API Root Called")
    return {
        "API Root"
    }

# POST - Read in prompt and search for vulnerabilities
@app.post("/vulnerability-check")
async def create_vul_query(vul_query: OpenQuery):
    # Read in prompts defined for vulnerability checks and make call to OpenAI
    prompt_dict = read_prompts("vulnerability-check")
    response = call_openai(prompt_dict["system"], prompt_dict["user"], vul_query.prompt)

    # If response is not successful, raise a 500 status code and log error in logs/requests.log
    if not response["success"]:
        error = response["error"]
        request_logger.error(f"Request ID: {vul_query.request_id} Error: {error}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error. Request ID: {vul_query.request_id}")
    else: 
        
        return response["data"]

# POST - Read in prompt string and search for any relevant information
@app.post("/info-check")
async def create_info_query(info_query: OpenQuery):
    # Read in prompts defined for info check and make call to OpenAI
    prompt_dict = read_prompts("info-check")
    response = call_openai(prompt_dict["system"], prompt_dict["user"], info_query.prompt)

    # If response is not successful, raise a 500 status code and log error in logs/requests.log
    if not response["success"]:
        error = response["error"]
        request_logger.error(f"Request ID: {info_query.request_id} Error: {error}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error. Request ID: {info_query.request_id}")
    else: 
        
        return response["data"]
