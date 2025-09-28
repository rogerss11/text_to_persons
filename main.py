from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/v1/extract-persons")
def campusai_extract_persons(text: TextInput):
    pass


load_dotenv()
CAMPUSAI_API_KEY = os.getenv("CAMPUSAI_API_KEY")

client = OpenAI(
    api_key=CAMPUSAI_API_KEY,
    base_url="https://campusai.compute.dtu.dk/api"
)

history = [{"role": "user", "content": "Hello, who won the world series in 2020?"}]
print("Enter ’exit’ to end the session.")

while True :
# Prompt the user
user_input = input(" You : ")
if user_input.lower() == "exit":
    break
history.append({"role": "user", "content": user_input})
response = client.chat.completions.create(
    model="gemma3:latest",
    messages=history,
    stream=False  # explicitly disable streaming
)
reply = response.choices[0].message.content
print(f"Assistant: {reply}" + "\n" + "-" * 40)
history.append({"role": "assistant", "content": reply})