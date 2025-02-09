from fastapi import FastAPI, HTTPException

from app.database import Database, ProductMissingError
from app.models import UserDto, OrderDto, ItemDto, CreateOrderDto, CreateItemDto, ItemState, OrderState
app = FastAPI()


database = Database()
database.add_user(UserDto(name="Alice"))
database.add_user(UserDto(name="Bob"))

database.add_order(CreateOrderDto(user_id=1))

database.add_item(CreateItemDto(order_id=1, product_name="bolt"))
database.add_item(CreateItemDto(order_id=1, product_name="nut"))
database.add_item(CreateItemDto(order_id=1, product_name="gear"))


# Endpoints for Orders
@app.post("/orders", response_model=OrderDto, status_code=201)
def create_order(create_order_dto: CreateOrderDto):
    try:
        database.get_user(create_order_dto.user_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found")

    order = database.add_order(create_order_dto)
    return order

@app.get("/orders", response_model=list[OrderDto], status_code=200)
def list_orders():
    return database.get_orders()

@app.get("/orders/{order_id}", response_model=OrderDto, status_code=200)
def get_order(order_id: int):
    try:
        order = database.get_order(order_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.put("/orders/{order_id}", response_model=OrderDto)
def update_order_state(order_id: int, state: OrderState):
    try:
        order = database.get_order(order_id)
        order.state = state
    except KeyError:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


# Endpoints for Items
@app.post("/items", response_model=ItemDto, status_code=201)
def create_item(create_item_dto: CreateItemDto):
    try:
        database.get_order(create_item_dto.order_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Order not found")

    try:
        item = database.add_item(create_item_dto)
    except ProductMissingError:
        raise HTTPException(status_code=404, detail="Product not found")

    return item

@app.get("/items", response_model=list[ItemDto], status_code=200)
def list_items():
    return database.get_items()

@app.get("/orders/{order_id}/items", response_model=list[ItemDto])
def get_items_by_order_id(order_id: int):
    items = [item for item in database.get_items() if item.order_id == order_id]
    return items

@app.put("/items/{item_id}", response_model=ItemDto)
def update_item_state(item_id: int, state: ItemState):
    try:
        item = database.get_item(item_id)
        item.state = state
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
