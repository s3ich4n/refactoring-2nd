import pytest
from src.case08.case08 import (
    Person,
    Department,
)


def test_person_basic():
    """department를 반드시 넣어야함

    :return:
    """
    with pytest.raises(TypeError):
        Person("Alice")


def test_department_basic():
    """
    Department 객체를 생성하고, chargeCode와 manager 게터/세터가 잘 동작하는지 테스트.
    """
    department = Department()
    assert department.charge_code is None
    assert department.manager is None

    department.charge_code = "CODE123"
    department.manager = "Bob"

    assert department.charge_code == "CODE123"
    assert department.manager == "Bob"


def test_person_and_department():
    """
    Person에 Department를 연결했을 때 정상적으로 참조가 이뤄지는지 확인.
    """
    department = Department()
    department.charge_code = "D100"
    department.manager = "Charlie"
    sut = Person("Alice", department=department)

    assert sut.department.manager == "Charlie"
    assert sut.department.charge_code == "D100"


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
    department = Department()
    department.charge_code = charge_code
    department.manager = manager
    sut = Person("Alice", department=department)

    assert sut.department.manager == manager
    assert sut.department.charge_code == charge_code
