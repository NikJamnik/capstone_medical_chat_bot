import os
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
print("✅ FastAPI server started!")

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    question = request.question
    answer = f"Here will be the answer of the RAG model to the question: {question}"
    return {"answer": answer}

@app.get("/ping")
async def ping():
    return {"ping": "pong"}
