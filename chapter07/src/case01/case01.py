organization = {"name": "Acme Gooseberries", "country": "GB"}


# client 1
result = f"<h1>{organization['name']}</h1>"
organization["name"] = "new name"
