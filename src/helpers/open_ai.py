import helpers.config as config
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from logger.logger import event_logger

def call_openai(system_prompt, user_prompt, query):
  event_logger.info("Loading environment variables")
  load_dotenv()
  client = OpenAI(
    api_key = config.OPENAI_API_KEY
  )
 
  # Attempt call to OpenAI
  try:
    event_logger.info("Calling OpenAI")
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
       {"role": "system", "content": system_prompt},
       {"role": "user", "content": user_prompt + query}
      ]
    )

    # Return first message choice if successful
    return {"success": True, "data": completion.choices[0].message.content}

  # Catch exceptions and pass error back to main.py
  except OpenAIError as err:
    event_logger.error(err)
    return {"success": False, "error": str(err)}

  except Exception as err:
    event_logger.error(err)
    return {"success": False, "error": str(err)}
