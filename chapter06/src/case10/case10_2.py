# client 2
a_reading = acquire_reading()
base_charge = base_rate(a_reading.month, a_reading.year) * a_reading.quantity
taxable_charge = max(0, base - tax_threshold(a_reading.year))
