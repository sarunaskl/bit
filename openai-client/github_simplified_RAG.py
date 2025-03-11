import os
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from rich import print

load_dotenv()


client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key = os.getenv("GITHUB_TOKEN"),
)

information = "Jaunius Pinelis is a great developer and loves to code. Lives in Vilnius, Lithuania."

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "system", "content": "This is information for you to work with: " + information},
        {"role": "user", "content": "Where does Jaunius Pinelis live?"},
    ],
)

event = completion.choices[0].message
print(event)