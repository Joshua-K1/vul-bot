import os
from dotenv import load_dotenv
from openai import OpenAI

def call_openai():

  load_dotenv()

  client = OpenAI(
    api_key = os.getenv('OPEN_AI_API_KEY')
  )

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
     {"role": "system", "content": "You are a cyber security engineer who is carrying out a security review of a solution, you are well spoken and have a keen eye for detail"},
     {"role": "user", "content": "Can you please give me information about the latest httpd package for RHEL OS"}
    ]
  )

  print(completion.choices[0].message)
