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


class CustomerRepository:
    def __init__(self):
        self._customers = {}

    def register_customer(self, id):
        if id not in self._customers:
            self._customers[id] = Customer(id)
        return self.find_customer(id)

    def find_customer(self, id):
        return self._customers.get(id)


# 기존 API와의 호환성을 위한 싱글톤 인스턴스
_default_repository = None


def initialize():
    global _default_repository
    _default_repository = CustomerRepository()


def register_customer(id):
    return _default_repository.register_customer(id)


def find_customer(id):
    return _default_repository.find_customer(id)
