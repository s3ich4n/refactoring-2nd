# client 2
from src.case10.case10 import (
    acquire_reading,
    enrich_reading,
    tax_threshold,
)

raw_reading = acquire_reading()
a_reading = enrich_reading(raw_reading)
base_charge = a_reading.base_charge
taxable_charge = max(0, a_reading.base_charge - tax_threshold(a_reading.year))
