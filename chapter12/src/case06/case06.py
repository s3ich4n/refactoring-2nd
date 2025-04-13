class Employee:
    def __init__(self, name, employee_type):
        self.validate_type(employee_type)
        self._name = name
        self._employee_type = employee_type

    def validate_type(self, arg):
        if arg not in ["engineer", "manager", "salesman"]:
            raise ValueError(f"Employee cannot be of type {arg}")

    def __str__(self):
        return f"{self._name} ({self._employee_type})"

    @classmethod
    def create(cls, name, employee_type):
        if employee_type == "engineer":
            return Engineer(name, "engineer")
        elif employee_type == "manager":
            return Manager(name, "manager")
        elif employee_type == "salesperson":
            return Salesperson(name, "salesman")
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
