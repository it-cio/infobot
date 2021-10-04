import cfg
import sql
import asyncio
import aioschedule
import routes


# choose a time interval to run functions
async def scheduler():
    aioschedule.every(15).to(30).seconds.do(routes.route_weather, greet='Прогноз погоды: ')
    aioschedule.every(30).seconds.do(routes.route_covid, greet='Коронавирус\nоперативные данные\n\n')
    while True:
        await aioschedule.run_pending()
        await cfg.asyncio.sleep(1)


async def tasks():
    asyncio.create_task(scheduler())
    await cfg.asyncio.sleep(1)
asyncio.get_event_loop().run_until_complete(tasks())


if __name__ == '__main__':
    routes.bot_run()