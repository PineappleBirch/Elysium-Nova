import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# --- Configuration ---
DATA_PATH = "data/"
DB_PATH = "vector_db/"
MODEL_NAME = "all-MiniLM-L6-v2"


def main():
    """
    Main function to run the ingestion pipeline.
    """
    print("--- Starting Ingestion Pipeline ---")

    # 1. Load Documents
    print(f"Loading documents from '{DATA_PATH}'...")
    documents = []
    for filename in os.listdir(DATA_PATH):
        if filename.endswith('.pdf'):
            file_path = os.path.join(DATA_PATH, filename)
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())
    print(f"Loaded {len(documents)} document pages.")

    # 2. Split Documents into Chunks
    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = text_splitter.split_documents(documents)
    print(f"Created {len(splits)} text chunks.")

    # 3. Create Embeddings and Store in ChromaDB
    print(f"Creating embeddings with '{MODEL_NAME}' model...")
    embedding_model = HuggingFaceEmbeddings(model_name=MODEL_NAME)

    print(f"Storing embeddings in ChromaDB at '{DB_PATH}'...")
    vector_store = Chroma.from_documents(
        documents=splits,
        embedding=embedding_model,
        persist_directory=DB_PATH
    )

    print("--- Ingestion Pipeline Finished Successfully ---")


if __name__ == '__main__':
    main()