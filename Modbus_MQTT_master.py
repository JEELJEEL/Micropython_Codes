from pymodbus.client import ModbusTcpClient
import paho.mqtt.client as mqtt
import binascii
import time

# Modbus Configuration
esp32_ip = '192.168.0.100'  # Replace with your ESP32's IP address
modbus_port = 502  # Modbus TCP default port

# MQTT Configuration
mqtt_server = 'mqtt.eclipseprojects.io'
mqtt_user = 'jeeljeeljhsbs'
mqtt_pass = 'Jeelnramani'
client_id = binascii.hexlify(b'raspberrypi_master').decode('utf-8')  # Convert to string
topic_pub = '/topic/qos0'

# Connect to ESP32 Modbus Slave
modbus_client = ModbusTcpClient(esp32_ip, port=modbus_port)
if modbus_client.connect():
    print(f"Connected to ESP32 Modbus Slave at {esp32_ip}:{modbus_port}")
else:
    print("Failed to connect to ESP32 Modbus Slave!")
    exit()

# MQTT Client Setup
mqtt_client = mqtt.Client(client_id)
mqtt_client.username_pw_set(mqtt_user, mqtt_pass)

# MQTT Connect
def connect_mqtt():
    try:
        mqtt_client.connect(mqtt_server, 1883, 60)
        print("Connected to MQTT server")
    except Exception as e:
        print(f"Failed to connect to MQTT server: {e}")
        exit()

connect_mqtt()

# Read Modbus Registers and Publish to MQTT
try:
    while True:
        # Read Holding Registers (address 0, 6 registers for temperature and humidity)
        response = modbus_client.read_holding_registers(address=0,count=6,slave=1)  # Only 2 arguments
        if not response.isError():
            temperature = response.registers[0] / 100.0
            humidity = response.registers[1] / 100.0
            print(f"Temperature: {temperature} °C")
            print(f"Humidity: {humidity} %")

            # Create the payload
            payload = f"{{\"temperature\": {temperature}, \"humidity\": {humidity}}}"

            # Publish to MQTT topic
            mqtt_client.publish(topic_pub, payload)
            print(f"Published to MQTT: {payload}")
        else:
            print("Error reading registers:", response)

        time.sleep(5)  # Delay between reads
except KeyboardInterrupt:
    print("Stopping...")
finally:
    modbus_client.close()
    mqtt_client.disconnect()
