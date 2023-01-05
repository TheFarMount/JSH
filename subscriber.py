# python3.6

import random
import string
from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "/python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
times = 0

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    global times
    def on_message(client, userdata, msg):
        global times
        times += 1
        _str = msg.payload.decode()
        if(times >= 2):
            _int = float(_str)
            print(f"Received {_str} from {msg.topic} topic, message type:{type(_int)}")

    client.subscribe(topic)
    client.on_message = on_message

#def str_to_int()

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()