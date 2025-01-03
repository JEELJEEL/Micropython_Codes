import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
import dht
esp.osdebug(None)
import gc
gc.collect()

ssid = 'Khush_EXT'
password = '9023669791'
mqtt_server = 'mqtt.eclipseprojects.io'
mqtt_user = 'jeeljeeljhsbs'
mqtt_pass = 'Jeelnramani'

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'/topic/qos1'
topic_pub = b'/topic/qos1'

last_message = 0
message_interval = 60

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
sensor = dht.DHT11(machine.Pin(4))

while not station.isconnected():
    pass

print('Connection successful')
print(station.ifconfig())

def read_temperature():
    try:
        sensor.measure()  
        temp = sensor.temperature()  
        return temp
    except OSError as e:
        print("Failed to read from DHT11 sensor:", e)
        return None  # Return None on failure

def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'notification' and msg == b'received':
        print('ESP received hello message')

def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server, user=mqtt_user, password=mqtt_pass)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub, qos=1)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()

try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()

while True:
    try:
        client.check_msg()  # Check for incoming MQTT messages
        if (time.time() - last_message) > message_interval:
            temp = read_temperature()
            if temp is not None:  # Only publish if temperature is valid
                msg = b'Temperature: %d°C' % temp
                client.publish(topic_pub, msg, qos=1)
                print("Published:", msg)
            last_message = time.time()
    except OSError as e:
        restart_and_reconnect()

