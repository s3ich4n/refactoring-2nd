
from dataclasses import dataclass
from datetime import (
    datetime,
    timedelta,
)

import arrow

from chapter06.src.my_clock import kst_now


@dataclass
class Order:
    amount: int


@dataclass
class Invoice:
    customer: str
    orders: list[Order]
    due_date: datetime | None


def print_owing(invoice):
    outstanding = 0

    print("==============")
    print("== 고객채무 ==")
    print("==============")

    for order in invoice.orders:
        outstanding += order.amount

    today = kst_now()
    invoice.due_date = today + timedelta(days=30)

    print(f"고객명: {invoice.customer}")
    print(f"채무액: {outstanding}")
    print(f"마감일: {arrow.get(invoice.due_date).format('YYYY-MM-DD HH:mm:ss ZZ', locale='ko')}")
