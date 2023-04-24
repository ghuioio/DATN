import pika
import json
import time
from pymongo import MongoClient

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='crypto_tweets_queue')

# Load data from MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client["crypto_db"]
tweets_collection = db["crypto_tweets"]
tweets = list(tweets_collection.find())

# Send the data to RabbitMQ
tweet_count = 0
for tweet in tweets:
    if tweet_count >= 100:  # Limit to 100 tweets
        break
    tweet_count += 1
    tweet_json = json.dumps(tweet, default=str)
    channel.basic_publish(exchange='', routing_key='crypto_tweets_queue', body=tweet_json)

# Close the connection
connection.close()

