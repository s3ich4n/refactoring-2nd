from dataclasses import dataclass


@dataclass
class Spaceship:
    owner: dict


default_owner = {"first_name": "Martin", "last_name": "Fowler"}
