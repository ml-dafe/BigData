import pika, time
import numpy as np

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='42')
while True:
    i = np.random.rand()
    channel.basic_publish(exchange='', routing_key='42', body=str(i))

    print(f'Сообщение {i} отправлено! ')
    time.sleep(1)

connection.close()

