# Twitter Sentiment Analysis Project

This project collects tweets from X app, preprocesses them, and performs sentiment analysis to classify tweets as positive, negative, or neutral. The project uses the Twitter API for data collection and `TextBlob` for sentiment analysis.

Im using x app Developer account for API access which you can sign up for free, but limited rate since it is free.

## Table of Contents
- [Twitter Sentiment Analysis Project](#twitter-sentiment-analysis-project)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Steps:](#steps)
  - [Usage](#usage)
  - [License](#license)

---

## Features
- Collect tweets from Twitter based on a specific query.
- Clean and preprocess text data for analysis.
- Perform sentiment analysis using `TextBlob`.
- Visualize sentiment distribution.

## Project Structure
```plaintext
twitter_sentiment_analysis/
├── config/
│   └── config.py            # Configuration file for API keys
├── data/
│   ├── tweets.csv           # Raw tweet data
│   ├── cleaned_tweets.csv   # Cleaned and preprocessed tweets
│   └── sentiment_analysis.csv # Sentiment analysis results
├── notebooks/
│   └── analysis.ipynb       # Jupyter notebook for analysis
├── src/
│   ├── data_collection.py   # Collects tweets from Twitter
│   ├── preprocess.py        # Preprocesses tweet text
│   └── sentiment_analysis.py # Analyzes sentiment of tweets
├── .env                     # Environment variables for API keys (ignored in .gitignore)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```
## Installation
Prerequisites
* Python 3.6 or above
* A Twitter Developer account for API access
## Steps:

* Clone this repository:

```bash
git clone https://github.com/EzioDEVio/twitter_sentiment_analysis.git
cd twitter_sentiment_analysis
```

* Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

* Install the dependencies:
```bash
pip install -r requirements.txt
```

* Set up your environment variables by creating a .env file:
```bash
API_KEY=your_api_key
API_SECRET=your_api_secret
ACCESS_TOKEN=your_access_token
ACCESS_SECRET=your_access_secret
BEARER_TOKEN=your_bearer_token
```

## Usage

* Data Collection
To collect tweets, run:
```bash
python -m src.data_collection
```
This script collects tweets based on your query and saves them in data/tweets.csv.

* Preprocessing
To clean the tweet data, run:

```bash
python -m src.preprocess
```

This step removes URLs, mentions, hashtags, and special characters, saving results to data/cleaned_tweets.csv.

* Sentiment Analysis
To perform sentiment analysis on the cleaned tweets, run:

```bash
python -m src.sentiment_analysis
```
This will classify each tweet as positive, neutral, or negative and save the results to data/sentiment_analysis.csv.

## License
This project is licensed under the MIT License.

