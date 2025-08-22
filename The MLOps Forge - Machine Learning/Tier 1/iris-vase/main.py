# Dependencies
from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

# Creating a FastAPI app instance
app = FastAPI(title="Iris Species Prediction API", version="1.0.0")

# Loading the trained model and target names
print("Loading model artifacts...")
model = joblib.load('iris_model.joblib')
target_names = joblib.load('iris_target_names.joblib')
model_columns = ['sepal lenth (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print("Model artifacts successfully loaded.")

# Defining the input data model with Pydantic
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Defining the prediction endpoint
@app.post("/predict", tags=["Predictions"])
async def predict_species(features: IrisFeatures):
    """
    Predicts species of Iris based on input features.
    """
    # DF from the input features
    input_data = pd.DataFrame([features.model_dump().values()], columns=model_columns)

    # Prediction
    prediction_index = model.predict(input_data)[0]

    # Getting species name from the index
    species_name = target_names[prediction_index]

    return {"predicted_species": species_name}

# Confirming API with simple root endpoint
@app.get("/", tags=["General"])
async def read_root():
    return {"message": "Welcome to Iris Prediction API!"}