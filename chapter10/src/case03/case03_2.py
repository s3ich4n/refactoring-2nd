from dataclasses import dataclass


@dataclass
class Instrument:
    capital: float = 0.0
    interest_rate: float = 0.0
    duration: float = 0.0
    income: float = 0.0
    adjustment: float = 0.0  # 이 속성명은 원본 코드에서 잘렸을 가능성이 있습니다


def adjusted_capital(an_instrument: Instrument):
    result = 0
    if an_instrument.capital <= 0:
        return result

    if not (an_instrument.interest_rate > 0 and an_instrument.duration > 0):
        return result

    result = (an_instrument.income / an_instrument.duration) * an_instrument.adjustment
    return result
