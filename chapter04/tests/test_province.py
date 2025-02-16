import pytest

from chapter04.src.province import Province


@pytest.fixture(
    name="test_data",
    scope="function",   # beforeEach 효과를 주려면
)
def sample_province_data():
    return {
        "name": "Asia",
        "producers": [
            {"name": "Byzantium", "cost": 10, "production": 9},
            {"name": "Attalia", "cost": 12, "production": 10},
            {"name": "Sinope", "cost": 10, "production": 6},
        ],
        "demand": 30,
        "price": 20,
    }


def test_sample_province_data(test_data):
    assert Province(test_data)


def test_province_shortfall(test_data):
    asia = Province(test_data)
    assert asia.shortfall == 5

def test_province_profit(test_data):
    asia = Province(test_data)
    assert asia.profit == 230
