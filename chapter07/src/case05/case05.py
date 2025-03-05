class Person:
    def __init__(self, telephone_number):
        self._telephone_number = telephone_number

    @property
    def office_area_code(self):
        return self._office_area_code

    @property
    def office_number(self):
        return self._office_number


class TelephoneNumber:
    def __init__(self, area_code):
        self._area_code = area_code

    @property
    def area_code(self):
        return self._area_code
