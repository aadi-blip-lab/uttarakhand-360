import os
import requests
from datetime import datetime
from zoneinfo import ZoneInfo
from cities import CITIES

API_KEY = os.getenv("WEATHER_API_KEY")

rows = ""
cards = ""

print("=" * 50)
print("UTTARAKHAND 360 WEATHER REPORT")
print("=" * 50)

for city in CITIES:

    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        name = data["location"]["name"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]

        print(f"\n{name} - {temp}°C")

        rows += f"""
        <tr>
            <td>{name}</td>
            <td>{temp}°C</td>
            <td>{condition}</td>
            <td>{humidity}%</td>
            <td>{wind} km/h</td>
        </tr>
        """
        cards += f"""
<div class="weather-card">

<h2>{name}</h2>

<div class="temp">{temp}°C</div>

<p>{condition}</p>

<p>💧 {humidity}%</p>

<p>💨 {wind} km/h</p>

</div>
"""

html = f"""
<!DOCTYPE html>
<html>
<head>
<title>Uttarakhand 360 | Live Weather Dashboard</title>

<style>

.cards{
display:flex;
flex-wrap:wrap;
gap:20px;
margin-bottom:30px;
}

.weather-card{
background:white;
width:220px;
padding:20px;
border-radius:15px;
box-shadow:0 5px 15px rgba(0,0,0,0.1);
text-align:center;
transition:0.3s;
}

.weather-card:hover{
transform:translateY(-5px);
}

.temp{
font-size:36px;
font-weight:bold;
color:#0b5394;
}

body {{
    font-family: Arial, sans-serif;
    background: #f2f2f2;
    margin: 0;
    padding: 0;
}}

.navbar {{
    background: #0b5394;
    color: white;
    padding: 15px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.logo {{
    font-size: 24px;
    font-weight: bold;
}}

.menu a {{
    color: white;
    text-decoration: none;
    margin-left: 20px;
    font-weight: bold;
}}

.container {{
    max-width: 1200px;
    margin: auto;
    padding: 30px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 10px;
    overflow: hidden;
}}

th, td {{
    padding: 14px;
    border-bottom: 1px solid #ddd;
    text-align: center;
}}

th {{
    background: #0b5394;
    color: white;
}}

h1 {{
    color: #0b5394;
    margin-bottom: 5px;
}}

p {{
    color: #555;
}}

</style>

</head>

<body>

<div class="navbar">
    <div class="logo">🌦 Uttarakhand 360</div>

    <div class="menu">
        <a href="#">Home</a>
        <a href="#">Weather</a>
        <a href="#">Districts</a>
        <a href="#">Travel</a>
        <a href="#">About</a>
    </div>
</div>

<div class="container">

<h1>Live Weather Dashboard</h1>

<p><strong>🌦 Weather Last Updated:</strong> {datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%d %B %Y • %I:%M:%S %p")}</p>

<p><strong>🕒 Current India Time:</strong> <span id="clock"></span></p>

<table>

<tr>
<th>City</th>
<th>Temperature</th>
<th>Condition</th>
<th>Humidity</th>
<th>Wind</th>
</tr>

{rows}

<div class="cards">

{cards}

</div>

</table>

</div>

<script>

function updateClock() {{

    const now = new Date();

    document.getElementById("clock").innerHTML =
        now.toLocaleTimeString("en-IN", {{
            timeZone: "Asia/Kolkata",
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
            hour12: true
        }});

}}

updateClock();

setInterval(updateClock, 1000);

</script>

</body>
</html>
"""

os.makedirs("docs", exist_ok=True)

with open("docs/index.html", "w", encoding="utf-8") as file:
    file.write(html)

print("\nWebsite Generated Successfully!")
