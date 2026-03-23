from aiogram import Bot, Dispatcher
from src.config import settings

bot = Bot(token=settings.telegram.bot_token)
dp = Dispatcher()