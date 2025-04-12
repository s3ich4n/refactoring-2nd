from datetime import datetime, timedelta


def delivery_date(order, is_rush):
    """
    주문의 배송 날짜를 계산합니다.

    Args:
        order: 주문 정보가 담긴 객체 (delivery_state와 placed_on 속성 필요)
        is_rush: 빠른 배송 여부를 나타내는 불리언 값

    Returns:
        datetime: 배송 예상 날짜
    """
    if order.delivery_state == "MA" or order.delivery_state == "CT":
        delivery_time = 1 if is_rush else 2
    elif order.delivery_state == "NY" or order.delivery_state == "NH":
        delivery_time = 2
        if order.delivery_state == "NH" and not is_rush:
            delivery_time = 3
    elif is_rush:
        delivery_time = 3
    elif order.delivery_state == "ME":
        delivery_time = 3
    else:
        delivery_time = 4

    result = order.placed_on + timedelta(days=2 + delivery_time)
    if is_rush:
        result = result - timedelta(days=1)

    return result


def rush_delivery_date(order):
    return delivery_date(order, is_rush=True)


def regular_delivery_date(order):
    return delivery_date(order, is_rush=False)


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
