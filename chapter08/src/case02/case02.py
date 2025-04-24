from datetime import date


def date_today():
    return date.today()


class Customer:
    def __init__(self, name, discount_rate):
        self.name = name
        self.set_discount_rate(discount_rate)
        self.contract = CustomerContract(date_today())

    @property
    def discount_rate(self):
        return self._discount_rate

    def set_discount_rate(self, a_number):
        self._discount_rate = a_number

    def become_preferred(self):
        self._discount_rate += 0.03
        # other nice things

    def apply_discount(self, amount):
        return amount - (amount * self.discount_rate)


class CustomerContract:
    def __init__(self, start_date):
        self.start_date = start_date
