from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    quantity: int
    item_price: int


def price(order):
    """가격(price) = 기본 가격 - 수량 할인 + 배송비

    :param order:
    :return:
    """
    base_price = order.quantity * order.item_price
    quantity_discount = max(0, order.quantity - 500) * order.item_price * 0.05
    shipping = min(order.quantity * order.item_price * 0.1, 100)

    return base_price - quantity_discount + shipping
