from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Integer)
    currency = Column(String(3))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"), onupdate=text("now()"))

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class ProductCategory(Base):
    __tablename__ = "product_categories"
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True, nullable=False)
