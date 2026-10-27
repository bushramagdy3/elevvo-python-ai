import requests
import dotenv

WEATHER_API_KEY = dotenv.get_key("WEATHER_API_KEY")

def getWheather(city :str):
    '''Returns the weather of city'''

    url = f"http://api.weatherapi.com/v1/current.json/key={WEATHER_API_KEY}&q='{city}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    raise Exception(f"Cannot retreive weather data: {response.status_code}")

if __name__ == "__main__":
    city = input()

    weather = getWheather(city)
