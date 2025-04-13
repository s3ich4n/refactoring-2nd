class Employee:
    def __init__(self, name, type):
        self.validate_type(type)
        self._name = name
        self._type = type

    def validate_type(self, arg):
        if arg not in ["engineer", "manager", "salesman"]:
            raise ValueError(f"Employee cannot be of type {arg}")

    @property
    def type_string(self):
        return str(self._type)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, arg):
        self._type = Employee.create_employee_type(arg)

    @property
    def capitalized_type(self):
        return self.type_string.capitalize()

    @classmethod
    def create_employee_type(cls, employee_type):
        if employee_type == "engineer":
            return Engineer()
        elif employee_type == "manager":
            return Manager()
        elif employee_type == "salesperson":
            return Salesperson()
        else:
            raise NotImplementedError(f"Employee cannot be of type {employee_type}")

    def __str__(self):
        return f"{self._name} ({self.capitalized_type})"


class EmployeeType:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self._value


class Engineer(EmployeeType):
    def __str__(self):
        return "engineer"


class Manager(EmployeeType):
    def __str__(self):
        return "manager"


class Salesperson(EmployeeType):
    def __str__(self):
        return "salesperson"
