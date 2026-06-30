import requests

API_KEY = "YOUR_WEATHERAPI_KEY"

CITY = "Dehradun"

url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"City: {data['location']['name']}")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")
else:
    print("Error fetching weather")
