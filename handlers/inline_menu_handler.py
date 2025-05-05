from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)

from config import bot
from handlers.commands_handler import quote_command, help_command
from handlers.subscribe_handler import subscribe_command

router = Router()


@router.message(Command('inline_menu'))
async def inline_menu_command(message: Message):
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


@router.callback_query()
async def process_callback(callback_query: CallbackQuery):
    if callback_query.data == "weather_button":
        await bot.answer_callback_query(callback_query.id, text="Ещё не реализовано")
    elif callback_query.data == "quote_button":
        await quote_command(message=callback_query.message)
    elif callback_query.data == "subscribe_button":
        await subscribe_command(message=callback_query.message)
    elif callback_query.data == "help_button":
        await help_command(message=callback_query.message)