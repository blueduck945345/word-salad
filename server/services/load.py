'''Add to redis set of lines'''
from redis.asyncio import Redis
from .constants import REDIS_LINES_SET

async def load(text: str, r: Redis):
    lines = [line for line in text.splitlines() if line.strip()]
    ## sanitized lines to avoid empty strings between repeated newlines
    ## and trailing whitespace
    if lines:
        await r.sadd(REDIS_LINES_SET, *lines)