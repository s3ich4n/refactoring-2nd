def price_order(product, quantity, shipping_method):
    price_data = calculate_pricing_data(product, quantity)
    return apply_shipping(price_data, shipping_method)


def calculate_pricing_data(product, quantity):
    base_price = product["base_price"] * quantity
    discount = (
        max(quantity - product["discount_threshold"], 0)
        * product["base_price"]
        * product["discount_rate"]
    )
    return {"base_price": base_price, "quantity": quantity, "discount": discount}


def apply_shipping(price_data, shipping_method):
    if price_data["base_price"] > shipping_method["discount_threshold"]:
        shipping_per_case = shipping_method["discounted_fee"]
    else:
        shipping_per_case = shipping_method["fee_per_case"]
    shipping_cost = price_data["quantity"] * shipping_per_case

    return price_data["base_price"] - price_data["discount"] + shipping_cost
