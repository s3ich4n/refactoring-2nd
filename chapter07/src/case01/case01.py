organization = {"name": "Acme Gooseberries", "country": "GB"}


# 임시로 이름 붙인 것
def get_raw_data_of_organization():
    return organization


# client 1
result = f"<h1>{get_raw_data_of_organization()['name']}</h1>"
get_raw_data_of_organization()["name"] = "new name"
