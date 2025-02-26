from src.case06.case06 import (
    Spaceship,
    Owner,
    get_owner,
    set_owner,
)


def test_access_data():
    space_ship = Spaceship(owner=get_owner())

    assert space_ship.owner.first_name == "Martin"
    assert space_ship.owner.last_name == "Fowler"


def test_modify_data():
    set_owner(Owner(first_name="Rebecca", last_name="Parsons"))

    assert get_owner().first_name == "Rebecca"
    assert get_owner().last_name == "Parsons"
