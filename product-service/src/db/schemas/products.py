from pydantic import BaseModel
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    currency: str
    created_at: datetime
    updated_at: datetime

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int
