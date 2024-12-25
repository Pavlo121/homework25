from pydantic import BaseModel
from typing import List, Optional


class ProductIn(BaseModel):
    name: str
    description: str
    price: float
    stock: int

    class Config:
        from_attributes = True


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True

class OrderIn(BaseModel):
    customer_name: str
    items: List[dict]

class OrderOut(OrderIn):
    id: int
    status: str
