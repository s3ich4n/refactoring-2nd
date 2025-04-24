from datetime import date


def date_today():
    return date.today()


class Customer:
    def __init__(self, name, discount_rate):
        self.name = name
        self._contract = CustomerContract(date_today())
        self.set_discount_rate(discount_rate)

    @property
    def discount_rate(self):
        return self.contract.discount_rate

    @property
    def contract(self):
        return self._contract

    def set_discount_rate(self, a_number):
        self.contract._discount_rate = a_number

    def become_preferred(self):
        self.set_discount_rate(self.discount_rate + 0.03)
        # other nice things

    def apply_discount(self, amount):
        return amount - (amount * self.discount_rate)


class CustomerContract:
    def __init__(self, start_date, discount_rate=None):
        self._start_date = start_date
        self._discount_rate = discount_rate

    @property
    def start_date(self):
        return self._start_date

    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, a_number):
        self._discount_rate = a_number
