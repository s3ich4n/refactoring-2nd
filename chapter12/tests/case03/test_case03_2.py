from chapter12.src.case03.case03_2 import (
    Employee,
    Manager,
)


class TestEmployee:
    def test_employee_creation(self):
        """일반 직원 생성 테스트"""
        employee = Employee("John Doe")
        assert employee._name == "John Doe"
        assert employee.is_privileged is False

    def test_manager_without_privilege(self):
        """특권이 없는 매니저 테스트"""
        manager = Manager("Jane Smith", 3)
        assert manager._name, "Jane Smith"
        assert manager._grade, 3
        assert manager.is_privileged is False

    def test_manager_with_privilege(self):
        """특권이 있는 매니저 테스트"""
        manager = Manager("Robert Johnson", 5)
        assert manager._name, "Robert Johnson"
        assert manager._grade, 5
        assert manager.is_privileged is True

    def test_assign_car_called(self):
        """특권이 있는 매니저가 자동차를 할당받는지 테스트"""

        # assign_car 메소드가 호출되었는지 확인하기 위한 모의 구현
        class TestManager(Manager):
            def __init__(self, name, grade):
                self.car_assigned = False
                super().__init__(name, grade)

            def assign_car(self):
                self.car_assigned = True

        # 특권이 없는 매니저
        manager1 = TestManager("Alice", 3)
        assert manager1.car_assigned is False

        # 특권이 있는 매니저
        manager2 = TestManager("Bob", 5)
        assert manager2.car_assigned is True
