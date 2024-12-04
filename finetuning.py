from dotenv import load_dotenv
from openai import OpenAI
import os
import json

# load .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Instantiate client with the API key
client = OpenAI(api_key=api_key)
model="ft:gpt-3.5-turbo-0125:aryzen::97lUwbDH"
# Specify the path to your file
filename = "data/prompts.jsonl"
print("Loading file:", filename)
# Upload the file
upload_response = client.files.create(file=open(filename, "rb"), purpose="fine-tune")
with open('response/upload_response.json', 'w') as f:
    json.dump(upload_response.dict(), f, indent=4)
# Get the file ID from the upload response
file_id = upload_response.id

# Create fine-tuning job
fine_tuning_response = client.fine_tuning.jobs.create(
    training_file=file_id,
    model=model
)

# Save the fine-tuning response to a file
with open('response/fine_tuning_response.json', 'w') as f:
    json.dump(fine_tuning_response.dict(), f, indent=4)

print("Response saved to fine_tuning_response.json")

# ft:gpt-3.5-turbo-0125:aryzen::93Phf7x2
# ft:gpt-3.5-turbo-0125:aryzen::93PMx1pD
# ft:gpt-3.5-turbo-0125:aryzen::948c216F
# ft:gpt-3.5-turbo-0125:aryzen::97lUwbDH
# ft:gpt-3.5-turbo-0125:aryzen::97mErX7U