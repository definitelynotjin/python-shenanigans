import requests
import toml
import json

# Jakarta
# with open("weather_config.toml") as f:
#     weather_config = toml.load(f)

# London, importing config into the app
with open("weather_config.json") as f:
    weather_config = json.load(f)
# Assign the api key and city from the config file
api_key = weather_config["weather"]["api_key"]
city = weather_config["weather"]["city"]

# URL of the API
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

try:
    response = requests.get(url, timeout=10)
    data = response.json()
    if response.status_code != 200:
        print("API Error:", response.status_code)
    else:
        print("Status code: ", response.status_code)
        print("Location: ", data["location"]["name"])
        print("Country: ", data["location"]["country"])
        print("Here is the temperature:", data["current"]["temp_c"])
        print("Weather data: ", data["current"]["condition"]["text"])
        print("Humidity: ", data["current"]["humidity"], "%")
        if data["current"]["precip_mm"] > 0:
            print("Rain expected ")
        else:
            print("Chance to rain: ")
except requests.RequestException:
    print("Timeout Error")
