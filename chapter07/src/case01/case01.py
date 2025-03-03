class Organization:
    def __init__(self, data):
        self.data = data


# 임시로 이름 붙인 것
def get_raw_data_of_organization():
    return organization.data


def get_organization():
    return organization


# client 1
organization = Organization({"name": "Acme Gooseberries", "country": "GB"})
result = f"<h1>{get_organization().data['name']}</h1>"
get_organization().data["name"] = "new name"
