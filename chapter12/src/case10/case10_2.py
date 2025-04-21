from dataclasses import dataclass


@dataclass
class BirdData:
    name: str
    plumage: str
    number_of_coconuts: int = 0
    voltage: float = 0
    is_nailed: bool = False


class Bird:
    def __init__(self, data):
        self._name = data.name
        self._plumage = data.plumage
        self._species_delegate = self.select_species_delegate(data)

    def select_species_delegate(self, data):
        if data.name == "European Swallow":
            return EuropianSwallowDelegate(data, self)
        elif data.name == "African Swallow":
            return AfricanSwallowDelegate(data, self)
        elif data.name == "Norwegian Blue":
            return NorwegianBlueParrotDelegate(data, self)
        else:
            return SpeciesDelegate(data, self)

    @classmethod
    def create(cls, data):
        return cls(data)

    @property
    def name(self):
        return self._name

    @property
    def plumage(self):
        return self._species_delegate.plumage

    @property
    def air_speed_velocity(self):
        return self._species_delegate.air_speed_velocity


class SpeciesDelegate:
    """이러면 - 뭐가 위임되었고 뭐가 남겨졌는지 파악하기 쉽다!"""

    def __init__(self, data, bird):
        self._bird = bird

    @property
    def plumage(self):
        return self._bird._plumage or "average"

    @property
    def air_speed_velocity(self):
        return None


class NorwegianBlueParrot(Bird):
    def __init__(self, data):
        super().__init__(data)
        self._voltage = data.voltage
        self._is_nailed = data.is_nailed

    @property
    def plumage(self):
        return self._species_delegate.plumage


class EuropianSwallowDelegate(SpeciesDelegate):
    @property
    def air_speed_velocity(self):
        return 35


class AfricanSwallowDelegate(SpeciesDelegate):
    def __init__(self, data, bird):
        super().__init__(data, bird)
        self._number_of_coconuts = data.number_of_coconuts

    @property
    def air_speed_velocity(self):
        return 40 - 2 * self._number_of_coconuts


class NorwegianBlueParrotDelegate(SpeciesDelegate):
    def __init__(self, data, bird):
        super().__init__(data, bird)
        self._voltage = data.voltage
        self._is_nailed = data.is_nailed

    @property
    def air_speed_velocity(self):
        if self._is_nailed:
            return 0
        else:
            return 10 + self._voltage / 10

    @property
    def plumage(self):
        if self._voltage > 100:
            return "scorched"
        else:
            return self._bird._plumage or "beautiful"
