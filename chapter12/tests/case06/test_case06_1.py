# pytest 테스트 코드
import pytest

from chapter12.src.case06.case06_1 import Employee


@pytest.mark.parametrize(
    "employee_type, is_problem",
    [
        pytest.param("engineer", False, id="(valid) engineer"),
        pytest.param("manager", False, id="(valid) manager"),
        pytest.param("student", True, id="(invalid) student"),
    ],
)
def test_employee_creation_with_valid_types(employee_type, is_problem):
    """유효한 타입으로 직원을 생성할 수 있는지 테스트"""
    if is_problem:
        with pytest.raises(NotImplementedError) as excinfo:
            _ = Employee.create("Test Employee", employee_type)
            assert f"Employee cannot be of type {employee_type}" in str(excinfo.value)
    else:
        employee = Employee.create("Test Employee", employee_type)
        assert employee._name == "Test Employee"
        assert employee.employee_type == employee_type
        assert str(employee) == f"{employee_type.capitalize()} - Test Employee"


def test_employee_string_representation():
    """직원의 문자열 표현이 올바른지 테스트"""
    employee = Employee.create("John Doe", "engineer")
    assert str(employee) == "Engineer - John Doe"

    employee = Employee.create("Jane Smith", "manager")
    assert str(employee) == "Manager - Jane Smith"

    employee = Employee.create("Bob Johnson", "salesperson")
    assert str(employee) == "Salesperson - Bob Johnson"


def test_engineer_creation():
    engineer = Employee.create(name="<NAME>", employee_type="engineer")
    assert engineer.employee_type == "engineer"


def test_manager_creation():
    manager = Employee.create(name="<NAME>", employee_type="manager")
    assert manager.employee_type == "manager"


def test_salesperson_creation():
    salesperson = Employee.create(name="<NAME>", employee_type="salesperson")
    assert salesperson.employee_type == "salesperson"
