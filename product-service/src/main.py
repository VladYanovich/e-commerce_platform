import uvicorn
from fastapi import FastAPI
from src.core.config import settings
from src.api.routes import products

app = FastAPI()
app.include_router(
    products.router,
    prefix=settings.api.prefix
    )

if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)

