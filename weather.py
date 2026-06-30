import os
import requests
from datetime import datetime
from cities import CITIES

API_KEY = os.getenv("WEATHER_API_KEY")

rows = ""

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

html = f"""
<!DOCTYPE html>
<html>
<head>
<title>Uttarakhand 360 Weather</title>

<style>

body{{
font-family:Arial;
background:#f2f2f2;
padding:30px;
}}

table{{
width:100%;
border-collapse:collapse;
background:white;
}}

th,td{{
padding:12px;
border:1px solid #ddd;
text-align:center;
}}

th{{
background:#0b5394;
color:white;
}}

h1{{
color:#0b5394;
}}

</style>

</head>

<body>

<h1>🌦 Uttarakhand 360 Weather</h1>

<p><b>Last Updated:</b> {datetime.now().strftime("%d %B %Y %I:%M %p")}</p>

<table>

<tr>
<th>City</th>
<th>Temperature</th>
<th>Condition</th>
<th>Humidity</th>
<th>Wind</th>
</tr>

{rows}

</table>

</body>
</html>
"""

os.makedirs("docs", exist_ok=True)

with open("docs/index.html", "w", encoding="utf-8") as file:
    file.write(html)

print("\nWebsite Generated Successfully!")
