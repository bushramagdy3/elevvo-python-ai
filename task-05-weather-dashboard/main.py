import requests
import dotenv
import sys

WEATHER_API_KEY = dotenv.get_key("WEATHER_API_KEY")

def getWheather(city :str):
    '''Returns the weather of city'''

    url = f"http://api.weatherapi.com/v1/current.json/key={WEATHER_API_KEY}&q='{city}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    raise Exception(f"Cannot retreive weather data: {response.status_code}")

def read_info(weather_info :dict, celsius :bool):
    print(f"Condition: {weather_info["condition:text"]}.")
    print(f"Temprature: {weather_info["temp_c"] if celsius else weather_info["temp_f"]} degrees.")
    print(f"Feels Like: {weather_info["feelslike_c"] if celsius else weather_info["feelslike_f"]} degrees.")
    print(f"Humidity: {weather_info["humidity"]}%")
    print(f"Cloud: {weather_info["cloud"]}%")
    print(f"is_day: {"Yes" if weather_info["is_day"] == 1 else "No"}.")
    print(f"UV: {weather_info["uv"]}%")

if __name__ == "__main__":
    print("Welcome to Bushra's weather dashboard!")

    city = input("Please enter your city:")
    celsius = input("Would you like to read temprature in celsius (Y) or fahrenheit (N)?")
    celsius = True if input == 'Y' else False

    try:
        weather_info = getWheather(city)
    except Exception as e:
        print(f"Wasn't able to get information for {city}, please try again")
        sys.exit()

    read_info(weather_info, celsius)
