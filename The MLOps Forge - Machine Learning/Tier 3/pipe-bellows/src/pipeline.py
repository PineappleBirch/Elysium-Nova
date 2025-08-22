import joblib
import json
import os
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def get_data():
    """
    Loads the Iris dataset from scikit-learn.

    Returns:
        tuple: A tuple containing:
            - X (pd.DataFrame): The feature data.
            - y (pd.Series): The target data.
    """
    print("INFO: Loading Iris dataset...")
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name='target')
    print("INFO: Dataset loaded successfully.")
    return X, y


def split_data(X, y):
    """
    Splits the feature and target data into training and testing sets.

    Args:
        X (pd.DataFrame): The feature data.
        y (pd.Series): The target data.

    Returns:
        tuple: A tuple containing the split data:
               (X_train, X_test, y_train, y_test).
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

    Args:
        X_train (pd.DataFrame): The training feature data.
        y_train (pd.Series): The training target data.

    Returns:
        The trained model object.
    """
    print("INFO: Training Logistic Regression model...")
    # We set max_iter to 200 to ensure the model converges
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)
    print("INFO: Model training complete.")
    return model


def evaluate_and_save_artifacts(model, X_test, y_test):
    """
    Evaluates the model on the test set and saves the performance
    metrics and the model artifact.

    Args:
        model: The trained model object.
        X_test (pd.DataFrame): The testing feature data.
        y_test (pd.Series): The testing target data.
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


if __name__ == '__main__':
    X_data, y_data = get_data()

    X_train, X_test, y_train, y_test = split_data(X_data, y_data)

    model = train_model(X_train, y_train)

    evaluate_and_save_artifacts(model, X_test, y_test)

    print("\n--- Pipeline Test Run Complete ---")