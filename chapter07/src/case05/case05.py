class Person:
    def __init__(self, telephone_number):
        self._telephone_number = telephone_number

    @property
    def office_area_code(self):
        return self._telephone_number.area_code

    @property
    def office_number(self):
        return self._telephone_number.number

    @property
    def telephone_number(self):
        return str(self._telephone_number)


class TelephoneNumber:
    def __init__(self, area_code, office_number):
        self._area_code = area_code
        self._number = office_number

    def __str__(self):
        return f"({self.area_code}) {self.number}"

    @property
    def area_code(self):
        return self._area_code

    @property
    def number(self):
        return self._number
