class Account:
    def __init__(self, number, account_type, interest_rate):
        self._number = number
        self._account_type = account_type
        # 코어 동작이 바뀌지 않는 선에서 필드를 옮겨야한다.
        # 그게 아니면 기능 변경이다. 리팩터링 그 이상의 것이 된다는 말.
        if interest_rate is not None:
            self._account_type.interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._account_type.interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._account_type.interest_rate = value

    @property
    def number(self):
        return self._number

    @property
    def account_type(self):
        return self._account_type


class AccountType:
    def __init__(self, name_string, interest_rate=None):
        self._name = name_string
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value
