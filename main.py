import cfg
import aioschedule
from aiogram import executor, types

from info.weather import weather_request


# @cfg.dp.message_handler(commands=['search'])
# async def bot_answer(message: types.Message):
#     answer = name_recognition(message)
#     await cfg.bot.send_message(cfg.user_id, answer)
#     try:
#         await cfg.bot.delete_message(cfg.bot_id, cfg.search_id)
#     except:
#         await cfg.bot.delete_message(cfg.user_id, cfg.search_id)
#     finally:
#         await cfg.asyncio.sleep(1)


@cfg.dp.message_handler(content_types=['pinned_message'])
async def delete_pinned(message: types.Message):
    await message.delete()


async def scheduler():
    aioschedule.every(5).to(10).seconds.do(weather_request, greet='Погода в Сочи:')
    while True:
        await aioschedule.run_pending()
        await cfg.asyncio.sleep(1)


async def on_startup(_):
    cfg.asyncio.create_task(scheduler())
    await cfg.bot.send_message(cfg.bot_id, 'Бот работает в тестовом режиме!')
    await cfg.asyncio.sleep(1)


'''
async def on_shutdown(_):
    sql_id = cfg.connection.execute(cfg.text(f'SELECT weather_id, covid_id FROM info;')).fetchone()
    if sql_id[0] != '0000':
        await cfg.bot.delete_message(cfg.bot_id, sql_id[0])
    if sql_id[1] != '0000':
        await cfg.bot.delete_message(cfg.bot_id, sql_id[1])
    cfg.connection.execute(cfg.text(f'UPDATE info SET weather_id = "0000", covid_id = "0000";'))
    await asyncio.sleep(1)
'''

if __name__ == '__main__':
    try:
        executor.start_polling(cfg.dp, skip_updates=True, on_startup=on_startup)  # on_shutdown=on_shutdown
    except Exception as ex:
        print(f'({cfg.date} {cfg.time}) AioGram-Error: {ex}')
