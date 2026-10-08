'''Sample from redis set of lines'''
from redis.asyncio import Redis
from .constants import REDIS_LINES_SET

async def sample(n: int, r: Redis):
    return await r.spop(REDIS_LINES_SET, count=n)