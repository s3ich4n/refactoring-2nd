# client 1
from src.case10.case10 import (
    enrich_reading,
    acquire_reading,
)

raw_reading = acquire_reading()
a_reading = enrich_reading(raw_reading)
base_charge = a_reading.base_charge
