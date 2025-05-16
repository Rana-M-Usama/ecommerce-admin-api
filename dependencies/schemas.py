from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict
from decimal import Decimal

class ProductBase(BaseModel):
    name: str
    category: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    product_id: int
    quantity: int
    sale_date: datetime
    total_amount: float

class Sale(SaleBase):
    id: int
    class Config:
        orm_mode = True

class InventoryBase(BaseModel):
    product_id: int
    quantity: int

class InventoryUpdate(BaseModel):
    quantity: int = Field(..., ge=0, description="Quantity must be greater than or equal to 0")

class Inventory(InventoryBase):
    id: int
    last_updated: datetime
    class Config:
        orm_mode = True

class RevenueReport(BaseModel):
    periods: List[Dict[str, float]]