from datetime import date

from chapter10.src.case01.case01 import (
    Plan,
    calculate_charge,
)


def test_summer_rate():
    my_plan = Plan(
        summer_start=date(2025, 6, 1),
        summer_end=date(2025, 8, 31),
        summer_rate=0.8,
        regular_rate=1.0,
        regular_service_charge=20.0,
    )
    a_date = date(2025, 7, 15)
    quantity = 100.0

    charge = calculate_charge(a_date, quantity, my_plan)

    assert charge == 80
