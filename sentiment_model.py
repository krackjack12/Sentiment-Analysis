# sentiment_model.py
from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def predict_sentiment(text):
    result = sentiment_pipeline(text)
    sentiment = result[0]['label']
    return sentiment
