from src.case03.case03 import (
    Order,
    price,
)


def test_price():
    assert price(Order(quantity=10, item_price=10)) == 110
