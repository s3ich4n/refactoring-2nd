from src.case10.case10 import (
    acquire_reading,
    enrich_reading,
)


def test_client3():
    raw_reading = acquire_reading()
    a_reading = enrich_reading(raw_reading)

    assert a_reading is not None


def test_client1():
    raw_reading = acquire_reading()
    a_reading = enrich_reading(raw_reading)
    assert a_reading.base_charge is not None


def test_client2():
    raw_reading = acquire_reading()
    a_reading = enrich_reading(raw_reading)

    assert a_reading.taxable_charge is not None
