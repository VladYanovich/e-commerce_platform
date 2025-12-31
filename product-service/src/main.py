from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from src.core.config import settings
from src.api.api_v1 import router as api_v1_router
from src.db.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()

app = FastAPI(
    lifespan=lifespan
)

app.include_router(
    api_v1_router,
    prefix=settings.api.prefix
    )

if __name__ == "__main__":
    uvicorn.run(
            "src.main:app",
                host = settings.run.host,
                port = settings.run.port,
                reload=True)

