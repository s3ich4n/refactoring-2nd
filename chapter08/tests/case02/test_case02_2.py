from chapter08.src.case02.case02_2 import Account, AccountType


class TestAccount:
    def test_initialization(self):
        # Setup
        account_type = AccountType("Savings")
        account = Account("12345", account_type, 0.05)

        # Verify
        assert account.number == "12345"
        assert account.account_type == account_type
        assert account.interest_rate == 0.05

    def test_interest_rate_property(self):
        # Setup
        account_type = AccountType("Checking")
        account = Account("67890", account_type, 0.03)

        # Exercise
        account.interest_rate = 0.04

        # Verify
        assert account.interest_rate == 0.04


class TestAccountType:
    def test_initialization(self):
        # Setup
        account_type = AccountType("Premium")

        # Verify
        assert account_type._name == "Premium"
