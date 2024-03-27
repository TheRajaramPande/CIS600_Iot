import random
import paho.mqtt.publish as publish

# MQTT Broker Information for ThingSpeak
mqttHost = "mqtt3.thingspeak.com"

topic = "channels/2486709/publish"

# Unique ID for the environmental station
client_ID ="MjMHDSgkGAk4LzoRCSoSNjw"
username="MjMHDSgkGAk4LzoRCSoSNjw"
password = "sSeD6L89lQG69IsX26h+PHuw"
transport = "websockets"
port = 80

try:
    while True:
        # Generate random sensor values
        temperature = round(random.uniform(-50, 50), 2)  # Range: -50 to 50 Celsius
        humidity = round(random.uniform(0, 100), 2)     # Range: 0 to 100%
        co2 = round(random.uniform(300, 2000), 2)       # Range: 300ppm to 2000ppm# Publish sensor values to MQTT channel
        payload = f"field1={temperature}&field2={humidity}&field3={co2}"
        print(payload)
       x:username,'password':password})
        print(f"Published Device 1: {payload}")
        

except KeyboardInterrupt:

    print("Exiting program")
except Exception as e:
        print (e)
