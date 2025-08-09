# Project: Citadel Dispatch

> A Tier 2 project in "The Quality Citadel" series. This project introduces automated API testing using Python with the `pytest` and `requests` libraries.

## Project Overview

This project demonstrates the fundamentals of automated API testing. It involves writing a suite of tests for a public REST API (JSONPlaceholder) to verify the correctness of its endpoints.

The test suite includes verifications for successful status codes (200 OK, 201 Created) and validates the structure and content of the JSON responses for both GET and POST requests. The project showcases a professional workflow, including a structured test file and a detailed dependency list.

## Automated Scenarios
- **GET /users:**
  - Verified that the endpoint returns a `200 OK` status code.
  - Verified that the response body is a list containing 10 user objects.
- **POST /posts:**
  - Verified that sending a valid payload returns a `201 Created` status code.
  - Verified that the response body contains the same data that was sent in the request.

## Technologies & Tools Used
- **Testing Framework:** pytest
- **HTTP Library:** requests
- **Language:** Python

## Setup and Installation

This project is part of a larger monorepo. To clone only this specific project, please follow these steps using Git's Sparse Checkout feature.

1. **Create and navigate into a new directory for the project:**
   ```bash
   mkdir citadel-dispatch
   cd citadel-dispatch
   ```
2. **Initialize an empty Git repository:**
   ```bash
   git init
   ```
3. **Connect to the remote Elysium-Nova repository:**
   ```bash
   git remote add origin https://github.com/PineappleBirch/Elysium-Nova.git
   ```
4. **Enable Sparse Checkout and define the project path:**
   ```bash
   git config core.sparseCheckout true
   echo "The Quality Citadel - Quality Assurance/Tier 2/citadel-dispatch/" >> .git/info/sparse-checkout
   ```
5. **Pull the project files:**
   ```bash
   git pull origin main
   ```
6. **Navigate to the final project directory and proceed with setup:**
   ```bash
   cd "The Quality Citadel - Quality Assurance/Tier 2/citadel-dispatch"
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage
To run the full test suite, execute the following command from the root of the project directory:
```bash
pytest
```