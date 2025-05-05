from aiogram import Bot

from utils.configure_scheduler import configure_scheduler
from utils.parse_command_line_arguments import parse_command_line_arguments

command_line_args = parse_command_line_arguments()

bot = Bot(token=command_line_args.tg_bot_key)
job_scheduler = configure_scheduler()
