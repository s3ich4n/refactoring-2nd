from dataclasses import dataclass


@dataclass
class Person:
    age: int
    salary: int


# 변환된 파이썬 코드
def calculate_stats(people):
    return f"youngestAge: {youngest_age(people)}, totalSalary: {total_salary(people)}"


def youngest_age(people):
    youngest = people[0].age if people else float("inf")
    for p in people:
        if p.age < youngest:
            youngest = p.age
    return youngest


def total_salary(people):
    total_salary = 0
    for p in people:
        total_salary += p.salary
    return total_salary
