# python 3.6
# https://www.emqx.com/zh/mqtt/public-mqtt5-broker
import random
import time
from paho.mqtt import client as mqtt_client
import keyboard


broker = 'broker.emqx.io' 
port = 1883               #服务器TCP接口

topic_left_arm1 = "/JSH/LeftArm/IfMove/"
topic_left_arm2 = "/JSH/LeftArm/Speed/"
topic_right_arm1 = "/JSH/RightArm/IfMove/"
topic_right_arm2 = "/JSH/RightArm/Speed/"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'  #用户ID

        
def connect_mqtt():

    client = mqtt_client.Client(client_id)

    #client.on_connect = on_connect
    try:
        client.connect(broker, port)
        print("成功连接服务器")
        return client
    except:
        print(f"连接服务器失败")
        return 0
    


def publish(client, topic, msg):
    try:
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"将消息 `{msg}` 发送到话题 `{topic}`")
        else:
            print(f"无法将消息发送到话题 {topic}")
    except:
        print('消息发送失败')


def connect():
    client = connect_mqtt()
    if client == 0:
        print('未连接到服务器')
    else:
        client.loop_start()
    return client



    

if __name__ == '__main__':
    client = connect()
    while(True):
        publish(client, topic_left_arm1, 114)
        #publish(client, topic_left_arm2, 0.5)
        publish(client, topic_right_arm1, 1)
        #publish(client, topic_right_arm2, 1.5)
        time.sleep(1)

