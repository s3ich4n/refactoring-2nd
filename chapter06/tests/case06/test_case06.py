from chapter06.src.case06.case06 import (
    default_owner,
    Spaceship,
)


def test_access_data():
    space_ship = Spaceship(owner=default_owner)

    assert space_ship.owner == default_owner


def test_modify_data():
    default_owner = {"first_name": "Rebecca", "last_name": "Parsons"}

    assert default_owner["first_name"] == "Rebecca"
    assert default_owner["last_name"] == "Parsons"
