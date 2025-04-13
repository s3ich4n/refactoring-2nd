class Party:
    def __init__(self, name):
        self._name = name


class Employee(Party):
    def __init__(self, name, user_id, monthly_cost):
        super().__init__(name)
        self._user_id = user_id
        self._monthly_cost = monthly_cost


class Department(Party):
    def __init__(self, name, staff):
        super().__init__(name)
        self._staff = staff
