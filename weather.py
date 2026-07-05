import os
import requests

from datetime import datetime
from zoneinfo import ZoneInfo

from cities import CITIES
from districts import DISTRICTS
from alerts import ALERTS
from blogger import publish_to_blogger


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

district_weather = []

weather_cards = ""

district_html = ""

weather_page_html = ""

chardham_html = ""

navbar = ""

hero = ""

highlights = ""

footer = f"""

<footer class="footer">

<h2>

🌦 Uttarakhand 360

</h2>

<p>

Weather • Districts • Char Dham • Travel • Treks • Road Status

</p>

<p>

Made with ❤️ for Dev Bhoomi Uttarakhand.

</p>

<p>

Weather data updates every hour.

</p>

<p>

© 2026 Uttarakhand 360

</p>

</footer>

"""

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
# FETCH DISTRICT WEATHER
# -----------------------------

print()
print("Fetching district weather...")
print("-" * 60)

for district in DISTRICTS:

    url = f"{BASE_URL}?key={API_KEY}&q={district['weather_query']}"

    try:

        response = requests.get(url, timeout=20)

        response.raise_for_status()

        data = response.json()

        location = data["location"]
        current = data["current"]

        district_weather.append({

            "city": district["name"],
            "division": district["division"],

            "temperature": current["temp_c"],
            "feels_like": current["feelslike_c"],
            "condition": current["condition"]["text"],
            "icon": "https:" + current["condition"]["icon"],

            "humidity": current["humidity"],
            "wind": current["wind_kph"],
            "wind_direction": current["wind_dir"],

            "visibility": current["vis_km"],
            "uv": current["uv"],
            "cloud": current["cloud"],

            "is_day": current["is_day"]

        })

        print(f"✓ {district['name']}")

    except Exception as error:

        print(f"✗ {district['name']}")
        print(error)

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
   district_weather,
    key=lambda city: city["temperature"]
)

coldest = min(
    district_weather,
    key=lambda city: city["temperature"]
)

windiest = max(
    district_weather,
    key=lambda city: city["wind"]
)

highest_humidity = max(
    district_weather,
    key=lambda city: city["humidity"]
)

highest_uv = max(
    district_weather,
    key=lambda city: city["uv"]
)

