from flask import Flask, request, jsonify
import joblib
import numpy as np
from Crypto.Cipher import AES
from base64 import b64decode

app = Flask(__name__)
model = joblib.load('energy_model.pkl')

KEY = b'Sixteen byte key'

def decrypt_data(encrypted_text):
    cipher = AES.new(KEY, AES.MODE_ECB)
    decoded = b64decode(encrypted_text)
    decrypted = cipher.decrypt(decoded).decode('utf-8').strip()
    return decrypted

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        temp = float(data['temp'])
        humidity = float(data['humidity'])
        device_usage = float(data['device_usage'])
    except KeyError:
        return jsonify({'error': 'Missing input parameters'}), 400

    prediction = model.predict(np.array([[temp, humidity, device_usage]]))[0]
    return jsonify({'predicted_energy_usage': round(prediction, 2)})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Energy Optimization API is running."})

if __name__ == '__main__':
    app.run(debug=True)
