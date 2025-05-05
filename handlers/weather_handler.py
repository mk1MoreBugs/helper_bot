import re

import requests
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from config import bot
from utils.parse_city_arg import parse_city_arg
from utils.weather_api import get_weather_from_city_name


class WeatherHandlerState(StatesGroup):
    weather_city = State()


router = Router()


@router.message(Command("weather", re.compile(r"weather [а-яА-Яa-zA-Z]+\D+-*")))
async def weather_command(message: Message, state: FSMContext):
    city_in_message: str = parse_city_arg(message)
    if len(city_in_message) == 0:
        await state.set_state(WeatherHandlerState.weather_city)
        await message.answer("Введите город")
    else:
        await send_weather_using_chat_id(chat_id=message.chat.id, city_name=city_in_message)


@router.message(WeatherHandlerState.weather_city)
async def process_select_weather_city(message: Message, state: FSMContext):
    message_chat_id = message.chat.id
    await send_weather_using_chat_id(chat_id=message_chat_id, city_name=message.text)
    await state.clear()


async def send_weather_using_chat_id(chat_id: int, city_name: str):
    try:
        weather_data = get_weather_from_city_name(city_name)
        weather_message = (
            f"Текущая погода в {city_name}: {weather_data['weather']} \n\n"
            f"Температура: {weather_data['temp']} ℃\n"
            f"По ощущению: {weather_data['temp_feels_like']} ℃\n"
            f"Видимость: {weather_data['visibility']} м\n"
            f"Скорость ветра: {weather_data['wind_speed']} м/c\n"
        )
        if weather_data["wind_gust"] is not None:
            weather_message += f"Порывы ветра: {weather_data["wind_gust"]} м/c\n"

        await bot.send_message(chat_id=chat_id, text=weather_message)

    except requests.ConnectionError:
        await bot.send_message(chat_id=chat_id, text="Не удалось выполнить запрос")
    except KeyError:
        await bot.send_message(chat_id=chat_id, text="Внутренняя ошибка")
    except IndexError:
        await bot.send_message(chat_id=chat_id, text="Не удалось выполнить запрос")
