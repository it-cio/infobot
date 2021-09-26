import os
import sqlite3
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
user_id = ''
search_id = ''
id_list = []

# SQL
sql_connection = sqlite3.connect('info.db')
cursor = sql_connection.cursor()
print("База данных подключена к SQLite")


def close_sql():
    global sql_connection
    cursor.close()
    if sql_connection:
        print("Всего строк, измененных после подключения к базе данных: ", sql_connection.total_changes)
        sql_connection.close()
        print("Соединение с SQLite закрыто")