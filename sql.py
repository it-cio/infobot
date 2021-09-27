import cfg
import aiosqlite


async def create():
    async with aiosqlite.connect('database.db') as db:
        print("SQL-Connection is established")
        await db.execute("DROP table IF EXISTS info")
        await db.execute("CREATE table IF NOT EXISTS info (weather TEXT, weather_id INTEGER, UNIQUE(weather, weather_id));")
        await db.execute("INSERT INTO info (weather, weather_id) VALUES ('forecast', 0);")
        await db.commit()


async def select(name):
    async with aiosqlite.connect('database.db') as db:
        cursor = await db.execute(f"SELECT {name}, {name}_id FROM info;")
        sql_request = await cursor.fetchone()
        sql_name = sql_request[0]
        sql_id = sql_request[1]
        return sql_name, sql_id


async def update(name, message_id, **kwargs):
    async with aiosqlite.connect('database.db') as db:
        cursor = await db.execute(f"SELECT weather_id FROM info;")
        sql_request = await cursor.fetchone()
        if sql_request == 0:
            await db.execute(f"UPDATE info SET weather  = '{name}', weather_id = '{message_id}';")
        else:
            await db.execute(f"UPDATE info SET weather  = '{name}';")
        await db.commit()


async def close():
    async with aiosqlite.connect('database.db') as db:
        # await db.execute("DROP table IF EXISTS info")
        print("SQL-Connection is closed")