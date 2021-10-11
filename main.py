import asyncio
import telegram
from data import sql, routes


async def tasks():
    asyncio.create_task(routes.scheduler())
    asyncio.create_task(routes.ami_listener())
    await asyncio.sleep(1)
asyncio.get_event_loop().run_until_complete(tasks())


if __name__ == '__main__':
    telegram.bot.run(startup=sql.create_table, shutdown=sql.drop_table)