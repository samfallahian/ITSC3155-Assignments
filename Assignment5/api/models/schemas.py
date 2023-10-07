from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SandwichBase(BaseModel):
    sandwich_name: str
    price: float


class SandwichCreate(SandwichBase):
    pass


class SandwichUpdate(SandwichBase):
    pass


class Sandwich(SandwichBase):
    id: int

    class Config:
        from_attributes = True


class ResourceBase(BaseModel):
    item: str
    amount: int


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(ResourceBase):
    pass


class Resource(ResourceBase):
    id: int

    class Config:
        from_attributes = True


class RecipeBase(BaseModel):
    amount: int


class RecipeCreate(RecipeBase):
    sandwich_id: int
    resource_id: int


class Recipe(RecipeBase):
    id: int
    sandwich: Sandwich = None
    resource: Resource = None

    class Config:
        from_attributes = True


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    sandwich_id: int


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    sandwiches: list[Sandwich] = None

    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    # order_date: Optional[datetime] = None
    order_date: datetime | None = None
    order_details: list[OrderDetail] = None

    class Config:
        from_attributes = True
