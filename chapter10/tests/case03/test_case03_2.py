from chapter10.src.case03.case03_2 import (
    Instrument,
    adjusted_capital,
)


def test_adjusted_capital_all_positive():
    # 모든 값이 양수인 경우
    instrument = Instrument(
        capital=1000.0,
        interest_rate=0.05,
        duration=12.0,
        income=120.0,
        adjustment=1.5,
    )
    expected = (120.0 / 12.0) * 1.5  # 15.0
    assert adjusted_capital(instrument) == expected


def test_adjusted_capital_zero_capital():
    # capital이 0인 경우
    instrument = Instrument(
        capital=0.0,
        interest_rate=0.05,
        duration=12.0,
        income=120.0,
        adjustment=1.5,
    )
    assert adjusted_capital(instrument) == 0


def test_adjusted_capital_zero_interest_rate():
    # interest_rate가 0인 경우
    instrument = Instrument(
        capital=1000.0,
        interest_rate=0.0,
        duration=12.0,
        income=120.0,
        adjustment=1.5,
    )
    assert adjusted_capital(instrument) == 0


def test_adjusted_capital_zero_duration():
    # duration이 0인 경우
    instrument = Instrument(
        capital=1000.0,
        interest_rate=0.05,
        duration=0.0,
        income=120.0,
        adjustment=1.5,
    )
    assert adjusted_capital(instrument) == 0
