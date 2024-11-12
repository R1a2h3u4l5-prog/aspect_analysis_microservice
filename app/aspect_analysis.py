import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def extract_aspects(review):
    aspects = ["service", "food", "ambience", "cleanliness", "staff"]
    return aspects

def analyze_sentiment(review, aspect):
    score = sia.polarity_scores(review)["compound"]
    return score

def aspect_sentiment_scores(review):
    aspects = extract_aspects(review)
    scores = {aspect: analyze_sentiment(review, aspect) for aspect in aspects}
    return scores
