from dataclasses import dataclass


@dataclass(frozen=True)
class Reading:
    customer: str
    quantity: int
    month: int
    year: int


reading = Reading(**{"customer": "ivan", "quantity": 10, "month": 5, "year": 2017})

# client 1
a_reading = acquire_reading()
base_charge = base_rate(a_reading.month, a_reading.year) * a_reading.quantity

# client 2
a_reading = acquire_reading()
base_charge = base_rate(a_reading.month, a_reading.year) * a_reading.quantity
taxable_charge = max(0, base - tax_threshold(a_reading.year))

# client 3
a_reading = acquire_reading()
basic_charge_amount = calculate_base_charge(a_reading)


def calculate_base_charge(a_reading):
    return base_rate(a_reading.month, a_reading.year) * a_reading.quantity
