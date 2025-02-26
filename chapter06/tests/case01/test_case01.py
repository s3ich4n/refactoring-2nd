import pytest

from src.case01.case01 import (
    Invoice,
    Order,
    print_owing,
)


@pytest.fixture
def invoice():
    return Invoice(
        customer="s3ich4n",
        orders=[Order(amount=3), Order(amount=4), Order(amount=7)],
        due_date=None,
    )


def test_print_owing(invoice):
    print_owing(invoice)
