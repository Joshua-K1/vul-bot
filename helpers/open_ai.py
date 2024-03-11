import helpers.config as config
from dotenv import load_dotenv
from fastapi import HTTPException
from openai import OpenAI, OpenAIError
from logger.logger import event_logger

def call_openai(system_prompt, user_prompt, query):
  event_logger.info("Loading environment variables")
  load_dotenv()
  client = OpenAI(
    api_key = config.open_ai_api_key
  )

  try:
    event_logger.info("Calling OpenAI")
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
       {"role": "system", "content": system_prompt + query},
       {"role": "user", "content": user_prompt}
      ]
    )

    return completion.choices[0].message.content

  except OpenAIError as err:
    event_logger.error(err)
    raise HTTPException(status_code=503, detail="OpenAI Server Error")

  except Exception as err:
    event_logger.error(err)
    raise HTTPException(status_code=503, detail="An unexpected error has occured")

