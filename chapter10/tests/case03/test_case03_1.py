import pytest

from chapter10.src.case03.case03_1 import (
    Employee,
    pay_amount,
)


def test_pay_amount_separated_employee():
    # 퇴사한 직원
    employee = Employee(is_separated=True)
    result = pay_amount(employee)

    assert result["amount"] == 0
    assert result["reason_code"] == "SEP"


def test_pay_amount_retired_employee():
    # 은퇴한 직원
    employee = Employee(is_retired=True)
    result = pay_amount(employee)

    assert result["amount"] == 0
    assert result["reason_code"] == "RET"


def test_pay_amount_regular_employee():
    # 일반 직원 (기본급 3,000,000원, 20일 근무, 10시간 초과근무)
    employee = Employee(base_salary=3000000)
    result = pay_amount(employee)

    # 계산 검증
    gross_pay = 3000000 * (20 / 20)  # 3,000,000원
    overtime_pay = 10 * (3000000 / 160) * 1.5  # 약 281,250원
    tax_amount = (gross_pay + overtime_pay) * 0.15  # 약 492,187.5원
    expected_net_pay = gross_pay + overtime_pay - tax_amount  # 약 2,789,062.5원

    assert result["amount"] == pytest.approx(expected_net_pay)
    assert result["reason_code"] == "REG"


def test_pay_amount_high_salary_employee():
    # 고액연봉 직원 (기본급 5,000,000원, 세금 25%)
    employee = Employee(base_salary=5000000)
    result = pay_amount(employee)

    # 계산 검증
    gross_pay = 5000000 * (20 / 20)  # 5,000,000원
    overtime_pay = 10 * (5000000 / 160) * 1.5  # 약 468,750원
    tax_amount = (gross_pay + overtime_pay) * 0.25  # 약 1,367,187.5원
    expected_net_pay = gross_pay + overtime_pay - tax_amount  # 약 4,101,562.5원

    assert result["amount"] == pytest.approx(expected_net_pay)
    assert result["reason_code"] == "REG"
