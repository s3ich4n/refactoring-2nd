from dataclasses import dataclass


def plumages(birds):
    return {b.name: plumage(b) for b in birds}


def speeds(birds):
    return {b.name: air_speed_velocity(b) for b in birds}


def create_bird(bird):
    if bird.type == "EuropeanSwallow":
        return EuropeanSwallow(bird)
    elif bird.type == "AfricanSwallow":
        return AfricanSwallow(bird)
    elif bird.type == "NorwegianBlueParrot":
        return NorwegianBlueParrot(bird)
    else:
        return Bird(bird)


def plumage(bird):
    return create_bird(bird).plumage()


def air_speed_velocity(bird):
    return create_bird(bird).air_speed_velocity()


@dataclass
class BirdData:
    name: str
    type: str
    number_of_coconuts: int = 0
    voltage: float = 0
    is_nailed: bool = False


class Bird:
    def __init__(self, name: BirdData):
        self.name = name

    def plumage(self):
        return "unknown"

    def air_speed_velocity(self):
        return None


class EuropeanSwallow(Bird):
    def plumage(self):
        return "average"

    def air_speed_velocity(self):
        return 35


class AfricanSwallow(Bird):
    def plumage(self):
        return "tired" if self.name.number_of_coconuts > 2 else "average"

    def air_speed_velocity(self):
        return 40 - 2 * self.name.number_of_coconuts


class NorwegianBlueParrot(Bird):
    def plumage(self):
        return "scorched" if self.name.voltage > 100 else "beautiful"

    def air_speed_velocity(self):
        return 0 if self.name.is_nailed else 10 + self.name.voltage / 10
