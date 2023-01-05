# python 3.6
#https://www.emqx.com/zh/mqtt/public-mqtt5-broker
import random
import time
from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io' 
port = 1883               #服务器TCP接口
topic = "/python/mqtt"    #话题名称(自定义)

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'  #用户ID

class eeg_data():
    __left_arm = 0.0
    __right_arm = 0.0
    __left_leg = 0.0
    __right_leg = 0.0

    #为左臂赋值
    def left_arm_assignment(self, data):
        self.__left_arm = data
    #为右臂赋值
    def right_arm_assignment(self, data):
        self.__right_arm = data
    #为左腿赋值
    def left_leg_assignment(self, data):
        self.__left_leg
    #为右腿赋值
    def rignt_leg_assignment(self, data):
        self.__right_leg
    #读取数据(返回数据列表)
    def show_data(self):
        print("左臂数据: %f, 右臂数据: %f, 左腿数据: %f, 右腿数据: %f", \
            self.left_arm_assignment, self.right_arm_assignment, \
            self.rignt_leg_assignment, self.rignt_leg_assignment)
        return [self.__left_arm, self.__right_arm, self.__left_leg, self.__right_leg]
    def __init__(self):
        print("消息实例已创建!")
        
        
def connect_mqtt():
#   def on_connect(client, userdata, flags, rc):
#       if rc == 0:
#           print("Connected to MQTT Broker!")
#       else:
#           print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)

    #client.on_connect = on_connect
    try:
        client.connect(broker, port)
        print("成功连接服务器")
        return client
    except:
        print(f"连接服务器失败")
        return 0
    


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        data = eeg_data()
        msg = data.show_data
        try:
            result = client.publish(topic, msg)
            status = result[0]
            if status == 0:
                print(f"将消息 `{msg}` 发送到话题 `{topic}`")
            else:
                print(f"无法将消息发送到话题 {topic}")
        except:
            print('消息发送失败')


def run():
    client = connect_mqtt()
    if client == 0:
        print('未连接到服务器')
    else:
        client.loop_start()
        publish(client)


if __name__ == '__main__':
    run()