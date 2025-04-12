from datetime import (
    datetime,
    timedelta,
)

import pytest

from chapter11.src.case03.case03_2 import (
    Order,
    rush_delivery_date,
    regular_delivery_date,
)


@pytest.fixture
def base_date():
    """테스트용 기준 날짜"""
    return datetime(2023, 1, 1)


@pytest.mark.parametrize(
    "state, is_rush, expected_days",
    [
        # MA, CT 케이스
        ("MA", True, 2),  # MA + 빠른 배송 = 1일 처리 + 2일 배송 - 1일(빠른 배송) = 2일
        ("CT", True, 2),  # CT + 빠른 배송 = 1일 처리 + 2일 배송 - 1일(빠른 배송) = 2일
        # NY, NH 케이스
        ("NY", True, 3),  # NY + 빠른 배송 = 2일 처리 + 2일 배송 - 1일(빠른 배송) = 3일
        ("NH", True, 3),  # NH + 빠른 배송 = 2일 처리 + 2일 배송 - 1일(빠른 배송) = 3일
        # ME와 기타 케이스
        ("ME", True, 4),  # ME + 빠른 배송 = 3일 처리 + 2일 배송 - 1일(빠른 배송) = 4일
        ("CA", True, 4),  # CA + 빠른 배송 = 3일 처리 + 2일 배송 - 1일(빠른 배송) = 4일
    ],
)
def test_rush_delivery_date(base_date, state, is_rush, expected_days):
    """다양한 주(State)와 빠른 배송 여부에 따른 배송일 계산 테스트"""
    # Given
    order = Order(state, base_date)

    # When
    result = rush_delivery_date(order)

    # Then
    expected_date = base_date + timedelta(days=expected_days)
    assert result == expected_date, f"Expected {expected_date}, got {result}"


@pytest.mark.parametrize(
    "state, is_rush, expected_days",
    [
        # MA, CT 케이스
        ("MA", False, 4),  # MA + 일반 배송 = 2일 처리 + 2일 배송 = 4일
        ("CT", False, 4),  # CT + 일반 배송 = 2일 처리 + 2일 배송 = 4일
        # NY, NH 케이스
        ("NY", False, 4),  # NY + 일반 배송 = 2일 처리 + 2일 배송 = 4일
        ("NH", False, 5),  # NH + 일반 배송 = 3일 처리 + 2일 배송 = 5일
        # ME와 기타 케이스
        ("ME", False, 5),  # ME + 일반 배송 = 3일 처리 + 2일 배송 = 5일
        ("CA", False, 6),  # CA + 일반 배송 = 4일 처리 + 2일 배송 = 6일
    ],
)
def test_regular_delivery_date(base_date, state, is_rush, expected_days):
    """다양한 주(State)와 일반 배송 여부에 따른 배송일 계산 테스트"""
    # Given
    order = Order(state, base_date)

    # When
    result = regular_delivery_date(order)

    # Then
    expected_date = base_date + timedelta(days=expected_days)
    assert result == expected_date, f"Expected {expected_date}, got {result}"


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
    order = Order("", base_date)

    # When/Then
    # 빈 문자열은 어떤 조건에도 포함되지 않으므로 'else' 케이스에 해당
    # 일반 배송: 4일 처리 + 2일 배송 = 6일
    result = regular_delivery_date(order)
    assert result == base_date + timedelta(days=6)

    # 빠른 배송: 3일 처리 + 2일 배송 - 1일(빠른 배송) = 4일
    result = rush_delivery_date(order)
    assert result == base_date + timedelta(days=4)
