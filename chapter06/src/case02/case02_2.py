from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    location: str


def report_lines(a_customer: Customer):
    lines = []

    lines.append(["name", a_customer.name]) # first step
    lines.append(["location", a_customer.location]) # second step and done. (also remove function)
    return lines
