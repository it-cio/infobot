import os
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
# from sqlalchemy import create_engine, MetaData, text

load_dotenv()

''' DateTime '''
date = datetime.now().strftime('%Y-%m-%d')
time = datetime.now().strftime('%H:%M:%S')
dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# ''' MySQL '''
# engine = create_engine(os.getenv('engine'))
# metadata = MetaData()
# connection = engine.connect()


''' AIOGram '''
bot_name = os.getenv('token')
bot_id = os.getenv('id')

# Global
user_id = ''
search_id = ''

bot = Bot(token=bot_name)
dp = Dispatcher(bot)