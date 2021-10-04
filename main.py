import cfg
import sql
import asyncio
import aioschedule

from framework.bot import run, on_startup
from routes import route_weather, route_covid


# # type '/weather' in chat to get weather forecast
# @cfg.dp.message_handler(commands=['weather'])
# async def bot_answer(message: types.Message):
#     sql_forecast, sql_id = await cfg.asyncio.create_task(sql.select('weather'))
#     bot_message = await cfg.bot.send_message(cfg.bot_id, f'Weather forecast: {sql_forecast}')
#     cfg.id_list.append(bot_message.message_id)
#     await message.delete()
#     await cfg.asyncio.sleep(1)


# choose a time interval to run functions
async def scheduler():
    aioschedule.every(15).to(30).seconds.do(route_weather, greet='Прогноз погоды: ')
    aioschedule.every(30).seconds.do(route_covid, greet='Коронавирус\nоперативные данные\n\n')
    while True:
        await aioschedule.run_pending()
        await cfg.asyncio.sleep(1)


async def tasks():
    asyncio.create_task(sql.create())
    asyncio.create_task(scheduler())
    await cfg.asyncio.sleep(1)
# asyncio.create_task(sql.close())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks())
    run()