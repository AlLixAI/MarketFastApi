import time
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from src.auth.base_config import auth_backend, fastapi_users
from src.operations.product.router import router as router_product
from src.operations.tasks.router import router as router_tasks
from src.auth.schemas import UserCreate, UserRead

from redis import asyncio as aioredis

app = FastAPI(
    title="Magazin Clothes"
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(router_product)
app.include_router(router_tasks)

# @app.get("/")
# @cache(expire=60)
# async def index():
#     time.sleep(2)
#     return dict(hello="world")


@asynccontextmanager # Нужен для подключения редиса к app, его инициализация, и подключение к нему. Через @cache можно кешировать запросы и это четко
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield
    await redis.close()

app.router.lifespan_context = lifespan