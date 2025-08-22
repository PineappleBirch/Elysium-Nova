import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import json
import os


def get_data():
    """
    Loads the Iris dataset from a local CSV file.
    """
    print("INFO: Loading Iris dataset from data/iris.csv...")
    # The path needs to be relative to the root of the project, not src/
    df = pd.read_csv("data/iris.csv")
    X = df.drop("target", axis=1)
    y = df["target"]
    print("INFO: Dataset loaded successfully.")
    return X, y


def split_data(X, y):
    """
    Splits the feature and target data into training and testing sets.
    """
    print("INFO: Splitting data into training and testing sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print("INFO: Data split successfully.")
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    """
    Initializes and trains a Logistic Regression model.
    """
    print("INFO: Training Logistic Regression model...")
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)
    print("INFO: Model training complete.")
    return model


def evaluate_and_save_artifacts(model, X_test, y_test):
    """
    Evaluates the model and saves the performance metrics and model artifact.
    """
    print("INFO: Evaluating model performance...")
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"INFO: Model accuracy on test set: {accuracy:.4f}")

    # Create an output directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Save metrics to a JSON file
    metrics = {"accuracy": accuracy}
    metrics_path = os.path.join(output_dir, "metrics.json")
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=4)
    print(f"INFO: Metrics saved to '{metrics_path}'")

    # Save the trained model
    model_path = os.path.join(output_dir, "model.joblib")
    joblib.dump(model, model_path)
    print(f"INFO: Model saved to '{model_path}'")