from dataclasses import dataclass


@dataclass(frozen=True)
class Driver:
    number_of_late_deliveries: int


def rating(driver):
    return 2 if driver.number_of_late_deliveries > 5 else 1
