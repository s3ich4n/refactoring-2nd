# order.py
class Priority:
    def __init__(self, priority):
        self._priority = priority

    def __str__(self):
        return self._priority


class Order:
    def __init__(self, data):
        self._priority = data.get("priority", "normal")  # 기본값 설정
        self._product = data.get("product")
        self._quantity = data.get("quantity", 0)
        self._buyer = data.get("buyer")

    def priority_string(self):
        return str(self._priority)

    def set_priority(self, value):
        self._priority = Priority(value)


def count_high_priority_orders(orders):
    return len(
        [order for order in orders if order.priority_string() in ("high", "rush")]
    )
