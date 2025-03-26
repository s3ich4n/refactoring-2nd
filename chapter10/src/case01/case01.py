from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Plan:
    summer_start: date
    summer_end: date
    summer_rate: float
    regular_rate: float
    regular_service_charge: float


def is_before(date1: date, date2: date) -> bool:
    return date1 < date2


def is_after(date1: date, date2: date) -> bool:
    return date1 > date2


def calculate_charge(a_date: date, quantity: float, plan: Plan) -> float:
    if not is_before(a_date, plan.summer_start) and not is_after(
        a_date, plan.summer_end
    ):
        return quantity * plan.summer_rate
    else:
        return quantity * plan.regular_rate + plan.regular_service_charge
