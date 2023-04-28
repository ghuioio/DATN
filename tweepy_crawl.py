
import tweepy
import json, csv, time
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
        tweet_data = {
            'coin': query,
            'name': tweet.user.name,
            'id': tweet.id_str,
            'url': f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id_str}",
            'date': str(tweet.created_at),
            'content': tweet.full_text,
            'userId': tweet.user.id_str,
            'followerCount': tweet.user.followers_count,
            'likeCount': tweet.favorite_count,
            'retweetCount': tweet.retweet_count
        }
        tweets.append(tweet_data)
    return tweets

def write_header_to_csv(filename):
    fieldnames = [
        'coin', 'name', 'id', 'url', 'date', 'content', 'userId',
        'followerCount', 'likeCount', 'retweetCount'
    ]

    with open(filename, mode='w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

def append_tweets_to_csv(tweets, filename):
    fieldnames = [
        'coin', 'name', 'id', 'url', 'date', 'content', 'userId',
        'followerCount', 'likeCount', 'retweetCount'
    ]

    with open(filename, mode='a', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for tweet in tweets:
            writer.writerow(tweet)

coinList = ['BTC','ETH','USDT', 'BNB','USDC','XRP', 'ADA', 'DOGE', 'STETH', 'MATIC',
            'SOL', 'DOT', 'BUSD', 'LTC', 'SHIB', 'TRX','AVAX', 'DAI', 'UNI', 'WBTC',
            'LINK','TON','ATOM','LEO','ETC','XMR','XLM','OKB','BCH','FIL',
            'LDO','TUSD','APT','HBAR','QNT','VET','CRO','NEAR','ALGO','APE',
            'ARB','ICP','EOS','FTM','GRT','SAND','AAVE','MANA','STX','THETA',
            'FRAX','EGLD','FLOW','XTZ','EDGT','AXS','IMX','RPL','NEO',
            'KCS','CRV','USDP','CFX', 'KLAY','BIT','LUNC','GT','USDD','WBT'
            'OP','BSV','CAKE','FXS','CHZ','GMX','MINA','MIOTA','MKR','DASH',
            'XEC','BTT','HT','BGB','XDC','CETH','KAS','TKX','PAXG','TWT',
            'XAUT','XRD','AGIX','CUSDC','ZIL','ENJ','RNDR','RUNE','INJ','RETH'
            ]
tweet_count = 100
output_filename = "tweepytweets.csv"
batch_size = 5

write_header_to_csv(output_filename)

for i in range(0, len(coinList), batch_size):
    batch = coinList[i:i + batch_size]
    for coin in batch:
        query = f"#{coin}"
        print(f"Fetching tweets for {query}")
        coin_tweets = search_tweets(query, tweet_count)
        append_tweets_to_csv(coin_tweets, output_filename)

    if i + batch_size < len(coinList):
        print("Waiting for 5 minutes before continuing...")
        time.sleep(300)

print(f"Data written to {output_filename}")