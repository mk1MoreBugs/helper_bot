import re

from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)

from config import dp, bot, job_scheduler
from utils.generate_bot_help_message import generate_bot_help_message
from utils.parse_city_arg import parse_city_arg


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я твой Telegram-бот! 🚀")


@dp.message(Command("weather", re.compile(r"^weather [а-яА-Яa-zA-Z]+\D+-*")))
async def weather_command(message: Message):
    city_in_message: str = parse_city_arg(message)
    await message.answer("city:" + city_in_message)


@dp.message(Command("quote"))
async def quote_command(message: Message):
    await send_quote_using_chat_id(chat_id=message.chat.id)


@dp.message(Command("subscribe"))
async def subscribe_command(message: Message):
    add_job_args = (message.chat.id,)
    job_scheduler.add_job(send_quote_using_chat_id, 'interval', seconds=10, args=add_job_args)

    await message.answer("Вы подписаны")


async def send_quote_using_chat_id(chat_id: int):
    quote_message = "Тестовая цитата"
    await bot.send_message(chat_id=chat_id, text=quote_message)


@dp.message(Command("help"))
async def help_command(message: Message):
    help_message = await generate_bot_help_message()
    await message.answer(help_message)


@dp.message(Command('inline_menu'))
async def menu_handler(message: Message):
    keyboard_buttons = [
        [
            InlineKeyboardButton(text="weather", callback_data="weather_button"),
            InlineKeyboardButton(text="quote", callback_data="quote_button"),
            InlineKeyboardButton(text="subscribe", callback_data="subscribe_button"),
            InlineKeyboardButton(text="help", callback_data="help_button"),
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    await message.answer(
        text='Список команд:',
        reply_markup=keyboard
    )


@dp.callback_query()
async def process_callback(callback_query: CallbackQuery):
    if callback_query.data == "weather_button":
        await bot.answer_callback_query(callback_query.id, text="Ещё не реализовано")
    elif callback_query.data == "quote_button":
        await quote_command(message=callback_query.message)
    elif callback_query.data == "subscribe_button":
        await subscribe_command(message=callback_query.message)
    elif callback_query.data == "help_button":
        await help_command(message=callback_query.message)
