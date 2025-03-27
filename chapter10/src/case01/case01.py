from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Plan:
    summer_start: date
    summer_end: date
    summer_rate: float
    regular_rate: float
    regular_service_charge: float


def is_summer(a_date: date, plan: Plan) -> bool:
    return plan.summer_start <= a_date <= plan.summer_end


def calculate_summer_charge(quantity: float, plan: Plan) -> float:
    return quantity * plan.summer_rate


def calculate_regular_charge(quantity: float, plan: Plan) -> float:
    return quantity * plan.regular_rate + plan.regular_service_charge


def calculate_charge(a_date: date, quantity: float, plan: Plan) -> float:
    if is_summer(a_date, plan):
        return calculate_summer_charge(quantity, plan)
    else:
        return calculate_regular_charge(quantity, plan)
