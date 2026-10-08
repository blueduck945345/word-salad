'''Dependency injection for Fast API'''

from redis.asyncio import Redis
from fastapi import Depends
from typing import Annotated
import os

def _init_redis():
    return Redis(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT")),
        decode_responses=True
    )

RedisClient = Annotated[Redis, Depends(_init_redis)]


__all__ = ["RedisClient"]