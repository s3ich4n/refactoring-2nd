from chapter12.src.case01.case01 import Department, Employee


class TestPullUpMethod:
    def test_department_annual_cost(self):
        """Department 클래스의 annual_cost 메서드가 올바르게 계산되는지 테스트"""
        department = Department()

        # 기본 monthly_cost는 10
        assert department.monthly_cost == 10
        assert department.annual_cost() == 120  # 10 * 12

        # monthly_cost 변경 시 annual_cost도 변경되어야 함
        department.monthly_cost = 20
        assert department.annual_cost() == 240  # 20 * 12

    def test_employee_annual_cost(self):
        """Employee 클래스의 annual_cost 메서드가 올바르게 계산되는지 테스트"""
        employee = Employee()

        # 기본 monthly_cost는 10
        assert employee.monthly_cost == 10
        assert employee.annual_cost() == 120  # 10 * 12

        # monthly_cost 변경 시 annual_cost도 변경되어야 함
        employee.monthly_cost = 15
        assert employee.annual_cost() == 180  # 15 * 12

    def test_annual_cost_implementation_consistency(self):
        """Department와 Employee의 annual_cost 구현이 동일한지 확인하는 테스트"""
        department = Department()
        employee = Employee()

        # 두 클래스의 monthly_cost를 동일하게 설정
        department.monthly_cost = 30
        employee.monthly_cost = 30

        # 두 클래스의 annual_cost 결과가 동일해야 함
        assert department.annual_cost() == employee.annual_cost()

        # monthly_cost를 변경해도 동일성이 유지되어야 함
        department.monthly_cost = 50
        employee.monthly_cost = 50
        assert department.annual_cost() == employee.annual_cost()
