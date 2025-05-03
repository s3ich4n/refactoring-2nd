def acquire_data(input):
    lines = input.split("\n")
    return [
        {"city": fields[0].strip(), "phone": fields[2].strip()}
        for fields in (line.split(",") for line in lines[1:] if line.strip() != "")
        if fields[1].strip() == "India"
    ]
