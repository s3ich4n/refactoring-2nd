class Site:
    def __init__(self, customer=None):
        # customer가 "unknown" 문자열이면 UnknownCustomer 객체로 변환
        if customer == "unknown":
            self._customer = UnknownCustomer(True)
        else:
            self._customer = customer

    @property
    def customer(self):
        return self._customer


class Customer:
    def __init__(self, name, billing_plan, payment_history):
        self._name = name
        self._billing_plan = billing_plan
        self._payment_history = payment_history

    def is_unknown(self):
        return False

    @property
    def name(self):
        return self._name

    @property
    def billing_plan(self):
        return self._billing_plan

    @billing_plan.setter
    def billing_plan(self, arg):
        ...
        # self._billing_plan = arg

    @property
    def payment_history(self):
        return self._payment_history


class PaymentHistory:
    def __init__(self, weeks_delinquent):
        self._weeks_delinquent = weeks_delinquent

    @property
    def weeks_delinquent_in_last_year(self):
        return self._weeks_delinquent


class Registry:
    def __init__(self):
        self.billing_plans = {"basic": "basic plan", "premium": "premium plan"}


# XXX
#   파이썬도 자바스크립트처럼 동적 타이핑이 되도록 코드를 구성해볼 예정
class UnknownCustomer:
    def __init__(self, unknown):
        self._unknown = unknown

    @property
    def is_unknown(self):
        return self._unknown

    @property
    def name(self):
        return "occupant"


# 클라이언트 코드
def get_customer_name(site):
    a_customer = site.customer
    # ... lots of intervening code ...
    customer_name = a_customer.name
    return customer_name


def get_billing_plan(site, registry):
    a_customer = site.customer

    plan = (
        registry.billing_plans["basic"]
        if is_unknown(a_customer)
        else a_customer.billing_plan
    )

    return plan


def set_billing_plan(site, new_plan):
    a_customer = site.customer

    if not is_unknown(a_customer):
        a_customer.billing_plan = new_plan


def get_weeks_delinquent(site):
    a_customer = site.customer
    weeks_delinquent = (
        0
        if is_unknown(a_customer)
        else a_customer.payment_history.weeks_delinquent_in_last_year
    )

    return weeks_delinquent


def is_unknown(arg):
    if not (isinstance(arg, Customer) or isinstance(arg, UnknownCustomer)):
        raise Exception("unknown customer")

    if isinstance(arg, Customer):
        return arg.is_unknown()
    else:
        return arg.is_unknown
