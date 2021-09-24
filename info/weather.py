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

    await cfg.bot.send_message(cfg.bot_id, greet + weather)
    await cfg.asyncio.sleep(1)
