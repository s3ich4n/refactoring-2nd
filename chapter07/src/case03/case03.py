# order.py
class Priority:
    _values = ("low", "normal", "high", "rush")

    def __init__(self, value):
        if value not in self._values:
            raise ValueError(f"Invalid priority value: {value}")
        self._value = value

    def higher_than(self, other):
        return self._values.index(self._value) > self._values.index(other._value)

    def __str__(self):
        return self._value

    def __eq__(self, other):
        return self._values.index(self._value) == self._values.index(other._value)


class Order:
    def __init__(self, data):
        self._priority = Priority(data.get("priority", "normal"))
        self._product = data.get("product")
        self._quantity = data.get("quantity", 0)
        self._buyer = data.get("buyer")

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = Priority(value) if isinstance(value, str) else value


def count_high_priority_orders(orders):
    return len(
        [order for order in orders if order.priority.higher_than(Priority("normal"))]
    )
