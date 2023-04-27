
import tweepy
import json
consumer_key = 'iN3Im21ozwb8EH8r0clqk4qMd'
consumer_secret = 'sqep91v7qv3UZaFanrx0degjLICXOPu6Fheutvn4iTULufK6sQ'
access_token = '80822144-b4NHGVdn0U5H400IUi6YtWYoyjHbEeztOoatHz0mB'
access_token_secret = 'Ky7oV2eVvxcEcBue031OO0yQbTVL5LKvUYtoVX3ZJikXz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
def search_tweets(query, count=100):
    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang='en', tweet_mode='extended').items(count):
        tweets.append(tweet._json)
    return tweets
    

query = "#BTC"
tweet_count = 100  # Set the number of tweets you want to fetch

btc_tweets = search_tweets(query, tweet_count)

for tweet in btc_tweets:
    print(json.dumps(tweet, indent=2))