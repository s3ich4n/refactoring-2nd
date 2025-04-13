from chapter12.src.case03.case03 import Party, Employee, Department


class TestCase03:
    def test_employee_initialization(self):
        # 테스트 데이터 설정
        name = "John Doe"
        user_id = "jdoe123"
        monthly_cost = 5000

        # Employee 인스턴스 생성
        employee = Employee(name, user_id, monthly_cost)

        # 필드 값이 올바르게 설정되었는지 검증
        assert employee._name == name
        assert employee._user_id == user_id
        assert employee._monthly_cost == monthly_cost

    def test_department_initialization(self):
        # 테스트 데이터 설정
        name = "Engineering"
        employee1 = Employee("Jane Smith", "jsmith456", 6000)
        employee2 = Employee("Bob Johnson", "bjohnson789", 7000)
        staff = [employee1, employee2]

        # Department 인스턴스 생성
        department = Department(name, staff)

        # 필드 값이 올바르게 설정되었는지 검증
        assert department._name == name
        assert department._staff == staff

    def test_inheritance_relationship(self):
        # Employee와 Department가 Party를 상속받았는지 확인
        employee = Employee("Test Employee", "emp001", 4000)
        department = Department("Test Department", [])

        assert isinstance(employee, Party)
        assert isinstance(department, Party)
