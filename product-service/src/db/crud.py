from typing import Sequence
from src.db.models import Product
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.db.schemas.products import ProductCreate


async def get_all_products(
        session: AsyncSession
) -> Sequence[Product]:
    stmt = select(Product).order_by(Product.id)
    result = await session.scalars(stmt)
    return result.all()

async def add_product(
        session: AsyncSession,
        product_create: ProductCreate
) -> Product:
    product = Product(**product_create.model_dump())
    session.add(product)
    await session.commit()
    return product

async def get_product(
        session: AsyncSession,
        id: int
) -> Product | None:
    stmt = select(Product).filter(Product.id == id)
    result = await session.scalars(stmt)
    return result.first()

async def update_product(
        session: AsyncSession,
        id: int,
        updated_product: ProductCreate
) -> Product | None:
    product = await session.get(Product, id)
    if product is None:
        return None
    for key, value in updated_product.model_dump().items():
        setattr(product, key, value)
    await session.commit()
    await session.refresh(product)
    return product

async def delete_product(
        session: AsyncSession,
        id: int
) -> Product | None:
    product = await session.get(Product, id)
    if product is None:
        return None
    await session.delete(product)
    await session.commit()
    return product


