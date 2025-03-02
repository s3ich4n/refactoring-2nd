# client 3
from src.case10.case10 import (
    acquire_reading,
    enrich_reading,
)

raw_reading = acquire_reading()
a_reading = enrich_reading(raw_reading)
basic_charge_amount = a_reading.base_charge
