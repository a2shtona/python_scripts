from openai import OpenAI
from dotenv import load_dotenv
import os
import json
load_dotenv()
client = OpenAI()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0125:aryzen::97mErX7U",
  messages=[
    {"role": "system", "content": "You are an Amazon Review Analysis chatbot, dedicated to evaluating the worth of a given review and discerning if it contains valuable insights, capable of influencing product improvements. My requirement involves merely identifying the value of the review, ranking it from low to high, excluding any explanatory outline. Thus, your response should be a simple, singular term."},
    {"role": "user", "content": "Hello"}
  ]
)
print(completion.choices[0].message.content)
with open('response/chat_test_response.json', 'w') as f:
    json.dump(completion.choices[0].message.dict(), f, indent=4)