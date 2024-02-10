import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from logger.logger import event_logger

def call_openai(system_prompt, user_prompt, query):
  load_dotenv()
  client = OpenAI(
    api_key = os.getenv('OPEN_AI_API_KEY')
  )

  try:
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
    return None

  except Exception as err:
    event_logger.error(err)
    return None

