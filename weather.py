import os
import requests

from datetime import datetime
from zoneinfo import ZoneInfo

from cities import CITIES


# ==========================================================
# UTTARAKHAND 360
# Weather Dashboard Generator
# Version 1.0
# ==========================================================


# -----------------------------
# CONFIGURATION
# -----------------------------

API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://api.weatherapi.com/v1/current.json"

TIMEZONE = ZoneInfo("Asia/Kolkata")

OUTPUT_FILE = "docs/index.html"


# -----------------------------
# STORAGE
# -----------------------------

cities_weather = []

weather_cards = ""

navbar = ""

hero = ""

highlights = ""

footer = ""

html = ""


# -----------------------------
# CONSOLE
# -----------------------------

print("=" * 60)
print("UTTARAKHAND 360")
print("LIVE WEATHER GENERATOR")
print("=" * 60)
print()


# -----------------------------
# FETCH WEATHER
# -----------------------------

for city in CITIES:

    url = f"{BASE_URL}?key={API_KEY}&q={city}"

    try:

        response = requests.get(url, timeout=20)

        response.raise_for_status()

        data = response.json()

        location = data["location"]

        current = data["current"]

        city_data = {

            "city": location["name"],

            "region": location["region"],

            "country": location["country"],

            "updated": location["localtime"],

            "temperature": current["temp_c"],

            "feels_like": current["feelslike_c"],

            "condition": current["condition"]["text"],

            "icon": "https:" + current["condition"]["icon"],

            "humidity": current["humidity"],

            "wind": current["wind_kph"],

            "wind_direction": current["wind_dir"],

            "pressure": current["pressure_mb"],

            "visibility": current["vis_km"],

            "uv": current["uv"],

            "cloud": current["cloud"],

            "is_day": current["is_day"]

        }

        cities_weather.append(city_data)

        print(
            f"✓ "
            f"{city_data['city']:<18}"
            f"{city_data['temperature']}°C"
        )

    except Exception as error:

        print(f"✗ {city}")

        print(error)

        print()


# -----------------------------
# CHECK DATA
# -----------------------------

if not cities_weather:

    print()

    print("No weather data received.")

    print("Stopping program.")

    raise SystemExit


print()

print("-" * 60)

print(
    f"Successfully fetched "
    f"{len(cities_weather)} cities."
)

print("-" * 60)

print()
# ==========================================================
# TODAY'S HIGHLIGHTS
# ==========================================================

warmest = max(
    cities_weather,
    key=lambda city: city["temperature"]
)

coldest = min(
    cities_weather,
    key=lambda city: city["temperature"]
)

windiest = max(
    cities_weather,
    key=lambda city: city["wind"]
)

highest_humidity = max(
    cities_weather,
    key=lambda city: city["humidity"]
)

highest_uv = max(
    cities_weather,
    key=lambda city: city["uv"]
)

best_visibility = max(
    cities_weather,
    key=lambda city: city["visibility"]
)


print("Today's Highlights")
print("------------------------------")

print(
    f"🔥 Warmest : "
    f"{warmest['city']} "
    f"({warmest['temperature']}°C)"
)

print(
    f"❄ Coldest : "
    f"{coldest['city']} "
    f"({coldest['temperature']}°C)"
)

print(
    f"💨 Windiest : "
    f"{windiest['city']} "
    f"({windiest['wind']} km/h)"
)

print(
    f"💧 Highest Humidity : "
    f"{highest_humidity['city']} "
    f"({highest_humidity['humidity']}%)"
)

print(
    f"☀ Highest UV : "
    f"{highest_uv['city']} "
    f"({highest_uv['uv']})"
)

print(
    f"👀 Best Visibility : "
    f"{best_visibility['city']} "
    f"({best_visibility['visibility']} km)"
)

print()


# ==========================================================
# GENERATE WEATHER CARDS
# ==========================================================

for city in cities_weather:

    day_night = "☀ Day" if city["is_day"] else "🌙 Night"

    weather_cards += f"""

<div class="weather-card">

    <div class="weather-header">

        <img
        src="{city['icon']}"
        alt="{city['condition']}">

        <h2>{city['city']}</h2>

    </div>

    <div class="temperature">

        {city['temperature']}°C

    </div>

    <div class="condition">

        {city['condition']}

    </div>

    <div class="weather-details">

        <p>

        🌡 Feels Like

        <strong>

        {city['feels_like']}°C

        </strong>

        </p>

        <p>

        💧 Humidity

        <strong>

        {city['humidity']}%

        </strong>

        </p>

        <p>

        💨 Wind

        <strong>

        {city['wind']} km/h

        </strong>

        </p>

        <p>

        🧭 Direction

        <strong>

        {city['wind_direction']}

        </strong>

        </p>

        <p>

        🌫 Visibility

        <strong>

        {city['visibility']} km

        </strong>

        </p>

        <p>

        ☀ UV Index

        <strong>

        {city['uv']}

        </strong>

        </p>

        <p>

        ☁ Cloud Cover

        <strong>

        {city['cloud']}%

        </strong>

        </p>

        <p>

        {day_night}

        </p>

    </div>

</div>

"""
# ==========================================================
# PAGE INFORMATION
# ==========================================================

