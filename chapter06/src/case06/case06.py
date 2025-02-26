from dataclasses import dataclass


@dataclass
class Spaceship:
    owner: dict


class DefaultOwnerManager:
    def __init__(self):
        self._owner = {"first_name": "Martin", "last_name": "Fowler"}

    @property
    def owner(self):
        return self._owner.copy()

    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner


manager = DefaultOwnerManager()
