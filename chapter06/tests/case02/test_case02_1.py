import pytest

from src.case02.case02_1 import (
    Driver,
    rating,
)


@pytest.fixture
def a_driver():
    return Driver(number_of_late_deliveries=6)


@pytest.mark.parametrize(
    "a_driver,expected",
    [
        (Driver(number_of_late_deliveries=6), 2),
        (Driver(number_of_late_deliveries=5), 1),
    ]
)
def test_case02_1(a_driver, expected):
    assert rating(a_driver) == expected
