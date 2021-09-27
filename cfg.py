import os
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

''' DateTime '''
date = datetime.now().strftime('%Y-%m-%d')
time = datetime.now().strftime('%H:%M:%S')
dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


''' AIOGram '''
bot_name = os.getenv('token')
bot_id = os.getenv('id')
bot = Bot(token=bot_name)
dp = Dispatcher(bot)

# Global
id_list = []