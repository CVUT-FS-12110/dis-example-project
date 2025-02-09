from app.models import UserDto, OrderDto, ItemDto, CreateOrderDto, CreateItemDto

# Mock Database
class Database:

    def __init__(self):
        self._users = {}
        self._orders = {}
        self._items = {}
        self._machining_products = {
            "bolt": 3,
            "nut": 2,
            "gear": 7,
            "shaft": 5,
            "bearing": 6,
            "sprocket": 8,
            "pulley": 4,
            "bracket": 5,
            "flange": 6,
            "coupling": 7
        }

        self._order_pk = 1
        self._item_pk = 1
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

    def add_item(self, create_item: CreateItemDto) -> ItemDto:
        product_complexity = self._get_product_complexity(create_item.product_name)
        item = ItemDto(id=self._item_pk, complexity=product_complexity, **create_item.model_dump())
        self._items[self._item_pk] = item
        self._item_pk += 1
        return item

    def get_items(self) -> list[ItemDto]:
        return list(self._items.values())

    def get_item(self, item_id: int) -> ItemDto:
        return self._items[item_id]

    def _get_product_complexity(self, product_name: str) -> int:
        try:
            return self._machining_products[product_name]
        except KeyError:
            raise ProductMissingError()

    def add_user(self, user: UserDto) -> UserDto:
        user.id = self._user_pk
        self._users[self._user_pk] = user
        self._user_pk += 1
        return user

    def get_users(self) -> list[UserDto]:
        return list(self._users.values())

    def get_user(self, user_id: int) -> UserDto:
        return self._users[user_id]


class ProductMissingError(Exception):
    pass
