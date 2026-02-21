from fastapi import APIRouter, Depends

from src.db.db_helper import db_helper
from src.db.crud import get_all_products, add_product, get_product
from src.db.schemas.products import ProductRead, ProductCreate
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    tags=["products"]
)

@router.get("/", response_model=list[ProductRead])
async def get_products(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    products = await get_all_products(session=session)
    return products

@router.post("/", response_model=ProductRead)
async def create_product(
        product_create: ProductCreate,
        session: AsyncSession = Depends(db_helper.session_getter)
):
    product = await add_product(session=session, product_create=product_create)
    return product

@router.get("/{id}", response_model=ProductRead)
async def get_one_product(
        id: int,
        session: AsyncSession = Depends(db_helper.session_getter)
):
    product = await get_product(session=session, id=id)
    return product