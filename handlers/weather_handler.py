import re

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from config import bot
from utils.parse_city_arg import parse_city_arg


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
        await message.answer("city:" + city_in_message)


@router.message(WeatherHandlerState.weather_city)
async def process_select_weather_city(message: Message, state: FSMContext):
    # TODO: impl get weather

    message_chat_id = message.chat.id
    await send_weather_using_chat_id(chat_id=message_chat_id)
    await state.clear()


async def send_weather_using_chat_id(chat_id: int):
    quote_message = "Тестовая погода"
    await bot.send_message(chat_id=chat_id, text=quote_message)
