import paho.mqtt.client as mqtt
import json
from variables.services.services_variables import get_variable
from measurements.logic.logic_measurements import create_measurement_object
from measurements.services.services_measurements import check_alarm

broker_address = "3.22.63.131"
broker_port = 1883
topic = "#"

def on_message(client, userdata, message):
 payload = message.payload.decode("utf-8")
 payloadJson = json.loads(payload)
 print("Message=", payloadJson)
 topic = message.topic.split('/')
 variable = get_variable(topic[2])
 create_measurement_object(variable, payloadJson["value"], payloadJson["unit"], topic[0] + topic[1])
 if variable.name == "Temperature":
  check_alarm(payloadJson["value"])

print("MQTT Start")
client = mqtt.Client('')
client.on_message = on_message
client.connect(broker_address, broker_port, 60)
client.subscribe(topic)