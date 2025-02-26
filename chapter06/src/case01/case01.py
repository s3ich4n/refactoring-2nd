
from dataclasses import dataclass
from datetime import (
    datetime,
    timedelta,
)

import arrow

from src.my_clock import kst_now


@dataclass
class Order:
    amount: int


@dataclass
class Invoice:
    customer: str
    orders: list[Order]
    due_date: datetime | None


def print_owing(invoice):
    print_banner()

    outstanding = calculate_outstanding(invoice)

    recore_due_date(invoice)
    method_name(invoice, outstanding)


def calculate_outstanding(invoice):
    result = 0
    for order in invoice.orders:
        result += order.amount
    return result


def recore_due_date(invoice):
    today = kst_now()
    invoice.due_date = today + timedelta(days=30)


def method_name(invoice, outstanding):
    print(f"고객명: {invoice.customer}")
    print(f"채무액: {outstanding}")
    print(f"마감일: {arrow.get(invoice.due_date).format('YYYY-MM-DD HH:mm:ss ZZ', locale='ko')}")


def print_banner():
    print("==============")
    print("== 고객채무 ==")
    print("==============")
