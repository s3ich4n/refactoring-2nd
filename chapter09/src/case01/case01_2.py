def discount(input_value, quantity):
    if input_value > 50:
        input_value = input_value - 2
    if quantity > 100:
        input_value = input_value - 1
    return input_value
