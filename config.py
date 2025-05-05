from aiogram import Bot, Dispatcher

from utils.configure_scheduler import configure_scheduler
from utils.get_bot_token import get_bot_token

bot = Bot(token=get_bot_token())
dp = Dispatcher()
job_scheduler = configure_scheduler()
