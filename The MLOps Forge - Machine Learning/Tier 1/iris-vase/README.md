# Project: Iris Vase

> A Tier 1 project in "The MLOps Forge" series. This project takes a machine learning API built with FastAPI ("Project: Iris Core") and containerizes it using Docker.

## Project Overview

This project demonstrates a fundamental skill in modern MLOps and software development: containerization. The goal is to package a Python web application, its dependencies, and its model files into a single, portable Docker image.

The `Dockerfile` provides a clear, step-by-step recipe for building the application, ensuring that it can be run consistently in any environment where Docker is installed. This solves the "it works on my machine" problem and is the first step toward scalable deployment.

## Features
- **Containerized Application:** The FastAPI application is fully containerized using Docker.
- **Reproducible Environment:** The `Dockerfile` ensures a consistent Python 3.11 environment with all necessary dependencies installed.
- **Port Mapping:** The container is configured to expose the application's port, making it accessible from the host machine.

## Technologies & Tools Used
- **Containerization:** Docker
- **Backend:** Python, FastAPI
- **Server:** Uvicorn

## Setup and Usage
This project is part of a larger monorepo. Please refer to the main repository's `README.md` for instructions on cloning individual projects.

1. **Prerequisites:** You must have Docker Desktop installed and running.
2. **Navigate to the project directory:**
   ```bash
   cd "The MLOps Forge - Machine Learning/Tier 1/iris-vase"
   ```
3. **Build the Docker Image:**
   ```bash
   docker build -t iris-vase-app .
   ```
4. **Run the Docker Container:**
   ```bash
   docker run -p 8000:8000 iris-vase-app
   ```
The API will now be running and accessible at `http://localhost:8000`. You can view the interactive documentation at `http://localhost:8000/docs`.