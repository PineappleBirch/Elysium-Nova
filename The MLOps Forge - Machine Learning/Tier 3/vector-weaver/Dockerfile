# --- Stage 1: The Builder ---
# This stage builds the vector database from the source documents.
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies needed for ingestion
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the data and the ingestion script
COPY ./data ./data
COPY ingest.py .

# Run the ingestion script to create the vector_db
# This happens during the image build process
RUN python ingest.py


# --- Stage 2: The Final Application ---
# This stage creates the lean, final image for running the API.
FROM python:3.11-slim

WORKDIR /app

# Install dependencies needed for the API
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the pre-built vector database from the 'builder' stage
COPY --from=builder /app/vector_db ./vector_db

# Copy the FastAPI application code
COPY app.py .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI server
# --host 0.0.0.0 makes it accessible from outside the container
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]