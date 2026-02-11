import requests
import csv
from datetime import datetime

# 1. EXTRACT: Get data from the API
# Specific for Bengaluru coordinates
print("Connecting to Weather Satellite...")
url = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
response = requests.get(url)
data = response.json()

# 2. TRANSFORM: Simplify the data
current_weather = {
    "time": data["current"]["time"],
    "temperature": data["current"]["temperature_2m"],
    "wind_speed": data["current"]["wind_speed_10m"],
    "city": "Bengaluru"
}

# 3. LOAD: Save to a CSV file
file_name = "bengaluru_weather.csv"
with open(file_name, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=current_weather.keys())
    writer.writeheader()
    writer.writerow(current_weather)

print(f"SUCCESS: Weather data saved to {file_name}")