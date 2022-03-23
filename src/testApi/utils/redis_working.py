import aioredis

from settings import REDIS_URL


def redis_connection():
    return aioredis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)

async def get_value(key):
    redis = redis_connection()
    async with redis.client() as conn:
        return await conn.get(key)




async def set_value(key, val):
    redis = redis_connection()
    async with redis.client() as conn:

        await conn.set(key, val)










