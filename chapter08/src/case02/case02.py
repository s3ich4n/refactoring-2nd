from datetime import date


def date_today():
    return date.today()


class Customer:
    def __init__(self, name, discount_rate):
        self.name = name
        self._discount_rate = discount_rate
        self.contract = CustomerContract(date_today())

    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, value):
        self._discount_rate = value

    def become_preferred(self):
        self._discount_rate += 0.03
        # other nice things

    def apply_discount(self, amount):
        return amount - (amount * self.discount_rate)


class CustomerContract:
    def __init__(self, start_date):
        self.start_date = start_date
