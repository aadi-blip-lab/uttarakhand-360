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

district_html = ""

weather_page_html = ""

chardham_html = ""

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

<li><a href="index.html">🏠 Home</a></li>

<li><a href="weather.html">🌦 Weather</a></li>

<li><a href="districts.html">🗺 Districts</a></li>

<li><a href="chardham.html">🛕 Char Dham</a></li>

<li><a href="#">🥾 Treks</a></li>

<li><a href="#">📍 Places</a></li>

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

GARHWAL = [
    "Dehradun",
    "Haridwar",
    "Uttarkashi",
    "Tehri Garhwal",
    "Pauri Garhwal",
    "Rudraprayag",
    "Chamoli"
]

KUMAON = [
    "Nainital",
    "Almora",
    "Bageshwar",
    "Champawat",
    "Pithoragarh",
    "Udham Singh Nagar"
]

garhwal_cards = ""

kumaon_cards = ""


for city in cities_weather:

    card = f"""

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

</div>

"""

    if city["city"] in GARHWAL:

        garhwal_cards += card

    elif city["city"] in KUMAON:

        kumaon_cards += card


district_html = f"""

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>Districts | Uttarakhand 360</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

{navbar}

<section class="hero">

<h1>

🏔 Districts of Uttarakhand

</h1>

<p>

Live Weather across all districts.

</p>

</section>

<section>

<h2>

🏔 Garhwal Region

</h2>

<div class="weather-grid">

{garhwal_cards}

</div>

</section>

<section>

<h2>

🌄 Kumaon Region

</h2>

<div class="weather-grid">

{kumaon_cards}

</div>

</section>

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

Don't be a Gamma in a Land of Lama.

</h2>

<p>

Live Weather • Travel • Mountains • Adventure

</p>

</section>

<section>

<h2>

🌤 Live Weather Across Uttarakhand

</h2>

<div class="weather-grid">

{weather_cards}

</div>

</section>

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
