import pytest

from chapter12.src.case06.case06_2 import (
    Employee,
    Engineer,
    Manager,
    Salesman,
)


def test_employee_creation_with_valid_types():
    """유효한 타입으로 직원을 생성할 수 있는지 테스트"""
    valid_types = ["engineer", "manager", "salesman"]
    expected_classes = [Engineer, Manager, Salesman]

    for i, type_value in enumerate(valid_types):
        employee = Employee("Test Employee", type_value)
        assert employee._name == "Test Employee"
        assert isinstance(employee._type, expected_classes[i])


def test_employee_creation_with_invalid_type():
    """유효하지 않은 타입으로 직원을 생성할 때 예외가 발생하는지 테스트"""
    with pytest.raises(ValueError) as excinfo:
        Employee("Test Employee", "developer")

    assert "Employee cannot be of type developer" in str(excinfo.value)


def test_employee_type_setter():
    """type 속성의 setter가 올바르게 작동하는지 테스트"""
    employee = Employee("John Doe", "engineer")
    assert isinstance(employee.type, Engineer)

    employee.type = "manager"
    assert isinstance(employee.type, Manager)

    # 유효하지 않은 타입으로 설정 시도
    with pytest.raises(ValueError) as excinfo:
        employee.type = "developer"
    assert "Employee cannot be of type developer" in str(excinfo.value)


def test_employee_capitalized_type():
    """capitalized_type 속성이 올바르게 작동하는지 테스트"""
    employee = Employee("John Doe", "engineer")
    assert employee.capitalized_type == "Engineer"

    employee = Employee("Jane Smith", "manager")
    assert employee.capitalized_type == "Manager"

    employee = Employee("Bob Johnson", "salesman")
    assert employee.capitalized_type == "Salesman"


def test_employee_string_representation():
    """직원의 문자열 표현이 올바른지 테스트"""
    employee = Employee("John Doe", "engineer")
    assert str(employee) == "John Doe (Engineer)"

    employee = Employee("Jane Smith", "manager")
    assert str(employee) == "Jane Smith (Manager)"

    employee = Employee("Bob Johnson", "salesman")
    assert str(employee) == "Bob Johnson (Salesman)"


def test_employee_type_classes():
    """EmployeeType 서브클래스들이 올바르게 작동하는지 테스트"""
    engineer = Engineer()
    manager = Manager()
    salesman = Salesman()

    assert str(engineer) == "engineer"
    assert str(manager) == "manager"
    assert str(salesman) == "salesman"
