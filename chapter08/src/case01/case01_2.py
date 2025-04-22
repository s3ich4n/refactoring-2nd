
class AccountType:
    def __init__(self, is_premium=False):
        self._is_premium = is_premium
    
    @property
    def is_premium(self):
        return self._is_premium


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
            result += self.overdraft_charge
        return result
    
    @property
    def overdraft_charge(self):
        if self.account_type.is_premium:
            base_charge = 10
            if self.days_overdrawn <= 7:
                return base_charge
            else:
                return base_charge + (self.days_overdrawn - 7) * 0.85
        else:
            return self.days_overdrawn * 1.75
