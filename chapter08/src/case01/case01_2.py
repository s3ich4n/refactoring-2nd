class AccountType:
    def __init__(self, is_premium=False):
        self._is_premium = is_premium

    @property
    def is_premium(self):
        return self._is_premium

    def overdraft_charge(self, days_overdrawn=0):
        """

        Notes:
            일단 값으로 넘기고,
            overdrawn date 이상의 값이 필요하면 `Account` 를 통째로 던지면 됨
        """
        if self.is_premium:
            base_charge = 10
            if days_overdrawn <= 7:
                return base_charge
            else:
                return base_charge + (days_overdrawn - 7) * 0.85
        else:
            return days_overdrawn * 1.75


class Account:
    def __init__(self, account_type=None, days_overdrawn=0):
        self._account_type = account_type if account_type else AccountType()
        self._days_overdrawn = days_overdrawn

    @property
    def account_type(self):
        return self._account_type

    @property
    def days_overdrawn(self):
        return self._days_overdrawn

    @property
    def bank_charge(self):
        result = 4.5
        if self.days_overdrawn > 0:
            # 인라인하는 방법도 있고,
            result += self.overdraft_charge
        return result

    @property
    def overdraft_charge(self):
        """직접 위임해서 쓰는 방법도 있다. 나는 이쪽이 더 마음에든다."""
        return self._account_type.overdraft_charge(self._days_overdrawn)
