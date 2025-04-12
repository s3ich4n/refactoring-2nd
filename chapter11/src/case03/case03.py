from datetime import datetime, timedelta


def rush_delivery_date(order):
    if order.delivery_state in ["MA", "CT", "NY"]:
        delivery_time = 1
    elif order.delivery_state in ["NH"]:
        delivery_time = 2
    else:
        delivery_time = 3
    return order.placed_on + timedelta(days=1 + delivery_time)


def regular_delivery_date(order):
    if order.delivery_state in ["MA", "CT", "NY"]:
        delivery_time = 2
    elif order.delivery_state in ["ME", "NH"]:
        delivery_time = 3
    else:
        delivery_time = 4
    return order.placed_on + timedelta(days=2 + delivery_time)


class Order:
    """주문 정보를 담는 클래스"""

    def __init__(self, delivery_state, placed_on):
        """
        Args:
            delivery_state (str): 배송 주(State) 코드
            placed_on (datetime): 주문 날짜
        """
        self.delivery_state = delivery_state
        self.placed_on = placed_on
