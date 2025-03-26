import pytest

from chapter10.src.case02.case02 import (
    Employee,
    disability_payout_eligibility,
)


def test_eligibility_pass():
    emp = Employee(seniority=3, months_disabled=6, is_part_time=False)
    assert disability_payout_eligibility(emp) == 1


@pytest.mark.parametrize(
    "employee",
    [
        Employee(seniority=1, months_disabled=6, is_part_time=False),  # 근속연수 부족
        Employee(seniority=3, months_disabled=13, is_part_time=False),  # 장애기간 초과
        Employee(seniority=3, months_disabled=6, is_part_time=True),  # 파트타임
    ],
)
def test_eligibility_fail(employee):
    assert disability_payout_eligibility(employee) == 0
