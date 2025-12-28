from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from src.core.config import settings
from src.api.routes import products
from src.db.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    print("dispose_engine")
    await db_helper.dispose()

app = FastAPI(
    lifespan=lifespan
)

app.include_router(
    products.router,
    prefix=settings.api.prefix
    )

if __name__ == "__main__":
    uvicorn.run(
            "src.main:app",
                host = settings.run.host,
                port = settings.run.port,
                reload=True)

