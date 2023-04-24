import pika, sys, os, json, csv
import snscrape.modules.twitter as sntwitter
from recrawl import recrawl_user_data
from ranking import get_ranking 
import pymongo
import time
# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["crypto_db"]
tweets_collection = db["crypto_tweets"]


def update_document(unique_id, new_data):
    tweets_collection.update_one(
        {"url": unique_id},
        {"$set": {
            "user.followersCount": new_data["followersCount"],
            "likeCount": new_data["likeCount"],
            "quoteCount": new_data["quoteCount"],
            "replyCount": new_data["replyCount"],
            "retweetCount": new_data["retweetCount"]
        }}
    )



def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='crypto_tweets_queue')

    def callback(ch, method, properties, body):
        data = json.loads(body)
        recrawl_user_data(data.url)
        with open('recrawled_data.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                tweet_id = row["url"]
                update_document(tweet_id, row)
        print(" [x] Received %r" % body)


    channel.basic_consume(queue='crypto_tweets_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


main()