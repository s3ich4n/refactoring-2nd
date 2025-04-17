class Employee:
    def __init__(self, name, id, monthly_cost):
        self._id = id
        self._name = name
        self._monthly_cost = monthly_cost

    @property
    def monthly_cost(self):
        return self._monthly_cost

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def annual_cost(self):
        return self.monthly_cost * 12


class Department:
    def __init__(self, name, staff):
        self._name = name
        self._staff = staff

    @property
    def staff(self):
        return self._staff.copy()

    @property
    def name(self):
        return self._name

    @property
    def total_monthly_cost(self):
        return sum(e.monthly_cost for e in self.staff)

    @property
    def head_count(self):
        return len(self.staff)

    @property
    def total_annual_cost(self):
        return self.total_monthly_cost * 12
