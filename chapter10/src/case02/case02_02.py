from dataclasses import dataclass


@dataclass
class Employee:
    seniority: int  # 근속연수
    on_vacation: bool  # 휴가여부


def seniority_payout_eligibility(an_employee: Employee) -> int | float:
    if is_eligible_for_seniority(an_employee):
        return 1
    return 0.5


def is_eligible_for_seniority(an_employee):
    return an_employee.on_vacation and an_employee.seniority > 10
