def price_order(product, quantity, shipping_method):
    base_price = product["basePrice"] * quantity
    discount = (
        max(quantity - product["discountThreshold"], 0)
        * product["basePrice"]
        * product["discountRate"]
    )

    if base_price > shipping_method["discountThreshold"]:
        shipping_per_case = shipping_method["discountedFee"]
    else:
        shipping_per_case = shipping_method["feePerCase"]

    shipping_cost = quantity * shipping_per_case
    price = base_price - discount + shipping_cost

    return price
