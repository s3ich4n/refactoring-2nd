class Employee:
    def __init__(self, name, employee_type):
        self.validate_type(employee_type)
        self._name = name
        self._employee_type = employee_type

    def validate_type(self, arg):
        if arg not in ["engineer", "manager", "salesman"]:
            raise ValueError(f"Employee cannot be of type {arg}")

    @property
    def employee_type(self):
        return self._employee_type

    def __str__(self):
        return f"{self._name} ({self._employee_type})"
