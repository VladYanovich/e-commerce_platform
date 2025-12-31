from fastapi import APIRouter, Depends

from src.db.db_helper import db_helper
from src.db.crud import get_all_products, add_product
from src.db.schemas.products import ProductRead, ProductCreate
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    tags=["products"]
)

@router.get("/", response_model=list[ProductRead])
async def get_products(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    users = await get_all_products(session=session)
    return users

@router.post("/", response_model=ProductRead)
async def create_product(
        product_create: ProductCreate,
        session: AsyncSession = Depends(db_helper.session_getter)
):
    product = await add_product(session=session, product_create=product_create)
    return product
