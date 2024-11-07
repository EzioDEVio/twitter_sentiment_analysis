import time
import tweepy
import pandas as pd
from config.config import BEARER_TOKEN

# Set up Tweepy client with bearer token
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def collect_tweets(query, max_results=100):
    tweets_data = []
    retries = 3  # Number of retries allowed

    while retries > 0:
        try:
            tweets = client.search_recent_tweets(query=query, max_results=max_results)
            for tweet in tweets.data:
                tweets_data.append([tweet.id, tweet.text, tweet.created_at])
            break  # Exit loop if successful
        except tweepy.TooManyRequests as e:
            print("Rate limit exceeded. Waiting 15 minutes before retrying...")
            time.sleep(15 * 60)  # Wait for 15 minutes
            retries -= 1  # Decrement retry count

    # Convert to DataFrame and save if data was collected
    if tweets_data:
        df = pd.DataFrame(tweets_data, columns=["TweetID", "Text", "CreatedAt"])
        df.to_csv("data/tweets.csv", index=False)
        print(f"Saved {len(df)} tweets to data/tweets.csv")
    else:
        print("Failed to collect tweets due to rate limits.")
