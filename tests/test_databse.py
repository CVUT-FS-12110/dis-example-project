import pytest
from app.database import Database
from app.models import CreateCustomerDto, CreateOrderDto, CreateProductDto, ProductState, OrderState


@pytest.fixture
def db():
    return Database()


def test_add_customer(db):
    customer = db.add_customer(CreateCustomerDto(user_id=1))
    assert customer.id == 1
    assert customer.user_id == 1


def get_customer(db):
    customer = db.add_customer(CreateCustomerDto(user_id=1))
    assert customer.id == 1
    assert customer.user_id == 1

    retrieved_customer = db.get_customer(customer.id)
    assert retrieved_customer.id == customer.id


def test_add_and_get_order(db):
    db.add_customer(CreateCustomerDto(user_id=1))  # Add a customer first
    order = db.add_order(CreateOrderDto(customer_id=1))
    assert order.id == 1
    assert order.customer_id == 1
    assert order.state == OrderState.CREATED

    retrieved_order = db.get_order(order.id)
    assert retrieved_order.id == order.id


def test_add_and_get_product(db):
    db.add_customer(CreateCustomerDto(user_id=1))  # Add a customer first
    db.add_order(CreateOrderDto(customer_id=1))  # Add an order first
    product = db.add_product(CreateProductDto(order_id=1, product_name="bolt"))
    assert product.id == 1
    assert product.order_id == 1
    assert product.product_name == "bolt"
    assert product.state == ProductState.ORDERED

    retrieved_product = db.get_product(product.id)
    assert retrieved_product.id == product.id


def test_get_orders(db):
    db.add_customer(CreateCustomerDto(user_id=1))  # Add a customer first
    db.add_order(CreateOrderDto(customer_id=1))
    db.add_order(CreateOrderDto(customer_id=1))
    orders = db.get_orders()
    assert len(orders) == 2


def test_get_products(db):
    db.add_customer(CreateCustomerDto(user_id=1))  # Add a customer first
    db.add_order(CreateOrderDto(customer_id=1))  # Add an order first
    db.add_product(CreateProductDto(order_id=1, product_name="bolt"))
    db.add_product(CreateProductDto(order_id=1, product_name="nut"))
    products = db.get_products()
    assert len(products) == 2
