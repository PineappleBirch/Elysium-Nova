from transformers import pipeline

# 1. Create a sentiment-analysis pipeline
# This will download the model and tokenizer on the first run
print("Loading model...")
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
print("Model loaded successfully.")

# 2. Use the pipeline to make a prediction
text_to_analyze = "We are building a sentiment analysis app and it is going to be amazing!"
result = classifier(text_to_analyze)

# 3. Print the result
print("\nAnalysis Result:")
print(result)
