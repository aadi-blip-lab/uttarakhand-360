import os
import requests

API_KEY = os.getenv("WEATHER_API_KEY")

city = "Dehradun"

url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("City:", data["location"]["name"])
    print("Temperature:", data["current"]["temp_c"], "°C")
    print("Condition:", data["current"]["condition"]["text"])
    print("Humidity:", data["current"]["humidity"], "%")
    print("Wind:", data["current"]["wind_kph"], "km/h")

else:
    print("Error:", response.text)
