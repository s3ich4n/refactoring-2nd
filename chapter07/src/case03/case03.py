# order.py
class Order:
    def __init__(self, data):
        self.priority = data.get("priority", "normal")  # 기본값 설정
        self.product = data.get("product")
        self.quantity = data.get("quantity", 0)
        self.buyer = data.get("buyer")


def count_high_priority_orders(orders):
    return len([order for order in orders if order.priority in ("high", "rush")])
