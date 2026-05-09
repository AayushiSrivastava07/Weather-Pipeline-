import requests
import pandas as pd
import schedule
import time
from datetime import datetime
import os

API_KEY = "6e79271a93b2e0650b4d4f48042cd81b"
CITY = "Delhi"

CSV_FILE = "weather_data.csv"


def fetch_weather_data():

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        # Check if API returned an error
        if response.status_code != 200:
            print(f"API Error: {data.get('message', 'Unknown error')}")
            return

        # Check if required fields exist
        if "main" not in data or "weather" not in data or "wind" not in data:
            print("Error: Unexpected API response format")
            return

        weather_data = {
            "timestamp": datetime.now(),
            "city": CITY,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather_condition": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        df = pd.DataFrame([weather_data])

        # Create CSV if not exists
        if not os.path.isfile(CSV_FILE):
            df.to_csv(CSV_FILE, index=False)

        else:
            df.to_csv(CSV_FILE, mode='a', header=False, index=False)

        print("Weather data saved successfully!")
        print(weather_data)

    except Exception as e:
        print("Error:", e)


# Run every 1 minute
schedule.every(1).minutes.do(fetch_weather_data)

print("Real-Time Weather Pipeline Started...")

# First run immediately
fetch_weather_data()

while True:
    schedule.run_pending()
    time.sleep(1)
