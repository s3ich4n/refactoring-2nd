from datetime import date

from chapter08.src.case02.case02_1 import (
    Customer,
    date_today,
    CustomerContract,
)


class TestCustomer:
    def test_initialization(self):
        # Setup
        customer = Customer("홍길동", 0.1)

        # Verify
        assert customer.name == "홍길동"
        assert customer.discount_rate == 0.1
        assert isinstance(customer.contract, CustomerContract)
        assert customer.contract.start_date == date_today()

    def test_become_preferred(self):
        # Setup
        customer = Customer("홍길동", 0.1)
        initial_discount = customer.discount_rate

        # Exercise
        customer.become_preferred()

        # Verify
        assert customer.discount_rate == initial_discount + 0.03

    def test_apply_discount(self):
        # Setup
        customer = Customer("홍길동", 0.1)
        amount = 1000

        # Exercise
        discounted_amount = customer.apply_discount(amount)

        # Verify
        assert discounted_amount == amount - (amount * customer.discount_rate)
        assert discounted_amount == 900


class TestCustomerContract:
    def test_initialization(self):
        # Setup
        today = date.today()
        contract = CustomerContract(today)

        # Verify
        assert contract.start_date == today
