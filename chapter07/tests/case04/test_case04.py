from src.case04.case04 import (
    Order,
    Item,
)


def test_order_price_with_small_order():
    """소액 주문(1000원 이하)에 대한 가격 계산 테스트"""
    # 테스트 준비: 1000원 이하의 주문 (예: 10개 * 90원 = 900원)
    item = Item(90)
    order = Order(10, item)

    # 예상 결과: 900 * 0.98 = 882
    expected_price = 900 * 0.98

    # 검증
    assert order.price == expected_price
    assert (
        abs(order.price - expected_price) < 0.0001
    )  # 부동소수점 비교를 위한 오차 허용


def test_order_price_with_large_order():
    """대액 주문(1000원 초과)에 대한 가격 계산 테스트"""
    # 테스트 준비: 1000원 초과의 주문 (예: 20개 * 60원 = 1200원)
    item = Item(60)
    order = Order(20, item)

    # 예상 결과: 1200 * 0.95 = 1140
    expected_price = 1200 * 0.95

    # 검증
    assert order.price == expected_price
    assert (
        abs(order.price - expected_price) < 0.0001
    )  # 부동소수점 비교를 위한 오차 허용


def test_order_with_exact_threshold():
    """정확히 경계값(1000원)에 대한 가격 계산 테스트"""
    # 테스트 준비: 정확히 1000원의 주문
    item = Item(100)
    order = Order(10, item)

    # 예상 결과: 1000 * 0.98 = 980 (1000원은 초과가 아니므로 0.98 적용)
    expected_price = 1000 * 0.98

    # 검증
    assert order.price == expected_price


def test_order_with_zero_quantity():
    """수량이 0인 경우 테스트"""
    item = Item(100)
    order = Order(0, item)

    # 예상 결과: 0 * 0.98 = 0
    expected_price = 0

    # 검증
    assert order.price == expected_price


def test_order_with_zero_price():
    """아이템 가격이 0인 경우 테스트"""
    item = Item(0)
    order = Order(10, item)

    # 예상 결과: 0 * 0.98 = 0
    expected_price = 0

    # 검증
    assert order.price == expected_price
