import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "8d33ca280e8e6282c3bf829e1efd5672"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
URL = "https://official-joke-api.appspot.com/jokes/ten"

def get_ten_jokes() -> Dict:
    res = requests.get(URL)
    return res.json()

def main():
    temp = get_weather("London")
    print(temp)
    print("---")
    jokes = get_ten_jokes()
    print(jokes)

if __name__ == "__main__":
    main()