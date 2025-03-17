from chapter09.src.case05.case05 import (
    Order,
    Customer,
    CustomerRepository,
    initialize,
    register_customer,
    find_customer,
)


def test_order_and_customer():
    # 테스트 데이터 생성
    order_data = {"number": "12345", "customer": "C001"}

    # Order 객체 생성
    order = Order(order_data)

    # 테스트 검증
    assert order._number == "12345"
    assert order.customer.id == "C001"

    # Customer 객체가 올바르게 생성되었는지 확인
    assert isinstance(order.customer, Customer)
    assert order.customer._id == "C001"


def test_customer_repository_class():
    # 객체지향 방식으로 레포지토리 사용
    repo = CustomerRepository()

    # 고객 등록
    customer = repo.register_customer("C001")

    # 검증
    assert customer.id == "C001"
    assert repo.find_customer("C001") is customer
    assert repo.find_customer("nonexistent") is None


def test_legacy_singleton_functions():
    # 초기화
    initialize()

    # 고객 등록
    customer = register_customer("C002")

    # 검증
    assert customer.id == "C002"
    assert find_customer("C002") is customer
    assert find_customer("nonexistent") is None
