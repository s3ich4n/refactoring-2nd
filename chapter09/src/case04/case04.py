class TelephoneNumber:
    def __init__(self):
        self._area_code = None
        self._number = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, arg):
        self._area_code = arg

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, arg):
        self._number = arg


class Person:
    def __init__(self):
        self._telephone_number = TelephoneNumber()

    @property
    def office_area_code(self):
        return self._telephone_number.area_code

    @office_area_code.setter
    def office_area_code(self, arg):
        self._telephone_number.area_code = arg

    @property
    def office_number(self):
        return self._telephone_number.number

    @office_number.setter
    def office_number(self, arg):
        self._telephone_number.number = arg
