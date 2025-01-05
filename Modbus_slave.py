import network
import socket
import struct
import time
import random

# Wi-Fi settings
SSID = 'Khush_EXT'
PASSWORD = '9023669791'

# Modbus TCP settings
MODBUS_PORT = 502  # Default Modbus TCP port
MODBUS_SLAVE_ID = 1  # Slave ID for Modbus

# Wi-Fi connection
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    while not wlan.isconnected():
        time.sleep(1)
        print("Connecting to WiFi...")
    
    print("WiFi connected")
    print("IP Address:", wlan.ifconfig()[0])

# Generate random sensor data
def generate_random_sensor_data():
    temperature = random.uniform(20, 30)  # Random temperature between 20 and 30 °C
    humidity = random.uniform(40, 60)  # Random humidity between 40 and 60 %
    return [int(temperature * 100), int(humidity * 100)]

# Handle Modbus requests
def handle_modbus_request(data):
    print("Received raw data:", data)  # Debug: print raw data received

    # Verify the length of the data
    if len(data) < 12:
        print("Invalid Modbus request format")
        return None

    # Modbus request structure: [Transaction ID (2 bytes), Protocol ID (2 bytes), Length (2 bytes), Unit ID (1 byte), Function Code (1 byte), Start Address (2 bytes), Number of Registers (2 bytes)]
    transaction_id = struct.unpack('>H', data[0:2])[0]
    protocol_id = struct.unpack('>H', data[2:4])[0]
    length = struct.unpack('>H', data[4:6])[0]
    slave_id = data[6]
    function_code = data[7]
    start_address = struct.unpack('>H', data[8:10])[0]
    num_registers = struct.unpack('>H', data[10:12])[0]

    print(f"Transaction ID: {transaction_id}, Protocol ID: {protocol_id}, Length: {length}")
    print(f"Slave ID: {slave_id}, Function Code: {function_code}, Start Address: {start_address}, Number of Registers: {num_registers}")

    if slave_id != MODBUS_SLAVE_ID:
        print("Invalid slave ID")
        return None

    if function_code == 3:  # Read Holding Registers
        registers = generate_random_sensor_data()[:num_registers]
        response = bytearray(struct.pack('>H', transaction_id) + struct.pack('>H', protocol_id) + struct.pack('>H', 3 + len(registers) * 2))
        response.extend(bytearray([slave_id, function_code, len(registers) * 2]))
        for reg in registers:
            response.extend(struct.pack('>H', reg))
        print("Sending response:", response)  # Debug: print response
        return response

    print("Unsupported function code")
    return None


# Modbus server
def modbus_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', MODBUS_PORT))
    s.listen(5)  # Allow multiple connections

    print("Modbus server running on port", MODBUS_PORT)

    while True:
        try:
            conn, addr = s.accept()
            print("New connection from", addr)

            # Keep the connection open to handle multiple requests
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                response = handle_modbus_request(data)
                if response:
                    conn.send(response)
                else:
                    print("No valid response to send")

        except Exception as e:
            print(f"Error handling connection: {e}")

        finally:
            conn.close()

# Main function
def main():
    connect_wifi()
    modbus_server()

# Run the main function
if __name__ == '__main__':
    main()

