from pydantic import BaseModel
from enum import Enum


class ItemState(str, Enum):
    ORDERED = "ORDERED"
    READY = "READY"


class OrderState(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class CreateItemDto(BaseModel):
    order_id: int = 1
    product_name: str
    state: ItemState = ItemState.ORDERED


class ItemDto(CreateItemDto):
    id: int
    complexity: int


class CreateOrderDto(BaseModel):
    user_id: int = 1
    state: OrderState = OrderState.PENDING


class OrderDto(CreateOrderDto):
    id: int


class UserDto(BaseModel):
    id: int = None
    name: str
