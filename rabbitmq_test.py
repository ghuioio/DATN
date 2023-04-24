import pika
import json
import time

def callback(ch, method, properties, body):
    # Process the tweet data
    tweet = json.loads(body)
    print("Received tweet:", tweet)

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='crypto_tweets_queue')

# Add the 1-day delay before consuming messages
print("Waiting for 1 day before processing messages...")
time.sleep(60)
print("Starting to process messages")

# Start consuming messages from the queue
channel.basic_consume(queue='crypto_tweets_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
