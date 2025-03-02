def price_order(product, quantity, shipping_method):
    base_price = product["basePrice"] * quantity
    discount = (
        max(quantity - product["discountThreshold"], 0)
        * product["basePrice"]
        * product["discountRate"]
    )

    price_data = {"base_price": base_price, "quantity": quantity, "discount": discount}

    price = apply_shipping(price_data, shipping_method)

    return price


def apply_shipping(price_data, shipping_method):
    if price_data["base_price"] > shipping_method["discountThreshold"]:
        shipping_per_case = shipping_method["discountedFee"]
    else:
        shipping_per_case = shipping_method["feePerCase"]
    shipping_cost = price_data["quantity"] * shipping_per_case
    price = price_data["base_price"] - price_data["discount"] + shipping_cost

    return price
