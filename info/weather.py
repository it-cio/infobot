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
    cfg.weather_message_id.append(bot_message.message_id)
    await cfg.asyncio.sleep(1)
