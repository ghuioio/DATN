import pika, sys, os, json
import snscrape.modules.twitter as sntwitter

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # channel.queue_declare(queue='hello')

    # def callback(ch, method, properties, body):
    #     print(" [x] Received %r" % body)

    # channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    # print(' [*] Waiting for messages. To exit press CTRL+C')
    # channel.start_consuming()

    channel.queue_declare(queue='crypto_tweets_queue')

    def callback(ch, method, properties, body):
        tweet = json.loads(body)
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