from fastapi import FastAPI, HTTPException

from app.database import Database
from app.models import CreateUserDto, UserDto, CustomerDto, CreateCustomerDto, OrderDto, ProductDto, CreateOrderDto, CreateProductDto, ProductState, OrderState
app = FastAPI()


database = Database()

database.add_user(CreateUserDto(username="Alice"))
database.add_user(CreateUserDto(username="Bob"))

database.add_customer(CreateCustomerDto(user_id=1))
database.add_customer(CreateCustomerDto(user_id=2))

database.add_order(CreateOrderDto(customer_id=1))

database.add_product(CreateProductDto(order_id=1, product_name="bolt", complexity=1))
database.add_product(CreateProductDto(order_id=1, product_name="nut", complexity=2))
database.add_product(CreateProductDto(order_id=1, product_name="gear", complexity=3))

# Endpoints for Customers
@app.post("/customers", response_model=CustomerDto, status_code=201)
def create_customer(create_customer_dto: CreateCustomerDto):
    customer = database.add_customer(create_customer_dto)
    return customer

@app.get("/customers", response_model=CustomerDto, status_code=200)
def get_customer():
    return database.get_orders()

# Endpoints for Orders
@app.post("/orders", response_model=OrderDto, status_code=201)
def create_order(create_order_dto: CreateOrderDto):
    try:
        database.get_customer(create_order_dto.customer_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Customer not found")

    order = database.add_order(create_order_dto)
    return order

@app.get("/orders", response_model=list[OrderDto], status_code=200)
def list_orders():
    return database.get_customers()

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


# Endpoints for Products
@app.post("/products", response_model=ProductDto, status_code=201)
def create_product(create_product_dto: CreateProductDto):
    try:
        database.get_order(create_product_dto.order_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Order not found")

    product = database.add_product(create_product_dto)

    return product

@app.get("/products", response_model=list[ProductDto], status_code=200)
def list_products():
    return database.get_products()

@app.get("/orders/{order_id}/products", response_model=list[ProductDto])
def get_products_by_order_id(order_id: int):
    products = [product for product in database.get_products() if product.order_id == order_id]
    return products

@app.put("/products/{product_id}", response_model=ProductDto)
def update_product_state(product_id: int, state: ProductState):
    try:
        product = database.get_product(product_id)
        product.state = state
    except KeyError:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
