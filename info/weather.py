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

    bot_message = await cfg.bot.send_message(cfg.bot_id, greet + weather)
    cfg.id_list.append(bot_message.message_id)
    sql_update = f"""Update info set weather = '{weather}', weather_id = {bot_message.message_id}"""
    cfg.cursor.execute(sql_update)
    cfg.sql_connection.commit()
    await cfg.asyncio.sleep(1)
