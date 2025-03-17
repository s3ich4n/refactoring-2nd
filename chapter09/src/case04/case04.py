class TelephoneNumber:
    def __init__(self, area_code, number):
        self._area_code = area_code
        self._number = number

    def __eq__(self, other):
        return self._area_code == other._area_code and self._number == other._number

    def __hash__(self):
        return hash((self._area_code, self._number))

    @property
    def area_code(self):
        return self._area_code

    @property
    def number(self):
        return self._number


class Person:
    def __init__(self):
        self._telephone_number = TelephoneNumber("", "")

    @property
    def office_area_code(self):
        return self._telephone_number.area_code

    @office_area_code.setter
    def office_area_code(self, arg):
        self._telephone_number = TelephoneNumber(arg, self.office_number)

    @property
    def office_number(self):
        return self._telephone_number.number

    @office_number.setter
    def office_number(self, arg):
        self._telephone_number = TelephoneNumber(self.office_area_code, arg)
