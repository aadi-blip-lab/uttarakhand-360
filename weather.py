import os
import requests

from datetime import datetime
from zoneinfo import ZoneInfo

from jinja2 import Environment, FileSystemLoader

from cities import CITIES


# ----------------------------------
# CONFIGURATION
# ----------------------------------

API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://api.weatherapi.com/v1/current.json"

TIMEZONE = ZoneInfo("Asia/Kolkata")


# ----------------------------------
# STORAGE
# ----------------------------------

weather_data = []


# ----------------------------------
# FETCH WEATHER
# ----------------------------------

print("=" * 60)
print("UTTARAKHAND 360")
print("Fetching Weather...")
print("=" * 60)


for city in CITIES:

    url = f"{BASE_URL}?key={API_KEY}&q={city}"

    try:

        response = requests.get(url, timeout=20)

        response.raise_for_status()

        data = response.json()

        current = data["current"]
        location = data["location"]

        city_weather = {

            "city": location["name"],

            "region": location["region"],

            "country": location["country"],

            "localtime": location["localtime"],

            "temperature": current["temp_c"],

            "feels_like": current["feelslike_c"],

            "condition": current["condition"]["text"],

            "icon": "https:" + current["condition"]["icon"],

            "humidity": current["humidity"],

            "wind": current["wind_kph"],

            "wind_dir": current["wind_dir"],

            "pressure": current["pressure_mb"],

            "visibility": current["vis_km"],

            "uv": current["uv"],

            "cloud": current["cloud"],

            "is_day": current["is_day"]

        }

        weather_data.append(city_weather)

        print(
            f"✓ {city_weather['city']} : "
            f"{city_weather['temperature']}°C"
        )

    except Exception as e:

        print(f"✗ {city}")
        print(e)


# ----------------------------------
# SORTING
# ----------------------------------

warmest = max(
    weather_data,
    key=lambda x: x["temperature"]
)

coldest = min(
    weather_data,
    key=lambda x: x["temperature"]
)

windiest = max(
    weather_data,
    key=lambda x: x["wind"]
)

humid = max(
    weather_data,
    key=lambda x: x["humidity"]
)

uv = max(
    weather_data,
    key=lambda x: x["uv"]
)

visibility = max(
    weather_data,
    key=lambda x: x["visibility"]
)


# ----------------------------------
# TEMPLATE ENGINE
# ----------------------------------

env = Environment(
    loader=FileSystemLoader("templates")
)

template = env.get_template("index.html")
# ----------------------------------
# RENDER WEBSITE
# ----------------------------------

html = template.render(

    weather=weather_data,

    updated=datetime.now(TIMEZONE).strftime(
        "%d %B %Y • %I:%M:%S %p"
    ),

    warmest=warmest,

    coldest=coldest,

    windiest=windiest,

    humid=humid,

    uv=uv,

    visibility=visibility,

    total_cities=len(weather_data)

)


# ----------------------------------
# SAVE WEBSITE
# ----------------------------------

with open(
    "docs/index.html",
    "w",
    encoding="utf-8"
) as file:

    file.write(html)


# ----------------------------------
# FINISHED
# ----------------------------------

print()

print("=" * 60)

print("WEBSITE GENERATED SUCCESSFULLY")

print("=" * 60)

print()

print(f"Cities Processed : {len(weather_data)}")

print(
    "Generated At :",
    datetime.now(TIMEZONE).strftime(
        "%d %B %Y %I:%M:%S %p"
    )
)
