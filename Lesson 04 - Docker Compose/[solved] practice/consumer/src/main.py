import paho.mqtt.client as mqtt
import csv
import json
# from hdfs import InsecureClient
# from json import dumps
#
# #client = InsecureClient('http://localhost:8022')
# client.write('model.json', dumps({'dsa':'sd'}))

# This is the Subscriber
broker = "95.31.7.170"
port = 1883
timelive = 60


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/aircrafts")

def on_message(client, userdata, msg):
    message = msg.payload.decode().replace('\'', '\"')
    try:
        input_json = json.loads(message)
        time = input_json[0]['time']
        qnt = list(input_json[0]['fields'].values())[0]
        with open('data/data.csv', 'a') as fd:
            fd.write(f'{time},{qnt}\n')

    except Exception as e:
        print("Couldn't parse raw data: %s" % message, e)

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(broker, port, timelive)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()