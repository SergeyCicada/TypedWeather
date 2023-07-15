from geopy.geocoders import Nominatim
from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates(city: str) -> Coordinates:
    """Request in GPS API service. Return latitude and longitude"""
    geolocator = Nominatim(user_agent="weather")
    location = geolocator.geocode(city)
    return Coordinates(latitude=location.latitude, longitude=location.longitude)



