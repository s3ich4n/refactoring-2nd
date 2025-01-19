import json
from textwrap import dedent

import pytest
from bs4 import BeautifulSoup

from chapter01.statements import (
    statement,
    html_statement,
)


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


def test_html_bills(invoices, plays):
    expected_html = dedent(
        """
        <h1>청구 내역 (고객명: BigCo)</h1>
        <table>
        <tr><th>연극</th><th>좌석 수</th><th>금액</th></tr>
         <tr><td>Hamlet</td><td>55</td><td>$650.00</td></tr>
         <tr><td>As You Like It</td><td>35</td><td>$580.00</td></tr>
         <tr><td>Othello</td><td>40</td><td>$500.00</td></tr>
        </table>
        <p>총액: <em>$1,730.00</em></p>
        <p>적립 포인트: <em>47</em> credits</p>
        """
    ).strip()

    actual_soup = BeautifulSoup(html_statement(invoices, plays), "html.parser")
    expected_soup = BeautifulSoup(expected_html, "html.parser")

    # compares between their html structures and contents
    assert str(actual_soup).rstrip() == str(expected_soup).rstrip()
