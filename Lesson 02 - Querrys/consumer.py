import pika, os, sys

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='42')

    def callback(ch, method, properties, body):
        print(f'Я прочитал сообщение {body}')

    channel.basic_consume(queue='42', on_message_callback=callback, auto_ack=True)
    print('Я начал читать')
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