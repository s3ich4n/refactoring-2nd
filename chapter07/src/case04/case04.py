class Order:
    def __init__(self, quantity, item):
        self._quantity = quantity
        self._item = item

    @property
    def base_price(self):
        return self._quantity * self._item.price

    @property
    def discount_factor(self):
        discount_factor = 0.98
        if self.base_price > 1000:
            discount_factor -= 0.03

        return discount_factor

    @property
    def price(self):
        return self.base_price * self.discount_factor


class Item:
    def __init__(self, price):
        self.price = price
