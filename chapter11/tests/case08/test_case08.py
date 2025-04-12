import pytest

from chapter11.src.case08.case08 import Employee


class TestEmployee:
    """Employee 클래스 테스트"""

    def test_create_employee(self):
        """Employee 객체 생성 테스트"""
        employee = Employee.create("John Doe", "E")
        assert employee._name == "John Doe"
        assert employee._type_code == "E"

    def test_name_property(self):
        """name 속성 테스트"""
        employee = Employee("Jane Smith", "M")
        assert employee.name == "Jane Smith"

    def test_type_property(self):
        """type 속성 테스트 - 타입 코드가 올바르게 변환되는지"""
        engineer = Employee("Bob", "E")
        manager = Employee("Alice", "M")
        salesman = Employee("Charlie", "S")

        assert engineer.employee_type == "Engineer"
        assert manager.employee_type == "Manager"
        assert salesman.employee_type == "Salesman"

    def test_legal_type_codes(self):
        """legal_type_codes 정적 메서드 테스트"""
        codes = Employee.legal_type_codes()

        assert isinstance(codes, dict)
        assert len(codes) == 3
        assert codes["E"] == "Engineer"
        assert codes["M"] == "Manager"
        assert codes["S"] == "Salesman"

    def test_invalid_type_code(self):
        """유효하지 않은 타입 코드 처리 테스트"""
        employee = Employee("Invalid", "X")

        # 유효하지 않은 타입 코드를 사용하면 KeyError가 발생해야 함
        with pytest.raises(KeyError):
            employee_type = employee.employee_type
