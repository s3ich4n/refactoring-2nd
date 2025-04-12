class Person:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
