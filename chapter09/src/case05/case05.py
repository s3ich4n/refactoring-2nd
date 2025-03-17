class Customer:
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id


class Order:
    def __init__(self, data):
        self._number = data["number"]
        self._customer = Customer(data["customer"])  # 다른 데이터 로드

    @property
    def customer(self):
        return self._customer
