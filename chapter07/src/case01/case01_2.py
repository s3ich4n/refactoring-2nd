customer_data = {
    "1920": {
        "name": "martin",
        "id": "1920",
        "usages": {
            "2016": {
                "1": 50,
                "2": 55,
                # remaining months of the year
            },
            "2015": {
                "1": 70,
                "2": 63,
                # remaining months of the year
            },
        },
    },
    "38673": {
        "name": "neal",
        "id": "38673",
        # more customers in a similar form
    },
}


# example (1) - write
def set_usage(customer_id, year, month, amount):
    customer_data[customer_id]["usages"][year][month] = amount


# example (2) - read
def compare_usage(customer_id, later_year, month):
    later = customer_data[customer_id]["usages"][later_year][month]
    earlier = customer_data[customer_id]["usages"][f"{int(later_year) - 1}"][month]

    return {
        "later_amount": later,
        "change": later - earlier,
    }
