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
            return EuropianSwallowDelegate()
        elif data.name == "African Swallow":
            return AfricanSwallowDelegate(data)
        else:
            return None

    @property
    def name(self):
        return self._name

    @property
    def plumage(self):
        return self._plumage or "average"

    @property
    def air_speed_velocity(self):
        return (
            self._species_delegate.air_speed_velocity if self._species_delegate else 0
        )


class NorwegianBlueParrot(Bird):
    def __init__(self, data):
        super().__init__(data)
        self._voltage = data.voltage
        self._is_nailed = data.is_nailed

    @property
    def plumage(self):
        if self._voltage > 100:
            return "scorched"
        else:
            return "beautiful"

    @property
    def air_speed_velocity(self):
        if self._is_nailed:
            return 0
        else:
            return 10 + self._voltage / 10


class EuropianSwallowDelegate:
    @property
    def air_speed_velocity(self):
        return 35


class AfricanSwallowDelegate:
    def __init__(self, data):
        self._number_of_coconuts = data.number_of_coconuts

    @property
    def air_speed_velocity(self):
        return 40 - 2 * self._number_of_coconuts
