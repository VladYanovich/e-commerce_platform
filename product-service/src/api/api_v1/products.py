from fastapi import APIRouter, Depends

from src.db.db_helper import db_helper
from src.db.crud import get_all_products, add_product, get_product, update_product, delete_product
from src.db.schemas.products import ProductRead, ProductCreate
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

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

@router.put('/{id}', response_model=ProductRead)
async def update_one_product(
        id: int,
        updated_product: ProductCreate,
        session: AsyncSession = Depends(db_helper.session_getter)
):
    product = await update_product(session=session, id=id, updated_product=updated_product)
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with id: {id} was not found")
    return product

@router.delete('/{id}', response_model=ProductRead)
async def delete_one_product(
        id: int,
        session: AsyncSession = Depends(db_helper.session_getter)
):
    product = await delete_product(session=session, id=id)
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with id: {id} was not found")
    return product