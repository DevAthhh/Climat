from typing import Any

from .get_weather import get_weather


def get_objects_for_context(request: Any) -> dict|str:
    """
    This is a function, which return
    an information about weather

    :param request:
    :return:
    """

    data_of_weather: list = [None, None, None]
    try:
        city = request.session.get('city')
        if city:
            data_of_weather = get_weather(city)
    except Exception as e:
        return f'Error: {e}'

    dict_of_weather_data: dict = {
        'city': city,
        'temperature': data_of_weather[1],
        'feels_like': data_of_weather[2],
        'weather': data_of_weather[0],
    }

    return dict_of_weather_data