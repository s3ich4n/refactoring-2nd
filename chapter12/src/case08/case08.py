class Party:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Employee(Party):
    def __init__(self, name, employee_id, monthly_cost):
        super().__init__(name)
        self._employee_id = employee_id
        self._name = name
        self._monthly_cost = monthly_cost

    @property
    def monthly_cost(self):
        return self._monthly_cost

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def annual_cost(self):
        return self.monthly_cost * 12


class Department(Party):
    def __init__(self, name, staff):
        super().__init__(name)
        self._name = name
        self._staff = staff

    @property
    def staff(self):
        return self._staff.copy()

    @property
    def monthly_cost(self):
        return sum(e.monthly_cost for e in self.staff)

    @property
    def head_count(self):
        return len(self.staff)

    @property
    def annual_cost(self):
        return self.monthly_cost * 12
