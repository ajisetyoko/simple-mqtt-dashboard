import paho.mqtt.client as paho
import time
import random

from itsdangerous import base64_encode
import json

broker = "localhost"
port = 1883

module_name = "A3p1"
sensor_type = "temperature"
sensor_id = "1001054"
module_uuid = "A100G18766A"

topic = f"{module_name}/{sensor_type}"


def on_publish(client, userdata, result):
    print("Device 1 : Data published.")
    print(result)
    pass


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


client = paho.Client(transport="websockets")
client.connect(broker, port)
client.on_publish = on_publish

while True:
    time.sleep(1)  # frequency about 1Hz
    data = {
        "value": random.randint(23, 31),
        "sensor_id": sensor_id,
        "module_uuid": module_uuid,
    }
    data_enc = base64_encode(json.dumps(data))

    ret = client.publish(topic, data_enc)

print("Stopped...")
