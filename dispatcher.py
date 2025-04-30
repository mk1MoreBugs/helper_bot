from aiogram import Bot, Dispatcher

from utils.get_bot_token import get_bot_token

bot = Bot(token=get_bot_token())
dp = Dispatcher()
