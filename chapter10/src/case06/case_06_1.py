class Customer:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def apply_discount(self, a_number):
        return (
            a_number - (self.discount_rate * a_number)
            if self.discount_rate
            else a_number
        )
