from chapter10.src.case05.case05 import (
    PaymentHistory,
    Site,
    get_customer_name,
    Customer,
    Registry,
    get_billing_plan,
    set_billing_plan,
    get_weeks_delinquent,
)


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
    assert customer.billing_plan == "new plan"


def test_get_weeks_delinquent():
    # 일반 고객 테스트
    payment_history = PaymentHistory(5)
    customer = Customer("John", "premium plan", payment_history)
    site = Site(customer)
    assert get_weeks_delinquent(site) == 5

    # unknown 고객 테스트
    site_unknown = Site("unknown")
    assert get_weeks_delinquent(site_unknown) == 0
