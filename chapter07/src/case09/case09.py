def found_person_old(people):
    for person in people:
        if person == "Don":
            return "Don"
        if person == "John":
            return "John"
        if person == "Kent":
            return "Kent"
    return ""


def found_person_new(people):
    """
    Return the first name from people that appears in the list of candidates,
    or an empty string if none are found.

    Notes:
        - This function uses a generator expression (p for p in people if p in candidates)
          to iterate over 'people'.
        - The built-in `next()` function retrieves **the first match** from that generator.
        - If no match is found, the default value "" is returned.
    """
    candidates = ["Don", "John", "Kent"]
    return next((p for p in people if p in candidates), "")
