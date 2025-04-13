class Employee:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f"{self.__class__.__name__} - {self._name}"

    @classmethod
    def create(cls, name, employee_type):
        if employee_type == "engineer":
            return Engineer(name)
        elif employee_type == "manager":
            return Manager(name)
        elif employee_type == "salesperson":
            return Salesperson(name)
        else:
            raise NotImplementedError(f"Employee cannot be of type {employee_type}")


class Engineer(Employee):
    @property
    def employee_type(self):
        # 일부러 잘 받아오는지 고장내기
        return "engineer"


class Manager(Employee):
    @property
    def employee_type(self):
        return "manager"


class Salesperson(Employee):
    @property
    def employee_type(self):
        return "salesperson"
