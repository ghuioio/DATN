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
for tweet in tweets:
    tweet_json = json.dumps(tweet, default=str)
    channel.basic_publish(exchange='', routing_key='crypto_tweets_queue', body=tweet_json)

# Close the connection
connection.close()

# Sleep for 1 day before re-crawling
time.sleep(60 * 60 * 24)
