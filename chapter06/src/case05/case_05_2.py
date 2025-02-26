from dataclasses import dataclass


@dataclass
class Address:
    state: str


@dataclass
class Customer:
    address: Address


def in_new_england(a_customer):
    return is_in_new_england(a_customer.address.state)


def is_in_new_england(state_code):
    return state_code in ["MA", "CT", "ME", "VT", "NH", "RI"]
