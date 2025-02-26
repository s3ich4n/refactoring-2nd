from dataclasses import dataclass


@dataclass
class Customer:
    name: int


class Book:
    """도서 관리 프로그램"""

    def __init__(self):
        self._reservations = []

    def add_reservation(self, customer):
        self.do_add_reservation(customer, False)

    def do_add_reservation(self, customer, is_priority):
        assert (
            is_priority is True or is_priority is False
        )  # 이러면 assertion으로 체크 가능
        self._reservations.append(customer)
