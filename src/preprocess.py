import re
import pandas as pd

def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)     # Remove mentions
    text = re.sub(r'#\w+', '', text)     # Remove hashtags
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.lower().strip()

def preprocess_tweets():
    df = pd.read_csv("data/tweets.csv")
    df["CleanedText"] = df["Text"].apply(clean_text)
    df.to_csv("data/cleaned_tweets.csv", index=False)
    print("Tweets have been cleaned and saved to data/cleaned_tweets.csv")

if __name__ == "__main__":
    preprocess_tweets()
