customer_data = {}

# example (1) - write
customer_data["customer_id"]["usages"]["year"]["month"] = amount


# example (2) - read
def compare_usage(customer_id, later_year, month):
    later = customer_data[customer_id]["usages"][later_year][month]
    earlier = customer_data[customer_id]["usages"][later_year - 1][month]

    return {
        "later_amount": later,
        "change": later - earlier,
    }
