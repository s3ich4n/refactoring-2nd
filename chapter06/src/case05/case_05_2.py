from dataclasses import dataclass


@dataclass
class Address:
    state: str


@dataclass
class Customer:
    address: Address


def in_new_england(a_customer):
    state_code = a_customer.address.state
    return state_code in ["MA", "CT", "ME", "VT", "NH", "RI"]
