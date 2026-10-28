from unittest.mock import patch, MagicMock
from main import getWheather
import pytest

@patch('main.requests')
def test_successful_response(mock_requests_get):
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "location": {"name": "Cairo", "country": "Egypt"},
        "current": {
            "condition": {"text": "Sunny"},
            "temp_c": 28.0,
            "temp_f": 82.4,
            "feelslike_c": 29.0,
            "feelslike_f": 84.2,
            "humidity": 40,
            "cloud": 0,
            "is_day": 1,
            "uv": 5.0,
        },
    }

    mock_requests_get.get.return_value = fake_response

    assert getWheather("cairo") == {
        "condition": {"text": "Sunny"},
        "temp_c": 28.0,
        "temp_f": 82.4,
        "feelslike_c": 29.0,
        "feelslike_f": 84.2,
        "humidity": 40,
        "cloud": 0,
        "is_day": 1,
        "uv": 5.0,
    }

@patch('main.requests')
def test_wrong_city(mock_requests_get):
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "location": {"name": "Cairo", "country": "Egypt"},
        "current": {
            "condition": {"text": "Sunny"},
            "temp_c": 28.0,
            "temp_f": 82.4,
            "feelslike_c": 29.0,
            "feelslike_f": 84.2,
            "humidity": 40,
            "cloud": 0,
            "is_day": 1,
            "uv": 5.0,
        },
    }

    mock_requests_get.get.return_value = fake_response

    city = "cc"
    with pytest.raises(
        Exception,
        match=f"{city} isn't a valid city name"
    ):
        getWheather(city)

@patch('main.requests')
def test_timeout(mock_requests_get):

    mock_requests_get.get.side_effect = Exception("Timeout")

    with pytest.raises(
        Exception,
        match="You seem like you're not connected, please try again"
    ):
        getWheather("cairo")

@patch('main.requests')
def test_connection(mock_requests_get):

    mock_requests_get.get.side_effect = Exception("Timeout")

    with pytest.raises(
        Exception,
        match="You seem like you're not connected, please try again"
    ):
        getWheather("cairo")

