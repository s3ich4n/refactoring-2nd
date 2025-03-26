from dataclasses import dataclass


def plumages(birds):
    return {b.name: plumage(b) for b in birds}


def speeds(birds):
    return {b.name: air_speed_velocity(b) for b in birds}


def plumage(bird):
    if bird.type == "EuropeanSwallow":
        return "average"
    elif bird.type == "AfricanSwallow":
        return "tired" if bird.number_of_coconuts > 2 else "average"
    elif bird.type == "NorwegianBlueParrot":
        return "scorched" if bird.voltage > 100 else "beautiful"
    else:
        return "unknown"


def air_speed_velocity(bird):
    if bird.type == "EuropeanSwallow":
        return 35
    elif bird.type == "AfricanSwallow":
        return 40 - 2 * bird.number_of_coconuts
    elif bird.type == "NorwegianBlueParrot":
        return 0 if bird.is_nailed else 10 + bird.voltage / 10
    else:
        return None


@dataclass
class Bird:
    name: str
    type: str
    number_of_coconuts: int = 0
    voltage: float = 0
    is_nailed: bool = False
