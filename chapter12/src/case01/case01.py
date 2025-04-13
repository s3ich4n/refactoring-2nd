class Party:
    def __init__(self):
        self.monthly_cost = 10


class Department(Party):
    def __init__(self):
        super().__init__()

    def total_annual_cost(self):
        return self.monthly_cost * 12


class Employee(Party):
    def __init__(self):
        super().__init__()

    def annual_cost(self):
        return self.monthly_cost * 12
