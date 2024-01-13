from functions.format_weather import format_weather
from functions.weather_api_servise import Weather


def test_format_weather():
    assert format_weather(Weather(temperature=14.33, weather_type="Clear")) == 'Temperature: 14.33, Weather Type: Clear'
