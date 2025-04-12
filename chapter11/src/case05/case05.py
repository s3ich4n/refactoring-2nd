class Order:
    def __init__(self, quantity, item_price):
        self.quantity = quantity
        self.item_price = item_price

    def final_price(self):
        """
        최종 가격을 계산
        """
        base_price = self.quantity * self.item_price
        return self.discounted_price(base_price)

    def discounted_price(self, base_price):
        """
        할인된 가격을 계산합니다.
        """
        return base_price * 0.9 if self.quantity > 100 else base_price * 0.95
