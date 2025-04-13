# pytest 테스트 코드
import pytest

from chapter12.src.case06.case06 import (
    Employee,
    Engineer,
)


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
        with pytest.raises(ValueError) as excinfo:
            _ = Employee("Test Employee", employee_type)
            assert f"Employee cannot be of type {employee_type}" in str(excinfo.value)
    else:
        employee = Employee("Test Employee", employee_type)
        assert employee._name == "Test Employee"
        assert employee.employee_type == employee_type
        assert str(employee) == f"Test Employee ({employee_type})"


def test_employee_string_representation():
    """직원의 문자열 표현이 올바른지 테스트"""
    employee = Employee("John Doe", "engineer")
    assert str(employee) == "John Doe (engineer)"

    employee = Employee("Jane Smith", "manager")
    assert str(employee) == "Jane Smith (manager)"

    employee = Employee("Bob Johnson", "salesman")
    assert str(employee) == "Bob Johnson (salesman)"


def test_engineer_creation():
    engineer = Engineer(name="<NAME>", employee_type="engineer")
