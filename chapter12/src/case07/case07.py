from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    gender: str
    name: str | None


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def gender_code(self):
        return "X"

    @classmethod
    def create_person(cls, name):
        return cls(name)

    @staticmethod
    def is_male(other):
        return isinstance(other, Male)


class Male(Person):
    @property
    def gender_code(self):
        return "M"

    @classmethod
    def create_male(cls, name):
        return cls(name)


class Female(Person):
    @property
    def gender_code(self):
        return "F"

    @classmethod
    def create_female(cls, name):
        return cls(name)


def load_from_input(data):
    """데이터 리스트에서 Person 객체 리스트를 생성합니다."""
    result = []
    number_of_males = 0
    for record in data:
        if record.is_male():
            number_of_males += 1
        result.append(create_person(record))
    return result


def create_person(user: User):
    if user.gender == "M":
        return Male.create_male(user.name)
    elif user.gender == "F":
        return Female.create_female(user.name)
    else:
        return Person.create_person(user.name)
