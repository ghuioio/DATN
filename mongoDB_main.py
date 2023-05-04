import pymongo
import csv

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["crypto_db"]
tweets_collection = db["crypto_tweets_0305"]

def update_document(unique_id, new_data):
    tweets_collection.update_one(
        {"tweet_id": unique_id},
        {"$set": new_data}
    )

# Import CSV data into MongoDB
with open('100coins100_0305tweets.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        tweets_collection.insert_one(row)