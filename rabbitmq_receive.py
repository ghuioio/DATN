import pika, sys, os, json
import snscrape.modules.twitter as sntwitter
from recrawl import recrawl_user_data
from ranking import get_ranking 
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='crypto_tweets_queue')

    def callback(ch, method, properties, body):
        data = json.loads(body)
        recrawl_user_data(data.url)
        print(" [x] Received %r" % body)


    channel.basic_consume(queue='crypto_tweets_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)