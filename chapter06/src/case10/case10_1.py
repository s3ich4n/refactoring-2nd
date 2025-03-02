# client 1
a_reading = acquire_reading()
base_charge = base_rate(a_reading.month, a_reading.year) * a_reading.quantity
