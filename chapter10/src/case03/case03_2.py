from dataclasses import dataclass


@dataclass
class Instrument:
    capital: float = 0.0
    interest_rate: float = 0.0
    duration: float = 0.0
    income: float = 0.0
    adjustment: float = 0.0


def adjusted_capital(an_instrument: Instrument):
    if (
        an_instrument.capital <= 0
        or an_instrument.interest_rate <= 0
        or an_instrument.duration <= 0
    ):
        return 0

    result = (an_instrument.income / an_instrument.duration) * an_instrument.adjustment
    return result
