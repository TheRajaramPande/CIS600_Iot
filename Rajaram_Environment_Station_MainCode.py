import random
import paho.mqtt.publish as publish

# MQTT Broker Information for IoT Hub
mqtt_broker = "mqtt3.thingspeak.com"  # MQTT broker address

iot_topic1 = "channels/2483692/publish"  # MQTT topic for publishing sensor data
iot_topic2 = "channels/ 2486845/publish" # MQTT topic for publishing sensor data

# Unique ID and authentication for the IoT devices
device_ID =  ["LyASNQQMJQM9MyEROTk6NjM", "PAM8ATkDKR0jLhIHHAMzBhM"]  # Device IDs
device_username = ["LyASNQQMJQM9MyEROTk6NjM", "PAM8ATkDKR0jLhIHHAMzBhM"]  # Device usernames
device_password =  ["v5mKtA5ggwuZkEOwHuX9pigI", "PAM8ATkDKR0jLhIHHAMzBhM"]  # Device passwords
transport_type = "websockets"  # Transport protocol
mqtt_port = 80  # MQTT port

def generate_values():
    """
    Generate random sensor values for temperature, humidity, and CO2 levels.
    Temperature range: -50 to 50 Celsius
    CO2 range: 300ppm to 2000ppm
    """
    temperature = round(random.uniform(-50, 50), 2)  # Random temperature value
    co2 = round(random.uniform(300, 2000), 2)  # Random CO2 value
    return temperature, humidity, co2

try:
    while True:
        # Generate sensor values
        temperature, humidity, co2 = generate_values()
        
        # Publish sensor values to MQTT channel for Device 1
        payload_device_1 = f"field1={temperature}&field2={humidity}&field3={co2}"
        publish.single(iot_topic1, payload_device_1, hostname=mqtt_broker, transport=transport_type, port=mqtt_port, client_id=device_ID[0], auth={'username': device_username[0], 'password': device_password[0]})
        print(f"Published Device 1: {payload_device_1}")
        
        # Generate sensor values
        temperature, humidity, co2 = generate_values()
        
        # Publish sensor values to MQTT channel for Device 2
        payload_device_2 = f"field1={temperature}&field2={humidity}&field3={co2}"
        publish.single(iot_topic2, payload_device_2, hostname=mqtt_broker, transport=transport_type, port=mqtt_port, client_id=device_ID[1], auth={'username': device_username[1], 'password': device_password[1]})
        print(f"Published Device 2: {payload_device_2}")

except KeyboardInterrupt:
    print("Exiting program")  # Handle keyboard interrupt
except Exception as e:
    print(e)  # Handle other exceptions
