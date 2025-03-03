class CustomerData:
    def __init__(self, data):
        self._data = data

    # example (1) - write
    def set_usage(self, customer_id, year, month, amount):
        get_customer_data()[customer_id]["usages"][year][month] = amount


def get_customer_data():
    return customer_data


def get_raw_data_of_customers():
    return customer_data._data


def set_raw_data_of_customers(arg):
    customer_data = CustomerData(arg)


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


# example (2) - read
def compare_usage(customer_id, later_year, month):
    later = get_customer_data()[customer_id]["usages"][later_year][month]
    earlier = get_customer_data()[customer_id]["usages"][f"{int(later_year) - 1}"][
        month
    ]

    return {
        "later_amount": later,
        "change": later - earlier,
    }
