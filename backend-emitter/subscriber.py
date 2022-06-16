from email import message
import paho.mqtt.client as mqtt
from itsdangerous import base64_decode

broker = "localhost"
port = 1883

module_name = "A3p1"
sensor_type = "temperature"
sensor_id = "1001054"
module_uuid = "A100G18766A"

topic = f"{module_name}/{sensor_type}"


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.payload)
    print(msg.topic + " " + str(msg.qos) + " " + base64_decode(msg.payload).decode())


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


mqttc = mqtt.Client(transport="websockets")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.connect(broker, 1883, 60)
mqttc.subscribe(topic, 0)

mqttc.loop_forever()
