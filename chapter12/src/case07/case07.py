from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    gender: str
    name: str | None


class Person:
    def __init__(
        self,
        name,
        gender_code,
    ):
        self._name = name
        self._gender_code = gender_code

    @property
    def name(self):
        return self._name

    @property
    def gender_code(self):
        return self._gender_code

    @classmethod
    def create_person(
        cls,
        name,
        gender_code: str = "X",
    ):
        return cls(name, gender_code)

    def is_male(self):
        return isinstance(self, Male)


class Male(Person):
    @property
    def gender_code(self):
        return self._gender_code


class Female(Person):
    @property
    def gender_code(self):
        return "F"


def load_from_input(data):
    """데이터 리스트에서 Person 객체 리스트를 생성합니다."""
    result = []
    number_of_males = 0
    for record in data:
        queried = create_person(record)
        if queried.is_male():
            number_of_males += 1
        result.append(queried)
    return result


def create_person(user: User):
    if user.gender == "M":
        return Person.create_person(user.name, "M")
    elif user.gender == "F":
        return Person.create_person(user.name, "F")
    else:
        return Person.create_person(user.name)
