from dataclasses import dataclass


@dataclass
class Person:
    age: int
    salary: int


# 변환된 파이썬 코드
def calculate_stats(people):
    return f"youngestAge: {youngest_age(people)}, totalSalary: {total_salary(people)}"


def youngest_age(people):
    # Generator expression with min()
    return min((p.age for p in people), default=float("inf"))


def total_salary(people):
    # Generator expression with sum()
    return sum(p.salary for p in people)
