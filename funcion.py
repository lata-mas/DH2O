from umqtt.simple import MQTTClient
import gc
import json
import machine
import utime

def settimeout(duration):
  pass
def t3_publication(topic, msg):
  print (topic, ';', msg)
  pycom.rgbled(0xff00)


def publish_thingsboard(token,UNIQUE_ID,data,place='', password=''):
  client = MQTTClient(UNIQUE_ID, "iot.ier.unam.mx", port = 1883, user=token, password=password)
  client.settimeout = settimeout
  client.connect()
  lugar = 'v1/devices/me/' + place
  print(json.dumps(data))
  client.publish(lugar, json.dumps(data) )
  client.disconnect()


