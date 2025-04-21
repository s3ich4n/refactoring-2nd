from datetime import datetime

import pytest

from chapter12.src.case10.case10_1 import (
    Show,
    Extras,
    create_booking,
    create_premium_booking,
)


@pytest.fixture
def show_with_talkback():
    return Show(price=100, properties={"talkback": True})


@pytest.fixture
def show_without_talkback():
    return Show(price=100, properties={})


@pytest.fixture
def extras_with_dinner():
    return Extras(premium_fee=50, properties={"dinner": True})


@pytest.fixture
def weekday():
    return datetime(2023, 5, 10)  # 수요일


@pytest.fixture
def weekend():
    return datetime(2023, 5, 13)  # 토요일


# 일반 예약 테스트
def test_regular_booking_base_price(
    show_with_talkback,
    weekday,
    weekend,
):
    # 주중 예약
    weekday_booking = create_booking(show_with_talkback, weekday)
    assert weekday_booking.base_price() == 100

    # 주말(성수기) 예약
    weekend_booking = create_booking(show_with_talkback, weekend)
    assert weekend_booking.base_price() == 115  # 100 + 15% 할증


def test_regular_booking_has_talkback(
    show_with_talkback,
    show_without_talkback,
    weekday,
    weekend,
):
    # 주중 예약, 톡백 있음
    weekday_booking = create_booking(show_with_talkback, weekday)
    assert weekday_booking.has_talk_back() is True

    # 주중 예약, 톡백 없음
    weekday_booking_no_talkback = create_booking(show_without_talkback, weekday)
    assert weekday_booking_no_talkback.has_talk_back() is False

    # 주말(성수기) 예약, 톡백 있음 - 성수기에는 톡백이 없어야 함
    weekend_booking = create_booking(show_with_talkback, weekend)
    assert weekend_booking.has_talk_back() is False


def test_regular_booking_has_not_dinner(
    show_with_talkback,
    show_without_talkback,
    weekday,
    weekend,
):
    # 주중 예약, 톡백 있음 -> 에러 발생
    # 주말 예약, 톡백 있음 -> 에러 발생
    weekday_booking = create_booking(show_with_talkback, weekday)
    weekend_booking = create_booking(show_without_talkback, weekend)
    with pytest.raises(AttributeError):
        weekday_booking.has_dinner()

    with pytest.raises(AttributeError):
        weekend_booking.has_dinner()


# 프리미엄 예약 테스트
def test_premium_booking_base_price(
    show_with_talkback,
    weekday,
    weekend,
    extras_with_dinner,
):
    # 주중 프리미엄 예약
    weekday_premium = create_premium_booking(
        show_with_talkback,
        weekday,
        extras_with_dinner,
    )
    assert weekday_premium.base_price() == 150  # 100 + 50 프리미엄 요금

    # 주말(성수기) 프리미엄 예약
    weekend_premium = create_premium_booking(
        show_with_talkback,
        weekend,
        extras_with_dinner,
    )
    assert weekend_premium.base_price() == 165  # 115 + 50 프리미엄 요금


def test_premium_booking_has_talkback(
    show_with_talkback,
    show_without_talkback,
    weekday,
    weekend,
    extras_with_dinner,
):
    # 주중 프리미엄 예약, 톡백 있음
    weekday_premium = create_premium_booking(
        show_with_talkback,
        weekday,
        extras_with_dinner,
    )
    assert weekday_premium.has_talk_back() is True

    # 주말(성수기) 프리미엄 예약, 톡백 있음 - 프리미엄은 성수기와 관계없이 톡백 있음
    weekend_premium = create_premium_booking(
        show_with_talkback,
        weekend,
        extras_with_dinner,
    )
    assert weekend_premium.has_talk_back() is True

    # 주중 프리미엄 예약, 톡백 없음
    weekday_premium_no_talkback = create_premium_booking(
        show_without_talkback,
        weekday,
        extras_with_dinner,
    )
    assert weekday_premium_no_talkback.has_talk_back() is False


def test_premium_booking_has_dinner(
    show_with_talkback,
    weekday,
    weekend,
    extras_with_dinner,
):
    # 주중 프리미엄 예약, 저녁 있음
    weekday_premium = create_premium_booking(
        show_with_talkback,
        weekday,
        extras_with_dinner,
    )
    assert weekday_premium.has_dinner() is True

    # 주말(성수기) 프리미엄 예약, 저녁 있음 - 성수기에는 저녁이 없어야 함
    weekend_premium = create_premium_booking(
        show_with_talkback,
        weekend,
        extras_with_dinner,
    )
    assert weekend_premium.has_dinner() is False
