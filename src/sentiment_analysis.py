from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

def perform_sentiment_analysis():
    df = pd.read_csv("data/cleaned_tweets.csv")
    df["Sentiment"] = df["CleanedText"].apply(analyze_sentiment)
    df.to_csv("data/sentiment_analysis.csv", index=False)
    print("Sentiment analysis completed and results saved to data/sentiment_analysis.csv")

if __name__ == "__main__":
    perform_sentiment_analysis()
