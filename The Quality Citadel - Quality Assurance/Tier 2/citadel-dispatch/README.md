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

This project is part of a larger monorepo. For instructions on how to clone only this specific project, please refer to the **[main repository's README.md](../../../README.md)**.

Once you have cloned the project, you can proceed with the setup:

1. **Navigate to the project directory:**
   ```bash
   cd "The Quality Citadel - Quality Assurance/Tier 2/citadel-dispatch"
   
2. **Create and activate a virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage
To run the full test suite, execute the following command from the root of the project directory:
```bash
pytest
```