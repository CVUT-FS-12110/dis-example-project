from app.models import UserDto, OrderDto, ProductDto, CreateOrderDto, CreateProductDto

# Mock Database
class Database:

    def __init__(self):
        self._users = {}
        self._orders = {}
        self._products = {}

        self._order_pk = 1
        self._product_pk = 1
        self._user_pk = 1

    def add_order(self, create_order: CreateOrderDto) -> OrderDto:
        order = OrderDto(id=self._order_pk, **create_order.model_dump())
        self._orders[self._order_pk] = order
        self._order_pk += 1
        return order

    def get_orders(self) -> list[OrderDto]:
        return list(self._orders.values())

    def get_order(self, order_id: int) -> OrderDto:
        return self._orders[order_id]

    def add_product(self, create_product: CreateProductDto) -> ProductDto:
        product = ProductDto(id=self._product_pk, **create_product.model_dump())
        self._products[self._product_pk] = product
        self._product_pk += 1
        return product

    def get_products(self) -> list[ProductDto]:
        return list(self._products.values())

    def get_product(self, product_id: int) -> ProductDto:
        return self._products[product_id]

    def add_user(self, user: UserDto) -> UserDto:
        user.id = self._user_pk
        self._users[self._user_pk] = user
        self._user_pk += 1
        return user

    def get_users(self) -> list[UserDto]:
        return list(self._users.values())

    def get_user(self, user_id: int) -> UserDto:
        return self._users[user_id]
