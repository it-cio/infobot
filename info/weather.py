import cfg
import requests


async def weather_request(greet):
    url = 'https://wttr.in/Sochi'
    weather_parameters = {
        'format': 2,
        '0': '',
        'T': '',
        'M': '',
        'lang': 'ru'
    }
    weather = requests.get(url, params=weather_parameters).text

    sql_request = cfg.connection.execute(f"SELECT weather, weather_id FROM info;").fetchone()
    sql_weather = sql_request[0]
    sql_id = sql_request[1]
    print(f'{sql_weather} - {sql_id}')

    if weather != sql_weather:
        if sql_id == 0:
            bot_message = await cfg.bot.send_message(cfg.bot_id, greet + weather, disable_notification=True)
            cfg.id_list.append(bot_message.message_id)
            await cfg.bot.pin_chat_message(cfg.bot_id, bot_message.message_id)
            cfg.connection.execute(f"UPDATE info SET weather  = '{weather}', weather_id = '{bot_message.message_id}';")
            cfg.connection.commit()
            await cfg.asyncio.sleep(1)
        else:
            await cfg.bot.edit_message_text(greet + weather, cfg.bot_id, sql_id)
            cfg.connection.execute(f"UPDATE info SET weather  = '{weather}';")
            cfg.connection.commit()
            await cfg.asyncio.sleep(1)
