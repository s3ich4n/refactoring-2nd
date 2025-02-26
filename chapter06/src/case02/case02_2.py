from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    location: str


def report_lines(a_customer: Customer):
    lines = []
    gather_customer_data(lines, a_customer)
    return lines


def gather_customer_data(out, a_customer):
    out.append(["name", a_customer.name])
    out.append(["location", a_customer.location])
