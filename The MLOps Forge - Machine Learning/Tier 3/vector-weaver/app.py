# app.py

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

# Import our RAG components
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# Load environment variables
load_dotenv()

# --- FastAPI App Initialization ---
app = FastAPI(
    title="Vector Weaver API",
    description="An API for querying a RAG pipeline built with LangChain and ChromaDB.",
    version="1.0.0",
)

# --- Pydantic Models for Request and Response ---
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

# --- RAG Chain Initialization (runs once on startup) ---
print("INFO: Initializing RAG chain...")
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = Chroma(persist_directory="vector_db/", embedding_function=embedding_model)
llm = ChatGroq(model="llama3-8b-8192", api_key=os.getenv("GROQ_API_KEY"))

prompt = PromptTemplate(
    template="""
    Answer the following question based only on the provided context.
    If the answer is not in the context, say you don't know.

    Context: {context}
    Question: {input}
    """,
    input_variables=["context", "input"],
)

document_chain = create_stuff_documents_chain(llm, prompt)
retriever = vector_store.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)
print("INFO: RAG chain initialized successfully.")

# --- API Endpoints ---
@app.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """
    Accepts a user's question and returns a context-based answer.
    """
    print(f"Received query: {request.question}")
    response = retrieval_chain.invoke({"input": request.question})
    return {"answer": response["answer"]}