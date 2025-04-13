class Employee:
    def __init__(self, name, type):
        self.validate_type(type)
        self._name = name
        self._type = type

    def validate_type(self, arg):
        if arg not in ["engineer", "manager", "salesman"]:
            raise ValueError(f"Employee cannot be of type {arg}")

    def __str__(self):
        return f"{self._name} ({self._type})"
