from datetime import date

import pytest

from chapter10.src.case01.case01 import (
    Plan,
    calculate_charge,
)


@pytest.fixture
def test_plan():
    return Plan(
        summer_start=date(2025, 6, 1),
        summer_end=date(2025, 8, 31),
        summer_rate=0.8,
        regular_rate=1.0,
        regular_service_charge=20.0,
    )


@pytest.mark.parametrize(
    "a_date, quantity, expected_charge",
    [
        (date(2025, 6, 1), 100.0, 80.0),  # summer_start (inclusive)
        (date(2025, 8, 31), 100.0, 80.0),  # summer_end (inclusive)
        (date(2025, 7, 15), 50.0, 40.0),  # summer mid
        (date(2025, 5, 31), 100.0, 120.0),  # before summer
        (date(2025, 9, 1), 100.0, 120.0),  # after summer
    ],
)
def test_calculate_charge(
    a_date,
    quantity,
    expected_charge,
    test_plan,
):
    assert calculate_charge(a_date, quantity, test_plan) == expected_charge
