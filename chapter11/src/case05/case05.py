class Order:
    def __init__(self, quantity, item_price):
        self.quantity = quantity
        self.item_price = item_price

    def final_price(self):
        """
        최종 가격을 계산
        """
        base_price = self.quantity * self.item_price
        discount_level = self._discount_level()
        return self.discounted_price(base_price, discount_level)

    def _discount_level(self):
        """
        할인 레벨을 결정하는 내부 메서드
        """
        if self.quantity > 100:
            return 2
        return 1

    def discounted_price(self, base_price, discount_level):
        """
        할인된 가격을 계산합니다.
        """
        discount_factors = {1: 0.95, 2: 0.9}
        return base_price * discount_factors.get(discount_level, 1.0)
