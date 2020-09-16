import paho.mqtt.client as mqtt

broker = '95.31.7.170'
port = 1883

def on_connect(consumer,  userdata, flags, rc):
    consumer.subscribe('/data')

def on_message(consumer, userdata, msg):
    print(msg.payload.decode())

consumer = mqtt.Client()
consumer.connect(broker, port)

consumer.on_connect = on_connect
consumer.on_message = on_message
consumer.loop_forever()


