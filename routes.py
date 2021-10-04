import cfg
import sql
from weather.forecast import weather_request
from covid.prognosis import covid_request


async def route_weather(greet):
    forecast = await weather_request()
    sql_forecast, sql_id = await cfg.asyncio.create_task(sql.select('weather'))

    if forecast != sql_forecast:
        try:
            weather_id = sql_id
            await cfg.bot.edit_message_text(greet + forecast, cfg.bot_id, weather_id)
        except Exception as ex:
            print(f'{ex} (message_id: {sql_id})')
            bot_message = await cfg.bot.send_message(cfg.bot_id, greet + forecast, disable_notification=True)
            weather_id = bot_message.message_id
            cfg.id_list.append(weather_id)
            await cfg.bot.pin_chat_message(cfg.bot_id, weather_id)
        finally:
            await cfg.asyncio.create_task(sql.update('weather', forecast, weather_id))
            await cfg.asyncio.sleep(1)


async def route_covid(greet):
    prognosis = await covid_request()
    sql_prognosis, sql_id = await cfg.asyncio.create_task(sql.select('covid'))

    if prognosis != sql_prognosis:
        try:
            bot_message = await cfg.bot.send_message(cfg.bot_id, greet + prognosis, disable_notification=True)
            cfg.id_list.append(bot_message.message_id)
            await cfg.asyncio.create_task(sql.update('covid', prognosis, bot_message.message_id))
        except Exception as ex:
            print(ex)
        finally:
            await cfg.asyncio.sleep(1)
