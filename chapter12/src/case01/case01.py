class Party:
    def __init__(self):
        self.monthly_cost = 10

    def annual_cost(self):
        return self.monthly_cost * 12

    def monthly_cost(self):
        raise NotImplementedError()


class Department(Party):
    def __init__(self):
        super().__init__()


class Employee(Party):
    def __init__(self):
        super().__init__()
