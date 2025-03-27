# AS-IS 코드
class Site:
    def __init__(self, customer=None):
        self._customer = customer

    @property
    def customer(self):
        return self._customer


class Customer:
    def __init__(self, name, billing_plan, payment_history):
        self._name = name
        self._billing_plan = billing_plan
        self._payment_history = payment_history

    @property
    def name(self):
        return self._name

    @property
    def billing_plan(self):
        return self._billing_plan

    @billing_plan.setter
    def billing_plan(self, arg):
        self._billing_plan = arg

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


# 클라이언트 코드 (AS-IS)
def get_customer_name(site):
    a_customer = site.customer
    # ... lots of intervening code ...
    if a_customer == "unknown":
        customer_name = "occupant"
    else:
        customer_name = a_customer.name
    return customer_name


def get_billing_plan(site, registry):
    a_customer = site.customer
    if a_customer == "unknown":
        plan = registry.billing_plans["basic"]
    else:
        plan = a_customer.billing_plan
    return plan


def set_billing_plan(site, new_plan):
    a_customer = site.customer
    if a_customer != "unknown":
        a_customer.billing_plan = new_plan


def get_weeks_delinquent(site):
    a_customer = site.customer
    if a_customer == "unknown":
        weeks_delinquent = 0
    else:
        weeks_delinquent = a_customer.payment_history.weeks_delinquent_in_last_year
    return weeks_delinquent
