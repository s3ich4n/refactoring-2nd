from chapter06.src.case06.case06 import (
    Spaceship,
    manager,
)


def test_access_data():
    space_ship = Spaceship(owner=manager.owner)

    assert space_ship.owner["first_name"] == "Martin"
    assert space_ship.owner["last_name"] == "Fowler"


def test_modify_data():
    manager.owner = {"first_name": "Rebecca", "last_name": "Parsons"}

    assert manager.owner["first_name"] == "Rebecca"
    assert manager.owner["last_name"] == "Parsons"
