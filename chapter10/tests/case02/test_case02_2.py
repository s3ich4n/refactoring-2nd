import pytest

from chapter10.src.case02.case02_2 import (
    Employee,
    seniority_payout_eligibility,
)


def test_eligibility_pass():
    emp = Employee(seniority=11, on_vacation=True)
    assert seniority_payout_eligibility(emp) == 1


@pytest.mark.parametrize(
    "employee",
    [
        Employee(seniority=6, on_vacation=True),
        Employee(seniority=10, on_vacation=True),
        Employee(seniority=11, on_vacation=False),
    ],
)
def test_eligibility_fail(employee):
    assert seniority_payout_eligibility(employee) == 0.5
