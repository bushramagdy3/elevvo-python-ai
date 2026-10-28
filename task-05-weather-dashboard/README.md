# Task 5 — Weather Dashboard Using a Public REST API

**Level:** Level 3

**Status:** Complete

An interactive command-line weather dashboard that retrieves current conditions for a user-specified city through [WeatherAPI.com](https://www.weatherapi.com/). It displays weather information in a readable format, supports Celsius and Fahrenheit, and handles invalid locations, timeouts, and connection failures with user-facing messages.

## Requirements coverage

| Required feature | Implementation | Status |
| --- | --- | --- |
| Consume a public REST API to fetch live weather for a user-specified city | [main.py](main.py) accepts a city and uses `requests` to call WeatherAPI's current-weather endpoint over HTTPS. | Complete |
| Handle API authentication using a key configured outside the source code | `WEATHER_API_KEY` is read from a local `.env` file using `python-dotenv` and passed to the API. | Complete |
| Handle invalid cities, timeouts, and failed requests gracefully | The application checks HTTP response codes and the returned location, applies a 10-second request timeout, and displays an error message when a lookup fails. | Complete |
| Present results in a clean, readable CLI format | The CLI displays the weather condition, temperature, feels-like temperature, humidity, cloud cover, daylight status, and UV index. | Complete |

## Bonuses and additional features

**Official bonus — Automated API tests: Complete.** Tests use `pytest` and `unittest.mock` to simulate successful responses, invalid locations, unsuccessful HTTP responses, timeouts, and connection failures. Mocked requests allow the tests to run without live API calls.

Additional features:

- A choice of Celsius or Fahrenheit for temperature and feels-like readings.
- Humidity, cloud cover, daylight status, and UV index alongside the current condition.
- Leading and trailing whitespace is removed from CLI city input, and matching ignores letter case.

## Setup

Use Python 3.12 or newer. The application depends on `requests` and `python-dotenv`; dependency versions are listed in [requirements.txt](requirements.txt).

Run the following from the repository root.

Windows PowerShell:

```powershell
cd task-05-weather-dashboard
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux:

```sh
cd task-05-weather-dashboard
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### API configuration

Create an account at [WeatherAPI.com](https://www.weatherapi.com/) and obtain an API key. Create a `.env` file beside `main.py` containing:

```dotenv
WEATHER_API_KEY=your_weatherapi_key_here
```

| Setting | Purpose |
| --- | --- |
| `WEATHER_API_KEY` | Authenticates requests to WeatherAPI. |

Start the application from the task directory so it can read `.env`. The repository's `.gitignore` excludes `.env` files from version control. API access requires an internet connection and is subject to the provider's plan limits.

### Test dependency

Install `pytest` in the same virtual environment to run the automated tests:

```sh
python -m pip install pytest
```

## Usage

From the task directory with the virtual environment active:

```sh
python main.py
```

Enter a city when prompted. Enter `Y` for Celsius or `N` for Fahrenheit; the temperature choice ignores letter case and surrounding whitespace. Any response other than `Y` selects Fahrenheit.

Illustrative complete interaction; weather values change with the location and time:

```text
Welcome to Bushra's weather dashboard!
Please enter your city: Cairo
Would you like to read temprature in celsius (Y) or fahrenheit (N)? Y
Condition: Sunny.
Temprature: 28 degrees.
Feels Like: 29 degrees.
Humidity: 40%
Cloud: 0%
is_day: Yes.
UV: 5
```

Both temperature readings use the selected scale. Humidity and cloud cover are percentages; UV is an index.

If a request fails, the application displays an error and exits. For example, a connection failure or timeout displays:

```text
You seem like you're not connected, please try again
```

An unsuccessful HTTP response displays its status code. For example:

```text
Cannot retreive weather data: 400
```

A city that does not match the location name returned by the API is rejected with a city-name error. Run the application again to perform another lookup.

## Demo

**Demo video:** `TASK_5_DEMO_URL`

The demo walks through:

1. Retrieving and displaying the current weather for Cairo.
2. Selecting Celsius and Fahrenheit.
3. Entering an invalid city and displaying the error response.
4. Demonstrating a handled connection failure.
5. Running the automated tests with mocked API responses.

## Tests and evaluation

Run the test suite from `task-05-weather-dashboard`:

```sh
python -m pytest -q
```

The tests in [test_main.py](test_main.py) replace the API request with controlled fake responses or exceptions and check the weather function's behavior.

| Test case | Expected behavior |
| --- | --- |
| Successful response for a valid city | Return the weather data from the response's `current` field. |
| Returned location does not match the city | Raise a city-name error. |
| Invalid city or unsuccessful HTTP status | Raise an error that includes the HTTP status code. |
| Request timeout | Raise the application's connection-failure message. |
| Connection failure | Raise the application's connection-failure message. |

The tests exercise the API-handling function independently of changing weather data and external network availability.

## Design decisions and limitations

- **HTTPS and JSON:** Weather data is requested from `https://api.weatherapi.com/v1/current.json`. HTTP status is checked before extracting JSON weather fields.
- **Local configuration:** The API key is stored in `.env` and read with `python-dotenv`.
- **Bounded waiting:** A 10-second request timeout limits waiting during connection and response reads.
- **Location matching:** The requested city is compared with the API's returned location name after normalization. Alternative spellings, aliases, and localized names may be rejected when the names differ.
- **Error messages:** Connection failures and timeouts share a user-facing message. Other HTTP failures include a status code.
- **One lookup per run:** The CLI presents one result or error, then exits. Weather data and service availability depend on the external provider.

## Attribution

Weather data is provided by [WeatherAPI.com](https://www.weatherapi.com/). See the [API documentation](https://www.weatherapi.com/docs/) for endpoint details and response fields.
