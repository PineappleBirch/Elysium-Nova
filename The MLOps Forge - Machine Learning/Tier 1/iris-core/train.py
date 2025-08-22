# Dependencies
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

print("Training script started...")

# Loading the Iris dataset from sk-learn
iris = load_iris()
X, y = iris.data, iris.target

# Creating a DataFrame for a quick preview
df = pd.DataFrame(X, columns=iris.feature_names)
print("Dataset successfully loaded. Preview: ")
print(df.head(), end='\n\n')

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialising and training the Logistic Regression model
model = LogisticRegression(max_iter=200)
print("\nTraining model...")
model.fit(X_train, y_train)
print("Model trained successfully.")

# Evaluating the model
accuracy = model.score(X_test, y_test)
print(f"Model accuracy - test set: {accuracy:.2f}")

# Saving the trained model to a file
model_filename = 'iris_model.joblib'
joblib.dump(model, model_filename)
print(f"\nModel saved to '{model_filename}'")

# Saving the target (species) names for use in the API
target_names_filename = 'iris_target_names.joblib'
joblib.dump(iris.target_names.tolist(), target_names_filename)
print(f"\nTarget names saved to '{target_names_filename}'")

print("\nTraining script finished.")