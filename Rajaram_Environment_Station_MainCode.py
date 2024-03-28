import random
import paho.mqtt.publish as publish

# MQTT Broker Information for IoT Hub
mqtt_broker = "mqtt3.thingspeak.com"

iot_topic = "channels/2483692/publish"

# Unique ID and authentication for the IoT devices
device_ID =  ["LyASNQQMJQM9MyEROTk6NjM", "PAM8ATkDKR0jLhIHHAMzBhM"]
device_username = ["LyASNQQMJQM9MyEROTk6NjM", "PAM8ATkDKR0jLhIHHAMzBhM"]
device_password =  ["v5mKtA5ggwuZkEOwHuX9pigI", "PAM8ATkDKR0jLhIHHAMzBhM"]
transport_type = "websockets"
mqtt_port = 80

try:
    while True:
        # Generate random sensor values 
        temperature = round(random.uniform(-50, 50), 2)  # Temperature range: -50 to 50 Celsius
        humidity = round(random.uniform(0, 100), 2)     # Humidity range: 0 to 100%
        co2 = round(random.uniform(300, 2000), 2)       # CO2 range: 300ppm to 2000ppm

        # Publish sensor values to MQTT channel for Device 1
        payload_device_1 = f"field1={temperature}&field2={humidity}&field3={co2}"
        publish.single(iot_topic, payload_device_1, hostname=mqtt_broker, transport=transport_type, port=mqtt_port, client_id=device_ID[0], auth={'username': device_username[0], 'password': device_password[0]})
        print(f"Published Device 1: {payload_device_1}")

        # Publish sensor values to MQTT channel for Device 2
        payload_device_2 = f"field1={temperature}&field2={humidity}&field3={co2}"
        publish.single(iot_topic, payload_device_2, hostname=mqtt_broker, transport=transport_type, port=mqtt_port, client_id=device_ID[1], auth={'username': device_username[1], 'password': device_password[1]})
        print(f"Published Device 2: {payload_device_2}")

except KeyboardInterrupt:
    print("Exiting program")
except Exception as e:
    print (e)
