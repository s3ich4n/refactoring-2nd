from chapter09.src.case05.case05 import (
    Order,
    Customer,
)


def test_order_and_customer():
    # 테스트 데이터 생성
    order_data = {"number": "12345", "customer": "C001"}

    # Order 객체 생성
    order = Order(order_data)

    # 테스트 검증
    assert order._number == "12345"
    assert order.customer.id == "C001"

    # Customer 객체가 올바르게 생성되었는지 확인
    assert isinstance(order.customer, Customer)
    assert order.customer._id == "C001"
