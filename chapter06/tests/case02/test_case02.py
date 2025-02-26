import pytest

from src.case02.case02 import (
    Driver,
    rating,
)


@pytest.fixture
def a_driver():
    return Driver(number_of_late_deliveries=6)


def test_case02(a_driver):
    assert rating(a_driver) == 2
