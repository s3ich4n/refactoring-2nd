from dataclasses import dataclass


@dataclass
class BirdData:
    name: str
    plumage: str
    voltage: float = 0
    is_nailed: bool = False


class Bird:
    def __init__(self, data):
        self._name = data.name
        self._plumage = data.plumage

    @property
    def name(self):
        return self._name

    @property
    def plumage(self):
        return self._plumage or "average"


class EuropeanSwallow(Bird):
    @property
    def air_speed_velocity(self):
        return 35


class AfricanSwallow(Bird):
    def __init__(self, data, number_of_coconuts):
        super().__init__(data)
        self._number_of_coconuts = number_of_coconuts

    @property
    def air_speed_velocity(self):
        return 40 - 2 * self._number_of_coconuts


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