best_visibility = max(
    district_weather,
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

<li><a href="index.html">🏠 Home</a></li>

<li><a href="weather.html">🌦 Weather</a></li>

<li><a href="districts.html">🗺 Districts</a></li>

<li><a href="chardham.html">🛕 Char Dham</a></li>

<li><a href="#">🥾 Treks</a></li>

<li><a href="#">🧭 Destinations</a></li>

<li><a href="#">🛣 Road Status</a></li>

<li><a href="#">🚨 Alerts</a></li>

<li><a href="about.html">ℹ About</a></li>

<li><a href="contact.html">📞 Contact</a></li>

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

<h1>

🏔 Uttarakhand 360

</h1>

<h2>

Everything You Need Before Entering the Himalayas

</h2>

<p>

🌦 Live Weather • 🗺 13 Official Districts • 🛕 Char Dham • 🥾 Treks • 🛣 Roads • 🚨 Alerts

</p>

<p style="margin-top:18px;font-size:18px;font-weight:600;color:#0d6efd;">

📍 Covering 13 Districts • 100+ Locations • Updated Every Hour

</p>

<div class="hero-buttons">

<a href="weather.html" class="btn-primary">

🌦 Live Weather

</a>

<a href="districts.html" class="btn-secondary">

🗺 Explore Districts

</a>

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

<h3>🔥 Warmest District</h3>

<p>{warmest["city"]}</p>

<strong>{warmest["temperature"]}°C</strong>

</div>

<div class="highlight-card">

<h3>❄ Coldest District</h3>

<p>{coldest["city"]}</p>

<strong>{coldest["temperature"]}°C</strong>

</div>

<div class="highlight-card">

<h3>💨 Windiest District</h3>

<p>{windiest["city"]}</p>

<strong>{windiest["wind"]} km/h</strong>

</div>

<div class="highlight-card">

<h3>💧 Most Humid District</h3>

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

cards_section = """

<section class="weather-preview">

<h2>🌦 Live Weather Across Uttarakhand</h2>

<p>
View real-time weather for all districts, Char Dham routes and trekking destinations.
</p>

<div style="text-align:center;margin-top:25px;">

<a href="weather.html" class="btn-primary">

🌦 View Live Weather

</a>

</div>

</section>

"""
# ==========================================================
# SUPPORT SECTION
# ==========================================================

support_section = """

<section class="support-section">

<h2>

❤️ Support Uttarakhand 360

</h2>

<p>

Uttarakhand 360 is an independent project built for travellers, pilgrims, trekkers and locals.

Your support helps us improve weather coverage, road updates, Char Dham information and build new features.

</p>

<a href="#" class="btn-primary">

❤️ Support the Project

</a>

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

Reliable weather information for travellers, pilgrims and locals across Uttarakhand.

</p>

<div class="chatbot-placeholder">

💬 Uttarakhand Assistant

<br>

<small>Coming Soon</small>

</div>

<p>

Powered by WeatherAPI • Updated Hourly

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

<section class="live-bar">

<div class="info-card">

🌦 Weather Updated

<strong>

{last_updated}

</strong>

</div>

<div class="info-card">

🕒 Current India Time

<strong id="clock"></strong>

</div>

</section>

{hero}

<section>

<h2>🤖 Uttarakhand Assistant (Beta)</h2>

<p>

Ask anything about Uttarakhand — weather, Char Dham, roads, treks, travel or destinations.

</p>

<div class="search-box">

<input
type="text"
id="aiQuestion"
placeholder="Example: Is Kedarnath good to visit this weekend?">

</div>

<div style="text-align:center;margin-top:20px;">

<button class="button" onclick="askAI()">

💬 Ask Assistant

</button>

</div>

</section>

{cards_section}

{highlights}

{support_section}

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
# WEATHER CARD FUNCTION
# ==========================================================

def create_weather_card(city):

    return f"""

<div class="weather-card">

<h2>

📍 {city['city']}

</h2>

<div class="temperature">

{city['temperature']}°C

</div>

<p>

{city['condition']}

</p>

<p>

💧 Humidity: {city['humidity']}%

</p>

<p>

💨 Wind: {city['wind']} km/h

</p>

<p>

👀 Visibility: {city['visibility']} km

</p>

</div>

"""

# ==========================================================
# GENERATE OTHER PAGES
# ==========================================================

print()

print("=" * 60)

print("GENERATING OTHER PAGES")

print("=" * 60)

print()

# ==========================================================
# DISTRICT INFORMATION
# ==========================================================

print("Generating districts.html...")

garhwal_cards = ""
kumaon_cards = ""

for district in district_weather:

    card = f"""
<div class="weather-card">

<h2>📍 {district['city']}</h2>

<div class="temperature">
{district['temperature']}°C
</div>

<p>{district['condition']}</p>

<p>🌡 Feels Like: {district['feels_like']}°C</p>

<p>💧 Humidity: {district['humidity']}%</p>

<p>💨 Wind: {district['wind']} km/h</p>

<p>👀 Visibility: {district['visibility']} km</p>

<p>☀ UV Index: {district['uv']}</p>

</div>
"""

    if district["division"] == "Garhwal":
        garhwal_cards += card
    else:
        kumaon_cards += card


district_html = f"""

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Districts | Uttarakhand 360</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

{navbar}

<section class="hero">

<h1>🗺 Districts of Uttarakhand</h1>

<p>
Official district weather across Garhwal and Kumaon.
</p>

</section>

<section>

<h2>🏔 Garhwal Division</h2>

<div class="weather-grid">

{garhwal_cards}

</div>

</section>

<section>

<h2>🌄 Kumaon Division</h2>

<div class="weather-grid">

{kumaon_cards}

</div>

</section>

{support_section}

{footer}

<script src="script.js"></script>

</body>

</html>

"""

with open(
    "docs/districts.html",
    "w",
    encoding="utf-8"
) as file:

    file.write(district_html)

print("✓ districts.html generated")

# ==========================================================
# WEATHER PAGE
# ==========================================================

print("Generating weather.html...")

weather_cards = ""

for city in cities_weather:

    weather_cards += create_weather_card(city)
#

weather_html = f"""

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Weather | Uttarakhand 360</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

{navbar}

<section class="hero">

<h1>

🌦 Uttarakhand Weather

</h1>

<h2>

Plan Your Journey with Live Weather Across Uttarakhand

</h2>

<p>

100+ Locations • Updated Hourly • Districts • Char Dham • Treks

</p>

</section>

<section>

<h2>

🌦 Live Weather Across Uttarakhand
101 Locations • Updated Every Hour

</h2>

<div class="search-box">

<input
type="text"
id="search"
placeholder="🔍 Search district, city, hill station or Char Dham...">

</div>

<br>

<div class="weather-grid">

{weather_cards}

</div>

</section>

{support_section}

{footer}

<script src="script.js"></script>

</body>

</html>

"""

with open(
    "docs/weather.html",
    "w",
    encoding="utf-8"
) as file:

    file.write(weather_html)

print("✓ weather.html generated")

# ==========================================================
# CHAR DHAM WEATHER
# ==========================================================

print("Generating chardham.html...")

dham_districts = {
    "Kedarnath": "Rudraprayag",
    "Badrinath": "Chamoli",
    "Gangotri": "Uttarkashi",
    "Yamunotri": "Uttarkashi"
}

char_dham_cards = ""

for city in cities_weather:

    if city["city"] in ["Rudraprayag", "Chamoli", "Uttarkashi"]:

        if city["city"] == "Rudraprayag":
            dham = "🛕 Kedarnath"

        elif city["city"] == "Chamoli":
            dham = "🛕 Badrinath"

        else:

            char_dham_cards += f"""

<div class="weather-card">

<h2>

🛕 Gangotri

</h2>

<p>

📍 Uttarkashi

</p>

{create_weather_card(city)}

</div>

"""

            dham = "🛕 Yamunotri"

        char_dham_cards += f"""

<div class="weather-card">

<h2>

{dham}

</h2>

<p>

📍 {city['city']}

</p>

{create_weather_card(city)}

</div>

"""

chardham_html = f"""

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Char Dham | Uttarakhand 360</title>

<link rel="stylesheet"
href="style.css">

</head>

<body>

{navbar}

<section class="hero">

<h1>

🛕 Char Dham Yatra

</h1>

<p>

Travel with Faith • Respect Nature • Leave No Trace

</p>

</section>

<section>

<h2>

🙏 Please Respect the Dhaam

</h2>

<div class="weather-card">

<p>

Char Dham is one of the holiest pilgrimage circuits in India.

Please remember this is a sacred place of worship before it is a tourist destination.

Travel respectfully,
keep the surroundings clean,
and honour local customs and traditions.

</p>

</div>

</section>

<section>

<h2>

🌦 Live Char Dham Weather

</h2>

<div class="weather-grid">

{char_dham_cards}

</div>

</section>

{support_section}

{footer}

<script src="script.js"></script>

</body>

</html>

"""

with open(
    "docs/chardham.html",
    "w",
    encoding="utf-8"
) as file:

    file.write(chardham_html)

print("✓ chardham.html generated")

print("✓ Ready to generate additional pages.")

print()

print("=" * 60)

print("ALL PAGES GENERATED")

print("=" * 60)

# ==========================================================
# ALERTS PAGE
# ==========================================================

print("Generating alerts.html...")

alert_cards = ""

for alert in ALERTS:

    color = "🟢"

    if alert["type"] == "advisory":
        color = "🟡"

    elif alert["type"] == "warning":
        color = "🟠"

    elif alert["type"] == "emergency":
        color = "🔴"

    alert_cards += f"""

<div class="weather-card">

<h2>

{color} {alert['title']}

</h2>

<p>

<b>📍 Area:</b> {alert['district']}

</p>

<p>

<b>🏛 Source:</b> {alert['source']}

</p>

<p>

<b>🕒 Issued:</b> {alert['issued'] if alert['issued'] else 'Latest Check'}

</p>

<p>

{alert['message']}

</p>

</div>

"""

# ==========================================================
# PUBLISH TO BLOGGER
# ==========================================================

titles = [
    "🌦 Uttarakhand Weather Brief",
    "🏔 Live Weather Across Uttarakhand",
    "🛕 Char Dham Weather Update",
    "🌄 Mountain Weather Report",
    "🚗 Uttarakhand Travel Weather",
    "🌧 Latest Weather Across Uttarakhand",
]

import random

blog_title = f"🌦 Uttarakhand Weather Brief | {last_updated}"

blog_content = f"""
<h1>🌦 Uttarakhand Weather Brief</h1>

<p><strong>{last_updated}</strong></p>

<hr>

<h2>🚧 Uttarakhand 360 is currently in BETA</h2>

<p>
Welcome to the early version of <strong>Uttarakhand 360</strong>.
We're constantly adding new features including district weather,
Char Dham updates, road conditions, travel information and much more.
Thank you for being part of the journey!
</p>

<hr>

<h2>🔥 Today's Weather Highlights</h2>

<ul>
<li>🔥 Warmest Place: <strong>{warmest['city']}</strong> ({warmest['temperature']}°C)</li>

<li>❄ Coldest Place: <strong>{coldest['city']}</strong> ({coldest['temperature']}°C)</li>

<li>💨 Strongest Winds: <strong>{windiest['city']}</strong> ({windiest['wind']} km/h)</li>

<li>💧 Highest Humidity: <strong>{highest_humidity['city']}</strong> ({highest_humidity['humidity']}%)</li>

<li>☀ Highest UV: <strong>{highest_uv['city']}</strong></li>

<li>👀 Best Visibility: <strong>{best_visibility['city']}</strong></li>
</ul>

<hr>

<h2>🏔 Live Coverage Available</h2>

<p>
✅ Major Cities<br>
✅ Hill Stations<br>
✅ District Headquarters<br>
✅ Char Dham Route<br>
✅ Tourist Destinations<br>
✅ Hourly Weather Updates
</p>

<p>
📍 Covering <strong>30+ destinations</strong> across Uttarakhand.
</p>

<hr>

<h2>🛕 Want More?</h2>

<p>
✔ Live Weather Dashboard<br>
✔ Char Dham Conditions<br>
✔ District-wise Weather<br>
✔ Mountain Destinations<br>
✔ Travel Information<br>
✔ Hourly Updates
</p>

<p>
<strong>All available on Uttarakhand 360.</strong>
</p>

<hr>

<div style="text-align:center;padding:20px;background:#f5f5f5;border-radius:10px;">

<h2>🌐 Explore the Complete Dashboard</h2>

<p>
Real-time weather for 30+ destinations across Uttarakhand.
</p>

<p>

<a href="https://aadi-blip-lab.github.io/uttarakhand-360/"
style="
background:#0d6efd;
color:white;
padding:12px 24px;
text-decoration:none;
border-radius:8px;
font-weight:bold;
">
Visit Uttarakhand 360 →
</a>

</p>

</div>

<hr>

<p style="font-size:13px;color:#777;text-align:center;">

Generated automatically by Uttarakhand 360.<br>

Weather updates every hour.<br>

More exciting features coming soon.

</p>
"""

publish_to_blogger(blog_title, blog_content)
