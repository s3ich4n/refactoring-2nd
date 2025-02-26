from dataclasses import dataclass


@dataclass
class Address:
    state: str


@dataclass
class Customer:
    address: Address


def in_new_england(a_customer):
    return a_customer.address.state in ["MA", "CT", "ME", "VT", "NH", "RI"]
