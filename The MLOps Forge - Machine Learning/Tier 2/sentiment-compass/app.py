import streamlit as st
from transformers import pipeline

# Set the title and a small description for the web app
st.title("Sentiment Compass 🧭")
st.write(
    "A simple web app to analyze the sentiment of your text. "
    "Powered by Hugging Face Transformers."
)

# Cache the model loading to prevent reloading on every user interaction
@st.cache_resource
def load_model():
    """Loads the sentiment analysis model from Hugging Face."""
    print("Loading model...")
    model = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )
    print("Model loaded.")
    return model

classifier = load_model()

# Create a text area for user input
user_input = st.text_area("Enter text for analysis:")

# Create a button to trigger the analysis
if st.button("Analyze Sentiment"):
    if user_input:
        # Get the prediction from the model
        result = classifier(user_input)[0]
        label = result['label']
        score = result['score']

        # Display the results
        st.write(f"**Sentiment:** {label}")
        st.write(f"**Confidence Score:** {score:.4f}")
    else:
        # Show a message if the user clicks the button without entering text
        st.warning("Please enter some text to analyze.")