page_title = "Uttarakhand 360 | Live Weather Dashboard"

tagline = "Live Weather • Travel • Road Conditions • Char Dham"

last_updated = datetime.now(TIMEZONE).strftime(
    "%d %B %Y • %I:%M:%S %p"
)


# ==========================================================
# NAVBAR
# ==========================================================

navbar = f"""

<nav class="navbar">

    <div class="logo">

        🌦 Uttarakhand 360

    </div>

    <ul>

        <li><a href="#">Home</a></li>

        <li><a href="weather.html">Weather</a></li>

        <li><a href="districts.html">Districts</a></li>

        <li><a href="chardham.html">Char Dham</a></li>

        <li><a href="#">Travel</a></li>

        <li><a href="#">Road Status</a></li>

        <li><a href="#">Alerts</a></li>

        <li><a href="about.html">About</a></li>

        <li><a href="contact.html">Contact</a></li>

    </ul>

    <button id="theme-toggle">

        🌙

    </button>

</nav>

"""


# ==========================================================
# HERO SECTION
# ==========================================================

hero = f"""

<header class="hero">

    <h1>Uttarakhand 360</h1>

    <p>

        {tagline}

    </p>

    <div class="hero-info">

        <div class="info-card">

            🌦 Weather Updated

            <strong>

                {last_updated}

            </strong>

        </div>

        <div class="info-card">

            🕒 Current India Time

            <strong id="clock">

                Loading...

            </strong>

        </div>

    </div>

    <div class="search-box">

        <input

        type="text"

        id="search"

        placeholder="Search district or city...">

    </div>

</header>

"""


# ==========================================================
# HIGHLIGHTS SECTION
# ==========================================================

highlights = f"""

<section class="highlights-section">

<h2>

🔥 Today's Highlights

</h2>

<div class="highlight-grid">

<div class="highlight-card">

<h3>🔥 Warmest</h3>

<p>{warmest["city"]}</p>

<strong>{warmest["temperature"]}°C</strong>

</div>

<div class="highlight-card">

<h3>❄ Coldest</h3>

<p>{coldest["city"]}</p>

<strong>{coldest["temperature"]}°C</strong>

</div>

<div class="highlight-card">

<h3>💨 Windiest</h3>

<p>{windiest["city"]}</p>

<strong>{windiest["wind"]} km/h</strong>

</div>

<div class="highlight-card">

<h3>💧 Highest Humidity</h3>

<p>{highest_humidity["city"]}</p>

<strong>{highest_humidity["humidity"]}%</strong>

</div>

<div class="highlight-card">

<h3>☀ Highest UV</h3>

<p>{highest_uv["city"]}</p>

<strong>{highest_uv["uv"]}</strong>

<p style="font-size:13px;color:#666;">
{"🌙 UV is 0 after sunset" if highest_uv["uv"] == 0 else "☀ Current UV Index"}
</p>

</div>

<div class="highlight-card">

<h3>👀 Best Visibility</h3>

<p>{best_visibility["city"]}</p>

<strong>{best_visibility["visibility"]} km</strong>

</div>

</div>

</section>

"""


# ==========================================================
# CURRENT WEATHER SECTION
# ==========================================================

cards_section = f"""

<section class="weather-section">

<h2>

Current Weather

</h2>

<div class="weather-grid">

{weather_cards}

</div>

</section>

"""
# ==========================================================
# FOOTER
# ==========================================================

footer = """

<footer class="footer">

<div class="footer-content">

<h2>Uttarakhand 360</h2>

<p>

Live Weather • Travel • Road Conditions • Char Dham

</p>

<p>

Need to get in touch?

Bring coffee first. ☕

</p>

<div class="chatbot-placeholder">

💬 Uttarakhand Assistant

<br>

<small>Coming Soon</small>

</div>

<p>

Powered by WeatherAPI

</p>

<p>

© 2026 Uttarakhand 360

</p>

</div>

</footer>

"""


# ==========================================================
# BUILD HTML
# ==========================================================

html = f"""

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>{page_title}</title>

<link rel="stylesheet" href="style.css">

<link rel="icon" href="favicon.svg">

<link rel="preconnect"
href="https://fonts.googleapis.com">

<link rel="preconnect"
href="https://fonts.gstatic.com"
crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
rel="stylesheet">

</head>

<body>

{navbar}

{hero}

{cards_section}

{highlights}

{footer}

<script src="script.js"></script>

</body>

</html>

"""


# ==========================================================
# SAVE WEBSITE
# ==========================================================

os.makedirs("docs", exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

    file.write(html)

# ==========================================================
# FINISHED
# ==========================================================

print()

print("=" * 60)

print("WEBSITE GENERATED SUCCESSFULLY")

print("=" * 60)

print()

print(f"Cities Processed : {len(cities_weather)}")

print("Generated At :", last_updated)

print()

print(f"Output File : {OUTPUT_FILE}")

print()

print("Ready for GitHub Pages.")

print()

print("=" * 60)

# ==========================================================
# GENERATE OTHER PAGES
# ==========================================================

print()

print("Generating additional pages...")

print()
