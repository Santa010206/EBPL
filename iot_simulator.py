import requests
import random
import time

while True:
    payload = {
        'temp': random.uniform(20.0, 35.0),
        'humidity': random.uniform(30.0, 70.0),
        'device_usage': random.uniform(1.0, 10.0)
    }
    response = requests.post("http://localhost:5000/predict", json=payload)
    print("IoT Sent:", payload, "| Response:", response.json())
    time.sleep(5)
