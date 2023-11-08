import requests
from functions.get_coordinates import *
from typing import NamedTuple
from config import OPENWEATHER_KEY

Celsius = float  # type - Literal


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: str


def get_weather(coordinates: Coordinates) -> Weather:
    """Requests weather in OpenWeather API and return weather"""

    w = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={coordinates.latitude}&lon={coordinates.longitude}&appid={OPENWEATHER_KEY}&units=metric')
    weather = w.json()
    return Weather(
        temperature=weather['main']['temp'],
        weather_type=weather['weather'][0]['main']
    )






