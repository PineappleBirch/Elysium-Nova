import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
DB_PATH = "vector_db/"
MODEL_NAME = "all-MiniLM-L6-v2"
LLM_MODEL = "llama3-8b-8192"


def main():
    """
    Main function to query the RAG pipeline.
    """
    # Initialize the embedding model
    embedding_model = HuggingFaceEmbeddings(model_name=MODEL_NAME)

    # Load the vector store from the persisted directory
    vector_store = Chroma(persist_directory=DB_PATH, embedding_function=embedding_model)

    # Initialize the LLM
    llm = ChatGroq(model=LLM_MODEL, api_key=os.getenv("GROQ_API_KEY"))

    # Define the prompt template
    prompt = PromptTemplate(
        template="""
        Answer the following question based only on the provided context.
        Think step-by-step and provide a detailed answer.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        Context: 
        {context}

        Question: 
        {input}
        """,
        input_variables=["context", "input"],
    )

    # Create the retrieval chain
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vector_store.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # --- Ask a Question ---
    question = "What is a solution to the double-spending problem?"
    print(f"Querying the knowledge base: '{question}'")

    # Invoke the chain
    response = retrieval_chain.invoke({"input": question})

    print("\n--- Answer ---")
    print(response["answer"])
    print("----------------")


if __name__ == '__main__':
    main()