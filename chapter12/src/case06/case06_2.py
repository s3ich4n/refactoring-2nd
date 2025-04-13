class Employee:
    def __init__(self, name, type):
        self._name = name
        self._type = self.create_employee_type(type)
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, arg):
        self._type = self.create_employee_type(arg)
    
    @property
    def capitalized_type(self):
        return str(self._type).capitalize()
    
    @staticmethod
    def create_employee_type(type_code):
        if type_code == "engineer":
            return Engineer()
        elif type_code == "manager":
            return Manager()
        elif type_code == "salesman":
            return Salesman()
        else:
            raise ValueError(f"Employee cannot be of type {type_code}")
    
    def __str__(self):
        return f"{self._name} ({self.capitalized_type})"


class EmployeeType:
    def __str__(self):
        raise NotImplementedError("Subclasses must implement __str__ method")


class Engineer(EmployeeType):
    def __str__(self):
        return "engineer"


class Manager(EmployeeType):
    def __str__(self):
        return "manager"


class Salesman(EmployeeType):
    def __str__(self):
        return "salesman"
