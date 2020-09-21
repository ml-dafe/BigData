# Семинар 1
### Часть 1. 
1. Установите и запустите RabbitMQ с помощью Docker
```docker run -it --rm -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management```
2. Создайте файл producer.py
    - Используйте библиотеку pika
    - Создайте подключение connection с помощью класса `pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))`
    - Для подклдчения к брокеру используйте метод `.channel()
    - Для обозначения очереди используйте метод `.queue_declare(queue='название очереди')`
    - Для публикации сообщения используйте метод `.basic_publish()`
    - Для закрытия подключения вы можете использовать метод `.close()`
3. Создайте файл consumer.py
    - Импортируйте библиотеки pika, sys, os
    - Используйте шаблон: 
        ```if __name__ == '__main__':
            try:
                main()
            except KeyboardInterrupt:
                print('Interrupted')
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)```
    - Создайте функцию main():
        - Аналогично producer.py подключитесь к серверу и выберите нужную очередь
        - Опишите настройки метода чтения из очереди `channel.basic_consume(queue='название очереди', on_message_callback=callback, auto_ack=True)
        - Не забудьте описать функцию callback
        - Начните читать очередь с помощью метода `.start_consuming()`
4. Запустите оба скрипта и проверьте передачу сообщений. 
### Часть 2. 
Задание касается решения курсового кейса         
1. Выберите клиент для чтения MQTT (например `paho`)
2. Подключитесь к брокеру `95.31.7.170:1883`
3. Попробуйте читать данные из очереди `/aircrafts` и `/data`
4. Попробуйте организовать постоянное чтение и сохранение данных. 
`