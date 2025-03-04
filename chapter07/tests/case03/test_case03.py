# test_order.py
from src.case03.case03 import (
    count_high_priority_orders,
    Priority,
    Order,
)


def test_order_creation():
    # 기본 주문 생성 테스트
    data = {"priority": "high", "product": "Widget", "quantity": 5, "buyer": "John Doe"}
    order = Order(data)
    assert order.priority == Priority("high")
    assert order._product == "Widget"
    assert order._quantity == 5
    assert order._buyer == "John Doe"


def test_order_with_missing_data():
    # 누락된 데이터가 있는 경우 테스트
    data = {"product": "Widget"}
    order = Order(data)
    assert order.priority == Priority("normal")  # 기본값 확인
    assert order._quantity == 0  # 기본값 확인
    assert order._product == "Widget"
    assert order._buyer is None


def test_high_priority_orders_count():
    # 고우선순위 주문 카운팅 테스트
    orders = [
        Order({"priority": "high", "product": "A"}),
        Order({"priority": "rush", "product": "B"}),
        Order({"priority": "normal", "product": "C"}),
        Order({"priority": "low", "product": "D"}),
        Order({"priority": "high", "product": "E"}),
    ]

    assert count_high_priority_orders(orders) == 3


def test_empty_orders_list():
    # 빈 주문 리스트 테스트
    assert count_high_priority_orders([]) == 0


def test_no_high_priority_orders():
    # 고우선순위 주문이 없는 경우 테스트
    orders = [
        Order({"priority": "normal", "product": "A"}),
        Order({"priority": "low", "product": "B"}),
    ]
    assert count_high_priority_orders(orders) == 0


# 나중의 리팩토링을 위한 Priority 클래스 테스트
def test_priority_comparison():
    # 향후 Priority 클래스로 리팩토링할 때 사용할 테스트
    data1 = {"priority": "high"}
    data2 = {"priority": "normal"}
    order1 = Order(data1)
    order2 = Order(data2)
    # Priority 클래스 리팩토링 후 아래 테스트 활성화
    assert order1.priority.higher_than(order2.priority)
