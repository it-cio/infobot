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
connection = sqlite3.connect('database.db')
print("SQL-Connection is established")
connection.execute("CREATE table IF NOT EXISTS info (weather TEXT, weather_id INTEGER, UNIQUE(weather, weather_id));")
connection.execute("INSERT INTO info (weather, weather_id) VALUES ('forecast', 0);")


def close_sql():
    # global connection
    connection.execute("DROP table IF EXISTS info")
    if connection:
        print("Total SQL-Requests: ", connection.total_changes)
        connection.close()
        print("SQL-Connection is closed")