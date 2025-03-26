from dataclasses import dataclass


@dataclass
class Employee:
    is_separated: bool = False
    is_retired: bool = False
    base_salary: int = 0

    def calculate_working_days(self):
        return 20  # 기본값

    def get_overtime_hours(self):
        return 10  # 기본값


def pay_amount(employee: Employee):
    if employee.is_separated:
        return {"amount": 0, "reason_code": "SEP"}
    if employee.is_retired:
        return {"amount": 0, "reason_code": "RET"}
    else:
        # 급여 계산 로직
        base_salary = employee.base_salary
        working_days = employee.calculate_working_days()
        overtime_hours = employee.get_overtime_hours()

        # 기본급 계산
        gross_pay = base_salary * (working_days / 20)

        # 초과근무 수당 계산
        overtime_pay = overtime_hours * (base_salary / 160) * 1.5

        # 세금 및 공제액 계산
        tax_rate = 0.15 if gross_pay <= 3000000 else 0.25
        tax_amount = (gross_pay + overtime_pay) * tax_rate

        # 최종 급여 계산
        net_pay = gross_pay + overtime_pay - tax_amount

        result = {"amount": net_pay, "reason_code": "REG"}

    return result
