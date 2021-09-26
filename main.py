import cfg
import aioschedule
from aiogram import executor, types

from info.weather import weather_request


@cfg.dp.message_handler(content_types=['pinned_message'])
async def delete_pinned(message: types.Message):
    await message.delete()


# @cfg.dp.message_handler(commands=['weather'])
# async def bot_answer(message: types.Message):
#     bot_message = await cfg.bot.send_message(cfg.bot_id, weather_request(message))
#     cfg.id_list.append(bot_message.message_id)
#     await cfg.asyncio.sleep(1)


async def scheduler():
    aioschedule.every(5).to(10).seconds.do(weather_request, greet='Погода в Сочи:')
    while True:
        await aioschedule.run_pending()
        await cfg.asyncio.sleep(1)


async def on_startup(_):
    cfg.asyncio.create_task(scheduler())
    bot_message = await cfg.bot.send_message(cfg.bot_id, 'Бот работает в тестовом режиме!')
    cfg.id_list.append(bot_message.message_id)
    await cfg.asyncio.sleep(1)


async def on_shutdown(_):
    cfg.close_sql()
    for message_id in cfg.id_list:
        await cfg.bot.delete_message(cfg.bot_id, message_id)
    await cfg.asyncio.sleep(1)


if __name__ == '__main__':
    try:
        executor.start_polling(cfg.dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    except Exception as ex:
        print(f'({cfg.date} {cfg.time}) AioGram-Error: {ex}')
