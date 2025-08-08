# Project: Iris Core

> A simple, robust web API built with FastAPI to serve a Scikit-learn model for Iris flower species classification. 
> This is a Tier 1 project in "The MLOps Forge" series of the Elysium Nova Project.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)

## Project Overview

This project serves as a foundational example of machine learning model deployment. 
It takes a pre-trained Scikit-learn model, wraps it in a FastAPI application, and exposes a single endpoint for real-time predictions. 
The primary goal is to demonstrate the core principles of serving a model as a RESTful API, including data validation and interactive documentation.

## Features
- Real-time classification of Iris species.
- Interactive API documentation via Swagger UI.
- Input data validation using Pydantic.
- Clean, modular code structure with separate training and serving scripts.

## Technologies Used
- **Backend:** Python, FastAPI
- **ML/Data:** Scikit-learn, Pandas, Joblib
- **Server:** Uvicorn

## Setup and Installation
To get this project running locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd project-iris-core
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate 
   # On Windows use `.\venv\Scripts\activate`
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command from the root of the project directory:
```bash
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`. You can access the interactive documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints
The main endpoint for this application is:

| Method | Endpoint    | Description                                       |
| :----- | :---------- | :------------------------------------------------ |
| `POST` | `/predict`  | Predicts the species of an Iris flower.           |

**Request Body Example:**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

## Screenshots
*(A screenshot of the interactive Swagger UI documentation)*

![Swagger UI Screenshot](assets/swagger_ui.png)