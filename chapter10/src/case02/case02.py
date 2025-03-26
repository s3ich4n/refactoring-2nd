from dataclasses import dataclass


@dataclass
class Employee:
    seniority: int  # 근속연수
    months_disabled: int  # 장애 개월 수
    is_part_time: bool  # 파트타임 여부


def disability_payout_eligibility(an_employee: Employee) -> int:
    if an_employee.seniority < 2 or an_employee.months_disabled > 12:
        return 0
    if an_employee.is_part_time:
        return 0
    return 1  # 조건을 모두 통과하면 지급 대상
