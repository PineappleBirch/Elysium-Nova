import json
import sys

# Define our performance threshold
ACCURACY_THRESHOLD = 0.9

# Read the metrics from the output file
try:
    with open("output/metrics.json") as f:
        metrics = json.load(f)
except FileNotFoundError:
    print("Error: 'output/metrics.json' not found. Did the training pipeline run?")
    sys.exit(1)

accuracy = metrics.get("accuracy")

# Check if the accuracy meets our threshold
if accuracy is not None and accuracy >= ACCURACY_THRESHOLD:
    print(f"Success: Model accuracy ({accuracy:.4f}) is above the threshold ({ACCURACY_THRESHOLD}).")
    sys.exit(0)
else:
    print(f"Failure: Model accuracy ({accuracy:.4f}) is below the threshold ({ACCURACY_THRESHOLD}).")
    sys.exit(1)