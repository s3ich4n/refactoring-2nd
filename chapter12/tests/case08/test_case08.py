from chapter12.src.case08.case08 import Employee, Department


def test_employee_creation():
    # 직원 객체 생성 및 기본 속성 테스트
    emp = Employee("홍길동", "E123", 5000000)
    assert emp.name == "홍길동"
    assert emp.id == "E123"
    assert emp.monthly_cost == 5000000


def test_employee_annual_cost():
    # 직원의 연간 비용 계산 테스트
    emp = Employee("김철수", "E456", 4000000)
    assert emp.annual_cost == 48000000  # 4,000,000 * 12


def test_department_creation():
    # 부서 객체 생성 및 기본 속성 테스트
    emp1 = Employee("홍길동", "E123", 5000000)
    emp2 = Employee("김철수", "E456", 4000000)
    dept = Department("개발팀", [emp1, emp2])

    assert dept.name == "개발팀"
    assert len(dept.staff) == 2
    assert dept.head_count == 2


def test_department_staff_copy():
    # staff가 복사본을 반환하는지 테스트
    emp1 = Employee("홍길동", "E123", 5000000)
    emp2 = Employee("김철수", "E456", 4000000)
    staff_original = [emp1, emp2]
    dept = Department("개발팀", staff_original)

    staff_copy = dept.staff
    assert staff_copy is not staff_original  # 동일한 객체 참조가 아님을 확인
    assert staff_copy == staff_original  # 내용은 동일함을 확인


def test_department_total_monthly_cost():
    # 부서의 월 총비용 계산 테스트
    emp1 = Employee("홍길동", "E123", 5000000)
    emp2 = Employee("김철수", "E456", 4000000)
    emp3 = Employee("이영희", "E789", 6000000)

    dept = Department("개발팀", [emp1, emp2, emp3])
    expected_monthly_cost = 5000000 + 4000000 + 6000000

    assert dept.total_monthly_cost == expected_monthly_cost


def test_department_total_annual_cost():
    # 부서의 연간 총비용 계산 테스트
    emp1 = Employee("홍길동", "E123", 5000000)
    emp2 = Employee("김철수", "E456", 4000000)

    dept = Department("개발팀", [emp1, emp2])
    expected_monthly_cost = 5000000 + 4000000
    expected_annual_cost = expected_monthly_cost * 12

    assert dept.total_annual_cost == expected_annual_cost


def test_empty_department():
    # 직원이 없는 부서 테스트
    dept = Department("빈 부서", [])

    assert dept.head_count == 0
    assert dept.total_monthly_cost == 0
    assert dept.total_annual_cost == 0
