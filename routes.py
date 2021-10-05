import asyncio

from sql import create_table, select, update, drop_table
from framework.bot import send_message, edit_message, pin_message, run
from weather.forecast import weather_request
from covid.prognosis import covid_request


async def route_weather(greet):
    forecast = await weather_request()
    sql_forecast, sql_id = await asyncio.create_task(select('weather'))

    if forecast != sql_forecast:
        try:
            weather_id = sql_id
            await edit_message(greet + forecast, weather_id)
        except Exception as ex:
            print(f'{ex} (id: {sql_id})')
            weather_id = await send_message(greet + forecast)
            await pin_message(weather_id)
        finally:
            await asyncio.create_task(update('weather', forecast, weather_id))
            await asyncio.sleep(1)


async def route_covid(greet):
    prognosis = await covid_request()
    sql_prognosis, sql_id = await asyncio.create_task(select('covid'))

    if prognosis != sql_prognosis:
        try:
            covid_id = await send_message(greet + prognosis)
            await asyncio.create_task(update('covid', prognosis, covid_id))
        except Exception as ex:
            print(ex)
        finally:
            await asyncio.sleep(1)


def bot_run():
    run(startup=create_table, shutdown=drop_table)