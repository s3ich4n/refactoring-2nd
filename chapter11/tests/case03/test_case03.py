from datetime import (
    datetime,
    timedelta,
)

import pytest

from chapter11.src.case03.case03 import (
    delivery_date,
    Order,
)


@pytest.fixture
def base_date():
    """테스트용 기준 날짜"""
    return datetime(2023, 1, 1)


@pytest.mark.parametrize(
    "state, is_rush, expected_days",
    [
        # 빠른 배송 테스트 케이스
        ("MA", True, 2),  # MA + 빠른 배송 = 1일 처리 + 1일 배송 = 2일
        ("CT", True, 2),  # CT + 빠른 배송 = 1일 처리 + 1일 배송 = 2일
        ("NY", True, 2),  # NY + 빠른 배송 = 1일 처리 + 1일 배송 = 2일
        ("NH", True, 3),  # NH + 빠른 배송 = 2일 처리 + 1일 배송 = 3일
        ("ME", True, 4),  # ME + 빠른 배송 = 3일 처리 + 1일 배송 = 4일
        ("CA", True, 4),  # CA + 빠른 배송 = 3일 처리 + 1일 배송 = 4일
        # 일반 배송 테스트 케이스
        ("MA", False, 4),  # MA + 일반 배송 = 2일 처리 + 2일 배송 = 4일
        ("CT", False, 4),  # CT + 일반 배송 = 2일 처리 + 2일 배송 = 4일
        ("NY", False, 4),  # NY + 일반 배송 = 2일 처리 + 2일 배송 = 4일
        ("ME", False, 5),  # ME + 일반 배송 = 3일 처리 + 2일 배송 = 5일
        ("NH", False, 5),  # NH + 일반 배송 = 3일 처리 + 2일 배송 = 5일
        ("CA", False, 6),  # CA + 일반 배송 = 4일 처리 + 2일 배송 = 6일
    ],
)
def test_delivery_date(base_date, state, is_rush, expected_days):
    """다양한 주(State)와 빠른 배송 여부에 따른 배송일 계산 테스트"""
    # Given
    order = Order(state, base_date)

    # When
    result = delivery_date(order, is_rush)

    # Then
    expected_date = base_date + timedelta(days=expected_days)
    assert result == expected_date


def test_order_creation():
    """Order 객체 생성 테스트"""
    # Given
    state = "NY"
    date = datetime(2023, 1, 1)

    # When
    order = Order(state, date)

    # Then
    assert order.delivery_state == state
    assert order.placed_on == date


# 엣지 케이스 테스트
def test_empty_state(base_date):
    """빈 주(State) 값 테스트"""
    # Given
    order = Order("", True)
    order.placed_on = base_date

    # When/Then
    # 빈 문자열은 어떤 조건에도 포함되지 않으므로 'else' 케이스에 해당
    result = delivery_date(order, True)
    assert result == base_date + timedelta(days=4)  # 3일 처리 + 1일 배송

    result = delivery_date(order, False)
    assert result == base_date + timedelta(days=6)  # 4일 처리 + 2일 배송
