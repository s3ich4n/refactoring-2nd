from chapter10.src.case05.case05_1 import (
    UnknownCustomer,
    PaymentHistory,
    Site,
    get_customer_name,
    Customer,
    Registry,
    get_billing_plan,
    set_billing_plan,
    get_weeks_delinquent,
)


def test_customer_properties():
    # 일반 고객 생성 및 속성 테스트
    payment_history = PaymentHistory(5)
    customer = Customer("John", "premium plan", payment_history)

    assert customer.name == "John"
    assert customer.billing_plan == "premium plan"
    assert customer.payment_history.weeks_delinquent_in_last_year == 5
    assert customer.is_unknown() is False


def test_get_customer_name():
    # 일반 고객 테스트
    payment_history = PaymentHistory(5)
    customer = Customer("John", "premium plan", payment_history)
    site = Site(customer)
    assert get_customer_name(site) == "John"

    # unknown 고객 테스트
    site_unknown = Site("unknown")
    assert get_customer_name(site_unknown) == "occupant"


def test_get_billing_plan():
    # 일반 고객 테스트
    payment_history = PaymentHistory(5)
    customer = Customer("John", "premium plan", payment_history)
    site = Site(customer)
    registry = Registry()
    assert get_billing_plan(site, registry) == "premium plan"

    # unknown 고객 테스트
    site_unknown = Site("unknown")
    assert get_billing_plan(site_unknown, registry) == "basic plan"


def test_set_billing_plan():
    # 일반 고객 테스트
    payment_history = PaymentHistory(5)
    customer = Customer("John", "premium plan", payment_history)
    site = Site(customer)
    set_billing_plan(site, "new plan")
    # setter를 없앴으니까 이를 반영
    assert customer.billing_plan == "premium plan"

    # unknown 고객에 대한 테스트 - 값이 변경되지 않음
    site_unknown = Site("unknown")
    # 예외가 발생하지 않는지 확인
    set_billing_plan(site_unknown, "new plan")


def test_get_weeks_delinquent():
    # 일반 고객 테스트
    payment_history = PaymentHistory(5)
    customer = Customer("John", "premium plan", payment_history)
    site = Site(customer)
    assert get_weeks_delinquent(site) == 5

    # unknown 고객 테스트
    site_unknown = Site("unknown")
    assert get_weeks_delinquent(site_unknown) == 0


def test_unknown_customer_class():
    # UnknownCustomer 클래스 테스트
    unknown_customer = UnknownCustomer(True)
    assert unknown_customer.is_unknown is True

    known_customer = UnknownCustomer(False)
    assert known_customer.is_unknown is False
