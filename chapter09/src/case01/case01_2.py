def discount(input_value, quantity):
    result = input_value
    if input_value > 50:
        result = result - 2
    if quantity > 100:
        result = result - 1
    return result
