import os
import requests
from cities import CITIES

API_KEY = os.getenv("WEATHER_API_KEY")

print("=" * 50)
print("UTTARAKHAND 360 WEATHER REPORT")
print("=" * 50)

for city in CITIES:
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print(f"\n📍 {data['location']['name']}")
        print(f"🌡 Temperature : {data['current']['temp_c']}°C")
        print(f"☁ Condition   : {data['current']['condition']['text']}")
        print(f"💧 Humidity   : {data['current']['humidity']}%")
        print(f"💨 Wind       : {data['current']['wind_kph']} km/h")

    else:
        print(f"\n❌ Could not fetch weather for {city}")
