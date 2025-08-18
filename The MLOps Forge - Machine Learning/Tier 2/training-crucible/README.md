# Project: Training Crucible

### The MLOps Forge - Tier 2

---

## 1. Project Overview

Training Crucible is an automated machine learning pipeline written in Python. The script handles the entire initial modeling workflow: automatically downloading a dataset, splitting it for training and testing, training a classification model, evaluating its performance, and saving the resulting model artifact and performance metrics.

This project demonstrates a foundational MLOps practice by creating a reproducible, automated, and self-contained training process that can be executed with a single command.

## 2. Technologies Used

- **Python 3.11+**
- **Scikit-learn:** For the dataset, model (`LogisticRegression`), and evaluation metrics.
- **Pandas:** For data manipulation and structuring.
- **Joblib:** For serializing and saving the trained model object.

## 3. Pipeline Steps

The pipeline script is orchestrated by `main.py` and performs the following steps in sequence:

1.  **Get Data:** Loads the Iris dataset from scikit-learn.
2.  **Split Data:** Splits the data into 80% training and 20% testing sets.
3.  **Train Model:** Trains a Logistic Regression classifier on the training data.
4.  **Evaluate & Save:** Evaluates the model on the test set and saves the accuracy score and the trained model to an `output/` directory.

## 4. Setup and Installation

This project is part of a larger monorepo. For instructions on how to clone only this specific project, please refer to the **[main repository's README.md](../../../README.md)**.

Once you have the project directory, you can proceed with the local setup:

1.  **Navigate to the project directory:**
    ```bash
    cd "The MLOps Forge - Machine Learning/Tier 2/training-crucible"
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 5. Running the Pipeline

To run the entire training pipeline, execute the main script:

```bash
python main.py
```

## 6. Output Artifacts

After a successful run, the following artifacts will be saved in the `output/` directory:

- **`model.joblib`**: The serialized, trained scikit-learn model object.
- **`metrics.json`**: A JSON file containing the model's performance metrics (e.g., accuracy).