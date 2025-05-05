from typing import Any

import requests

from config import command_line_args


def get_weather_from_city_name(city_name: str) -> dict[str, Any]:
    latitude_and_longitude = get_latitude_and_longitude_from_city_name(city_name)
    params = {
        "lat": latitude_and_longitude[0],
        "lon": latitude_and_longitude[1],
        "appid": command_line_args.weather_api_key,
        "units": "metric",
        "lang": "ru",
    }
    request = requests.get(
        url="https://api.openweathermap.org/data/2.5/weather",
        params=params,
    )

    return process_weather_data(request_body=request.json())


def get_latitude_and_longitude_from_city_name(city_name: str) -> tuple[Any, Any]:
    params = {
        "q": city_name,
        "appid": command_line_args.weather_api_key,
        "limit": 1,
    }
    request = requests.get(
        url="http://api.openweathermap.org/geo/1.0/direct",
        params=params,
    )
    request_body = request.json()
    return request_body[0]["lat"], request_body[0]["lon"]


def process_weather_data(request_body: dict[str, Any]) -> dict[str, Any]:
    return {
        "weather": request_body["weather"][0]["description"],
        "temp": request_body["main"]["temp"],
        "temp_feels_like": request_body["main"]["feels_like"],
        "visibility": request_body["visibility"],
        "wind_speed": request_body["wind"]["speed"],
        "wind_gust": request_body["wind"].get("gust"),
    }
