import json
import functools

import redis.asyncio as redis
from fastapi.encoders import jsonable_encoder
from src.core.config import settings


redis_client = redis.Redis(
    host=settings.redis.host,
    port=settings.redis.port,
    decode_responses=settings.redis.decode_responses
)

def redis_cache(ttl: int = 60):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            clean_kwargs = {
                k: v for k, v in kwargs.items()
                if k != "session"
            }

            key = f"{func.__name__}:{args}:{clean_kwargs}"

            cached = await redis_client.get(key)
            if cached:
                return json.loads(cached)

            result = await func(*args, **kwargs)

            await redis_client.set(
                key,
                json.dumps(jsonable_encoder(result)),
                ex=ttl
            )
            return result

        return wrapper
    return decorator