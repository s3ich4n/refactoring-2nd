# pytest 테스트 코드
import pytest

from chapter12.src.case06.case06 import Employee


def test_employee_creation_with_valid_types():
    """유효한 타입으로 직원을 생성할 수 있는지 테스트"""
    valid_types = ["engineer", "manager", "salesman"]

    for type in valid_types:
        employee = Employee("Test Employee", type)
        assert employee._name == "Test Employee"
        assert employee._type == type
        assert str(employee) == f"Test Employee ({type})"


def test_employee_creation_with_invalid_type():
    """유효하지 않은 타입으로 직원을 생성할 때 예외가 발생하는지 테스트"""
    with pytest.raises(ValueError) as excinfo:
        Employee("Test Employee", "developer")

    assert "Employee cannot be of type developer" in str(excinfo.value)


def test_employee_string_representation():
    """직원의 문자열 표현이 올바른지 테스트"""
    employee = Employee("John Doe", "engineer")
    assert str(employee) == "John Doe (engineer)"

    employee = Employee("Jane Smith", "manager")
    assert str(employee) == "Jane Smith (manager)"

    employee = Employee("Bob Johnson", "salesman")
    assert str(employee) == "Bob Johnson (salesman)"
