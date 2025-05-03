from dataclasses import dataclass


@dataclass
class Person:
    age: int
    salary: int


# 변환된 파이썬 코드
def calculate_stats(people):
    youngest = people[0].age if people else float("inf")
    total_salary = 0
    for p in people:
        if p.age < youngest:
            youngest = p.age
        total_salary += p.salary

    return f"youngestAge: {youngest}, totalSalary: {total_salary}"
