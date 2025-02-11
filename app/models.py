from pydantic import BaseModel
from enum import Enum


class ProductState(str, Enum):
    ORDERED = "ORDERED"
    READY = "READY"


class OrderState(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class CreateProductDto(BaseModel):
    order_id: int = 1
    product_name: str
    state: ProductState = ProductState.ORDERED
    complexity: int


class ProductDto(CreateProductDto):
    id: int


class CreateOrderDto(BaseModel):
    customer_id: int = 1
    state: OrderState = OrderState.PENDING


class OrderDto(CreateOrderDto):
    id: int


class CustomerDto(BaseModel):
    id: int = None
    name: str
