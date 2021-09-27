import cfg
import sql
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

    sql_weather, sql_id = await cfg.asyncio.create_task(sql.select('weather'))
    print(f'{sql_weather} - {sql_id}')

    if weather != sql_weather:
        if sql_id == 0:
            bot_message = await cfg.bot.send_message(cfg.bot_id, greet + weather, disable_notification=True)
            cfg.id_list.append(bot_message.message_id)
            await cfg.bot.pin_chat_message(cfg.bot_id, bot_message.message_id)
            await cfg.asyncio.create_task(sql.update(name=weather, message_id=bot_message.message_id))
            await cfg.asyncio.sleep(1)
        else:
            await cfg.bot.edit_message_text(greet + weather, cfg.bot_id, sql_id)
            await cfg.asyncio.create_task(sql.update(name=weather, message_id=None))
            await cfg.asyncio.sleep(1)

