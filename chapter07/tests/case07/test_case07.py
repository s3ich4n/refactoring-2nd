# tests/test_organization.py
import pytest
from src.case07.case07 import (
    Person,
    Department,
)


def test_person_basic():
    """
    Person 객체를 생성하고, 기본 속성(name, department)이 제대로 동작하는지 테스트.
    """
    p = Person("Alice")
    assert p.name == "Alice"
    assert p.department is None  # 초기값 확인


def test_department_basic():
    """
    Department 객체를 생성하고, chargeCode와 manager 게터/세터가 잘 동작하는지 테스트.
    """
    d = Department()
    assert d.charge_code is None
    assert d.manager is None

    d.charge_code = "CODE123"
    d.manager = "Bob"

    assert d.charge_code == "CODE123"
    assert d.manager == "Bob"


def test_person_and_department():
    """
    Person에 Department를 연결했을 때 정상적으로 참조가 이뤄지는지 확인.
    """
    p = Person("Alice")
    d = Department()

    d.charge_code = "D100"
    d.manager = "Charlie"

    # Person에 Department 객체를 세팅
    p.department = d

    assert p.department is d
    assert p.department.charge_code == "D100"
    assert p.department.manager == "Charlie"


@pytest.mark.parametrize(
    "charge_code, manager",
    [
        ("ENG-001", "Eve"),
        ("SALES-007", "Mallory"),
    ],
)
def test_department_parametrized(charge_code, manager):
    """
    다양한 케이스에 대해 Department의 chargeCode와 manager를 설정해보는 파라미터라이즈 테스트.
    """
    d = Department()
    d.charge_code = charge_code
    d.manager = manager

    assert d.charge_code == charge_code
    assert d.manager == manager
