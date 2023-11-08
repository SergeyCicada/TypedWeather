from functions.weather_api_servise import *


def format_weather(weather: Weather) -> str:
    """Formats weather to string"""
    temperature = str(weather.temperature)
    weather_type = weather.weather_type
    str_for_flask = f"Temperature: {temperature}, Weather Type: {weather_type}"
    return str_for_flask
