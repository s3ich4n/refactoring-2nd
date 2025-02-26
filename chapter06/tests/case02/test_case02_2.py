import pytest

from src.case02.case02_2 import Customer, report_lines


@pytest.fixture
def a_customer():
    return Customer(name="s3ich4n", location="Seoul")


def test_case02_2(a_customer):
    assert report_lines(a_customer) == [
        ["name", "s3ich4n"],
        ["location", "Seoul"],
    ]