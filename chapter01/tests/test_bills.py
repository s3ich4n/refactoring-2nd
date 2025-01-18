import json
from textwrap import dedent

import pytest

from chapter01.bills import statement


@pytest.fixture
def invoices():
    with open("invoices.json") as f:
        yield json.load(f)


@pytest.fixture
def plays():
    with open("plays.json") as f:
        yield json.load(f)


def test_bills(invoices, plays):
    result = dedent(
        """
            청구 내역 (고객명: BigCo)
             Hamlet: $650.00 55석
             As You Like It: $580.00 35석
             Othello: $500.00 40석
            총액: $1,730.00
            적립 포인트: 47점
            """
    ).strip()  # used strip() to remove blank

    # I focused on _the result_ of method. not an format.
    assert statement(invoices, plays).strip() == result
