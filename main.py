import os

from fastapi import FastAPI
from openai import OpenAI
from environ import key
from models import UserCreate
from fastapi.responses import RedirectResponse
from fastapi import status



app = FastAPI()

openai_client = OpenAI(api_key=key)

@app.get("/health")
def root_controller():
    return {"status": "healthy"}


@app.get("/chat")
def chat_controler(prompt:str):
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    statement = response.choices[0].message.content
    return {"response": statement}


@app.post("/users")
def create_user(user: UserCreate):
    return {"username": user.username, "password": user.password}


@app.get("/", include_in_schema=False)
def docs_redirect_controller():
    return RedirectResponse(url="/docs", status_code=status.HTTP_303_SEE_OTHER)