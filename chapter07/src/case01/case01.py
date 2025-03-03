class Organization:
    def __init__(self, data):
        self.name = data["name"]
        self.country = data["country"]


# client 1
organization = Organization({"name": "Acme Gooseberries", "country": "GB"})
result = f"<h1>{organization.name}</h1>"
organization.name = "new name"
