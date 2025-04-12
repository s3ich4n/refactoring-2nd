class Employee:
    def __init__(self, name, type_code):
        self._name = name
        self._type_code = type_code

    @classmethod
    def create(
        cls,
        name,
        type_code,
    ):
        return cls(name=name, type_code=type_code)

    @classmethod
    def create_engineer(cls, name):
        return cls(name=name, type_code="E")

    @property
    def name(self):
        return self._name

    @property
    def employee_type(self):
        return Employee.legal_type_codes()[self._type_code]

    @staticmethod
    def legal_type_codes():
        return {"E": "Engineer", "M": "Manager", "S": "Salesman"}
