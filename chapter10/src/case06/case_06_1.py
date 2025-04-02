class Customer:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def apply_discount(self, a_number):
        assert a_number >= 0, "금액은 음수가 될 수 없습니다"

        if self.discount_rate:
            assert isinstance(
                self.discount_rate, (int, float)
            ), "할인율은 숫자여야 합니다"
            return a_number - (self.discount_rate * a_number)
        else:
            return a_number
