import pytest
from fastapi.testclient import TestClient
from app.main import app, database

# client = TestClient(app)

def reset_database():
    """Reset the in-memory database before each test. Helper function."""
    database._customers = {}
    database._orders = {}
    database._products = {}
    database._users = {}

    database._order_pk = 1
    database._product_pk = 1
    database._customer_pk = 1
    database._user_pk = 1

@pytest.fixture
def app_client():
    """Fixture to provide a TestClient for the FastAPI app."""

    reset_database()
    client = TestClient(app)
    return client


def test_create_customer(app_client):
    response = app_client.post("/customers", json={"user_id": 1})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["user_id"] == 1


def test_create_order(app_client):
    # Create a customer first
    app_client.post("/customers", json={"user_id": 1})
    response = app_client.post("/orders", json={"customer_id": 1})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["customer_id"] == 1
    assert data["state"] == "CREATED"


def test_create_product(app_client):
    # Create a customer and an order first
    app_client.post("/customers", json={"user_id": 1})
    app_client.post("/orders", json={"customer_id": 1})
    response = app_client.post("/products", json={"order_id": 1, "product_name": "bolt"})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["order_id"] == 1
    assert data["product_name"] == "bolt"
    assert data["state"] == "ORDERED"


def test_list_orders(app_client):
    # Create a customer and multiple orders
    app_client.post("/customers", json={"user_id": 1})
    app_client.post("/orders", json={"customer_id": 1})
    app_client.post("/orders", json={"customer_id": 1})
    response = app_client.get("/orders")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_list_products(app_client):
    # Create a customer, an order, and multiple products
    app_client.post("/customers", json={"user_id": 1})
    app_client.post("/orders", json={"customer_id": 1})
    app_client.post("/products", json={"order_id": 1, "product_name": "bolt"})
    app_client.post("/products", json={"order_id": 1, "product_name": "nut"})
    response = app_client.get("/products")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
