class Account:
    def __init__(self, number, account_type, interest_rate):
        self.number = number
        self.account_type = account_type
        self.interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value


class AccountType:
    def __init__(self, name_string):
        self._name = name_string
