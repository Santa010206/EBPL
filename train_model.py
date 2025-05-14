import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample energy consumption dataset
data = pd.read_csv('energy_data.csv')  # Assume this has columns: temp, humidity, device_usage, energy

X = data[['temp', 'humidity', 'device_usage']]
y = data['energy']

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

joblib.dump(model, 'energy_model.pkl')
print("Model trained and saved.")
