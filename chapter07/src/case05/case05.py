class Person:
    def __init__(self, office_area_code, office_number):
        self._office_area_code = office_area_code
        self._office_number = office_number

    @property
    def office_area_code(self):
        return self._office_area_code

    @property
    def office_number(self):
        return self._office_number
