from dataclasses import dataclass


@dataclass
class Customer:
    name: int


class Book:
    """도서 관리 프로그램"""

    def __init__(self):
        self._reservations = []

    def add_reservation(self, customer):
        self._reservations.append(customer)
