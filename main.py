from typing import Optional
from fastapi import FastAPI
app= FastAPI()
@app.get("/")
def hello_world():
    return "Hi, I am currently dealing with FastAPI"