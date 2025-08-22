import pandas as pd
from sklearn.datasets import load_iris
import os

# Create data directory
os.makedirs("data", exist_ok=True)

# Load dataset from scikit-learn
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Save to a CSV file in the 'data' folder
df.to_csv("data/iris.csv", index=False)

print("Dataset successfully created at 'data/iris.csv'")