import pytest

from chapter11.src.case07.case07 import Person


def test_user_create():
    a = Person(user_id=1, name="<NAME>")

    assert a.user_id == 1
    assert a.name == "<NAME>"

    with pytest.raises(AttributeError):
        a.user_id = 2
