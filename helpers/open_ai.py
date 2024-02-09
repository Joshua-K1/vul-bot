import os
from dotenv import load_dotenv
from openai import OpenAI

def call_openai(system_prompt, user_prompt):

  load_dotenv()

  client = OpenAI(
    api_key = os.getenv('OPEN_AI_API_KEY')
  )

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
     {"role": "system", "content": system_prompt},
     {"role": "user", "content": user_prompt}
    ]
  )

  print(completion.choices[0].message)
  return completion.choices[0].message.content
