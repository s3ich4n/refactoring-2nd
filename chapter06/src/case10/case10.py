from dataclasses import dataclass


@dataclass(frozen=True)
class Reading:
    customer: str
    quantity: int
    month: int
    year: int


reading = Reading(**{"customer": "ivan", "quantity": 10, "month": 5, "year": 2017})
