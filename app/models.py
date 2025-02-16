import time

from pydantic import BaseModel
from enum import Enum


class ProductState(str, Enum):
    ORDERED = "ORDERED"
    READY = "READY"


class OrderState(str, Enum):
    CREATED = "CREATED"
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class CreateProductDto(BaseModel):
    order_id: int = 1
    product_name: str
    state: ProductState = ProductState.ORDERED
    timestamp: float = time.time()

class ProductDto(CreateProductDto):
    id: int


class CreateOrderDto(BaseModel):
    customer_id: int = 1
    state: OrderState = OrderState.CREATED
    timestamp: float = time.time()

class OrderDto(CreateOrderDto):
    id: int


class CreateCustomerDto(BaseModel):
    user_id: int = 1

class CustomerDto(CreateCustomerDto):
    id: int = None


class CreateUserDto(BaseModel):
    username: str


class UserDto(CreateUserDto):
    id: int = None
