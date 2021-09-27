import cfg
import sql
import requests


async def weather_request(greet):
    url = 'https://wttr.in/Sochi'  # write the name of your city here
    weather_parameters = {
        'format': 2,
        '0': '',
        'T': '',
        'M': '',
        'lang': 'ru'
    }
    forecast = requests.get(url, params=weather_parameters).text

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

