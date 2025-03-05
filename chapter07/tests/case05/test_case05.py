# tests/test_person.py

import pytest
from src.case05.case05 import Person


def test_person_initialization():
    """Person 클래스가 정상적으로 초기화되는지 테스트합니다."""
    office_area_code = "010"
    office_number = "1234-5678"
    person = Person(office_area_code, office_number)

    assert person.office_area_code == office_area_code
    assert person.office_number == office_number


@pytest.mark.parametrize(
    "area_code, number",
    [
        ("02", "9876-5432"),
        ("031", "111-2222"),
        ("010", "0000-0000"),
    ],
)
def test_person_multiple_cases(area_code, number):
    """다양한 케이스에 대한 Person 초기화 및 프로퍼티 검증."""
    person = Person(area_code, number)
    assert person.office_area_code == area_code
    assert person.office_number == number
