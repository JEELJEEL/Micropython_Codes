# Micropython Codes for Beginners

This repository contains various MicroPython scripts that demonstrate essential IoT and embedded programming concepts. Each script is designed to teach fundamental functionalities in a practical and beginner-friendly way.

## Prerequisites

- A MicroPython-compatible device (e.g., ESP32, ESP8266).
- MicroPython firmware installed on your device.
- [Thonny IDE](https://thonny.org/) to upload and run MicroPython scripts.

---

## Overview of Scripts

### 1. **Interrupt-Driven GPIO Handling**
Learn how to handle GPIO interrupts to detect events like button presses or other digital input changes.

- **Key Features**:
  - Configures GPIO pins as input and output.
  - Uses interrupt service routines (ISR) for event-driven programming.

- **Usage**:
  - Connect a button to a GPIO pin.
  - The script will trigger an action (e.g., toggle an LED) on button press.

### 2. **Interval-Based Data Sending**
Send data periodically using timers in MicroPython.

- **Key Features**:
  - Demonstrates how to use `utime` or `machine.Timer`.
  - Ideal for periodic sensor readings or IoT data uploads.

- **Usage**:
  - Configure the interval duration and the data to send.

### 3. **MQTTQoS0.py**
Basic implementation of MQTT with QoS 0.

- **Key Features**:
  - Connects to an MQTT broker.
  - Publishes and subscribes to a topic with no acknowledgment (QoS 0).

- **Usage**:
  - Set the broker address, topic, and credentials.
  - Publish a message and observe incoming messages.

### 4. **MQTTQoS1.py**
Advanced MQTT implementation with QoS 1.

- **Key Features**:
  - Ensures message delivery at least once.
  - Suitable for applications requiring guaranteed delivery.

- **Usage**:
  - Same as `MQTTQoS0.py` but with QoS 1 enabled.

### 5. **Modbus_MQTT_Master**
Combines Modbus and MQTT protocols for communication.

- **Key Features**:
  - Acts as a Modbus master.
  - Sends Modbus data over MQTT to a cloud or local broker.

- **Usage**:
  - Connect Modbus-compatible sensors.
  - Configure MQTT broker details.

### 6. **Modbus_Slave**
Implements a Modbus slave device.

- **Key Features**:
  - Responds to Modbus queries from a master device.

- **Usage**:
  - Simulate a Modbus sensor or actuator.

### 7. **OTA.ino**
Example script for Over-the-Air (OTA) updates.

- **Key Features**:
  - Facilitates remote firmware updates.
  - Ideal for maintaining IoT devices in the field.

- **Usage**:
  - Upload the initial firmware.
  - Push updates using the OTA protocol.

### 8. **Plant_Watering**
Automated plant watering system using MicroPython.

- **Key Features**:
  - Reads soil moisture sensor data.
  - Activates a water pump based on moisture levels.

- **Usage**:
  - Connect a soil moisture sensor and a relay module.
  - Adjust thresholds for watering.

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/JEELJEEL/Micropython_Codes.git
   cd Micropython_Codes
   ```

2. Open Thonny IDE:
   - Connect your MicroPython-compatible device.
   - Ensure the correct port and interpreter are selected in Thonny's settings.

3. Upload a script to your MicroPython device:
   - Open the script in Thonny.
   - Click on the "Save As..." option and upload it to your device.

4. Run the script:
   - Click the "Run" button in Thonny.

---

## Contribution

Feel free to contribute by creating pull requests or suggesting improvements. This repository is designed to help others learn and grow in the field of MicroPython programming.

---

## License

This project is licensed under the MIT License.

---

Happy coding! 🚀
