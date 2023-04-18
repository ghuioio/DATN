import snscrape.modules.twitter as sntwitter
import csv
import os

def get_user_data(tweet_url):
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(tweet_url).get_items()):
        if tweet.url == tweet_url:
            return tweet.user.followersCount, tweet.likeCount, tweet.quoteCount, tweet.replyCount, tweet.retweetCount
            break 

# Main function
if __name__ == "__main__":
    print(get_user_data('https://twitter.com/Hroshid746/status/1644340708424450048'))
