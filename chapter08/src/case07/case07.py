from dataclasses import dataclass


@dataclass
class Person:
    age: int
    salary: int


# 변환된 파이썬 코드
def calculate_stats(people):
    total_salary = 0

    for p in people:
        total_salary += p.salary

    youngest = people[0].age if people else float("inf")
    for p in people:
        if p.age < youngest:
            youngest = p.age

    return f"youngestAge: {youngest}, totalSalary: {total_salary}"
