import snscrape.modules.twitter as sntwitter
import csv
import os
import pandas as pd



def recrawl_user_data(tweet_url):
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(tweet_url).get_items()):
        if tweet.url == tweet_url:
            return tweet.user.followersCount, tweet.likeCount, tweet.quoteCount, tweet.replyCount, tweet.retweetCount
            break 

# Main function
if __name__ == "__main__":
    # Load the CSV file
    data = pd.read_csv('100coin100tweets.csv', encoding='utf-8')
    print(data.iloc[0].url)
    print(recrawl_user_data(data.iloc[0].url))
