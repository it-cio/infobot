import cfg
import sql
from weather.forecast import weather_request


async def route_weather(greet):

    forecast = await weather_request()
    sql_forecast, sql_id = await cfg.asyncio.create_task(sql.select('weather'))

    if forecast != sql_forecast:
        if sql_id == 0:
            bot_message = await cfg.bot.send_message(cfg.bot_id, greet + forecast, disable_notification=True)
            cfg.id_list.append(bot_message.message_id)
            await cfg.bot.pin_chat_message(cfg.bot_id, bot_message.message_id)
            await cfg.asyncio.create_task(sql.update('weather', forecast, bot_message.message_id))
            await cfg.asyncio.sleep(1)
        else:
            await cfg.bot.edit_message_text(greet + forecast, cfg.bot_id, sql_id)
            await cfg.asyncio.create_task(sql.update('weather', forecast, sql_id))
            await cfg.asyncio.sleep(1)



