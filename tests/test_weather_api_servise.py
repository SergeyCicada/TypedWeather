from functions.weather_api_servise import get_weather
from functions.weather_api_servise import Weather
from functions.get_coordinates import Coordinates
import responses


@responses.activate
def test_get_weather():
    valid_json_answer = {
            "coord": {
                "lon": 49.7265,
                "lat": 51.1986
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 14.33,
                "feels_like": 12.7,
                "temp_min": 14.11,
                "temp_max": 14.11,
                "pressure": 1015,
                "humidity": 43,
                "sea_level": 1015,
                "grnd_level": 1004
            },
            "visibility": 10000,
            "wind": {
                "speed": 7.84,
                "deg": 173,
                "gust": 11.98
            },
            "clouds": {
                "all": 0
            },
            "dt": 1697441071,
            "sys": {
                "country": "RU",
                "sunrise": 1697425507,
                "sunset": 1697464085
            },
            "timezone": 14400,
            "id": 513328,
            "name": "Ozinki",
            "cod": 200
        }

    responses.add(method=responses.GET, url="https://api.openweathermap.org/data/2.5/weather?lat=51.198559&lon=49"
                                            ".72654&appid=5f9f44b23563b9a26ac812dc60fe37a0&units=metric",
                  json=valid_json_answer, status=200)

    assert get_weather(Coordinates(latitude=51.198559, longitude=49.72654)) == Weather(temperature=14.33, weather_type='Clear')
