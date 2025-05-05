from enum import Enum

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
     KeyboardButton,
    ReplyKeyboardMarkup,
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import job_scheduler
from handlers.quote_handler import send_quote_using_chat_id
from handlers.weather_handler import send_weather_using_chat_id


class SubscribeHandlerState(StatesGroup):
    subscribe_option = State()
    weather_city = State()


class SubscribeOption(Enum):
    WEATHER = "weather"
    QUOTE = "quote"


router = Router()


@router.message(Command("subscribe"))
async def subscribe_command(message: Message, state: FSMContext):
    await state.set_state(SubscribeHandlerState.subscribe_option)

    keyboard = [[ KeyboardButton(text=option.value) for option in SubscribeOption]]
    await message.answer(
        text=f"Выберите тип подписки: **weather** или **quote**",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=keyboard,
            resize_keyboard=True,
        ),
        parse_mode='Markdown',
    )


@router.message(
    SubscribeHandlerState.subscribe_option,
    F.text.casefold() == SubscribeOption.QUOTE.value,
)
async def process_quote_subscribe_option(message: Message, state: FSMContext):
    await state.clear()

    message_chat_id = message.chat.id
    job_scheduler.add_job(
        send_quote_using_chat_id,
        'interval',
        days=1,
        args=(message_chat_id,),
        id=f"{SubscribeOption.QUOTE.value}_{message_chat_id}",
        replace_existing=True,
    )
    await message.answer("Вы подписаны на рассылку мотивирующих цитат")


@router.message(
    SubscribeHandlerState.subscribe_option,
    F.text.casefold() == SubscribeOption.WEATHER.value,
)
async def process_weather_subscribe_option(message: Message, state: FSMContext):
    await state.set_state(SubscribeHandlerState.weather_city)
    await message.answer("Введите город")


@router.message(
    SubscribeHandlerState.subscribe_option,
)
async def process_unknown_subscribe_option(message: Message, state: FSMContext):
    await message.answer(
        text="Введены некорректные данные. \n Допустимые значения: **weather** или **quote**",
        parse_mode='Markdown',
    )


@router.message(
    SubscribeHandlerState.weather_city,
)
async def process_select_weather_city(message: Message, state: FSMContext):
    message_chat_id = message.chat.id
    city_name = message.text

    job_scheduler.add_job(
        send_weather_using_chat_id,
        'interval',
        days=1,
        args=(message_chat_id, city_name),
        id=f"{SubscribeOption.WEATHER.value}_{message_chat_id}",
        replace_existing=True,
    )

    await message.answer("Вы подписаны на рассылку погоды")
    await state.clear()
