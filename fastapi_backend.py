from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
import os


app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-mpnet-base-v2")
vectorstore = PineconeVectorStore(
    index_name = "dermatologist-v2",
    embedding = embedding,
    namespace = "clinical-derm"
)
llm = ChatOpenAI(model = "gpt-3.5-turbo", temperature = 0)
qa = RetrievalQA.from_chain_type(llm = llm, retriever = vectorstore.as_retriever(), return_source_documents = True)

@app.post("/ask")
async def ask(request: QuestionRequest):
    result = qa.invoke({"query": request.question})
    return {"answer": result["result"]}

@app.get("/ping")
async def ping():
    return {"message": "RAG backend is live!"}
