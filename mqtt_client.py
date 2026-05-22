import paho.mqtt.client as mqtt
import json
from .models import Sensor, SensorData


broker = "broker.hivemq.com"
port = 1883
topic = "structurepulse/sensors"

def on_message(client, userdata, message):
    payload = message.payload.decode()
    data = json.loads(payload)

    sensor = Sensor.objects.get(id=data['sensor_id'])

    SensorData.objects.create(
        sensor=sensor,
        vibration=data['vibration'],
        temperature=data['temperature'],
        humidity=data['humidity']
    )
client = mqtt.Client()
client.on_message = on_message
client.connect(broker)















import paho.mqtt.client as mqtt
import json

from .models import Sensor
from .models import SensorData


BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "structurepulse/data"


def on_connect(client, userdata, flags, rc):

    print("MQTT connecté")

    client.subscribe(TOPIC)


def on_message(client, userdata, msg):

    payload = msg.payload.decode()

    data = json.loads(payload)

    sensor = Sensor.objects.get(
        id=data['sensor_id']
    )

    SensorData.objects.create(
        sensor=sensor,
        vibration=data['vibration'],
        temperature=data['temperature'],
        humidity=data['humidity']
    )

    print("Données reçues MQTT")


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.loop_start()