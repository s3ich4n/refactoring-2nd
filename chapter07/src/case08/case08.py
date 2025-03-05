# organization.py


class Person:
    def __init__(self, name, department):
        self._name = name
        self._department = department

    @property
    def name(self):
        return self._name

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, arg):
        self._department = arg


class Department:
    def __init__(self):
        self._charge_code = None
        self._manager = None

    @property
    def charge_code(self):
        return self._charge_code

    @charge_code.setter
    def charge_code(self, arg):
        self._charge_code = arg

    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, arg):
        self._manager = arg
