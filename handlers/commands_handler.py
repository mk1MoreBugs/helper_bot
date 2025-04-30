from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


from dispatcher import dp, bot


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я твой Telegram-бот! 🚀")


@dp.message(Command("help"))
async def help_command(message: Message):
    bot_commands = await bot.get_my_commands()
    await message.answer(str(bot_commands))


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

"""
@dp.callback_query('help_button')
async def process_callback(callback_query: CallbackQuery):
    if callback_query.data == "weather_button":
        await bot.answer_callback_query(callback_query.id, text="Вы нажали кнопку 1")
    elif callback_query.data == "quote_button":
        await bot.answer_callback_query(callback_query.id, text="Вы нажали кнопку 2")
    elif callback_query.data == "subscribe_button":
        await bot.answer_callback_query(callback_query.id, text="Вы нажали кнопку 2")
    elif callback_query.data == "help_button":
        await help_command(message=callback_query.message)
"""
