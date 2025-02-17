import pytest

from chapter04.src.province import Province


@pytest.fixture(
    name="asia",
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


def test_sample_province_data(asia):
    assert Province(asia)


def test_province_shortfall(asia):
    asia = Province(asia)
    assert asia.shortfall == 5

def test_province_profit(asia):
    asia = Province(asia)
    assert asia.profit == 230

def test_change_production(asia):
    asia = Province(asia)
    asia.producers[0].production = 20

    assert asia.shortfall == -6
    assert asia.profit == 292

def test_province_with_no_producers():
    data = {
        "name": "Asia",
        "producers": [],
        "demand": 30,
        "price": 20
    }

    no_producers = Province(data)

    assert no_producers.shortfall == 30
    assert no_producers.profit == 0

def test_province_with_zero_demand(asia):
    asia = Province(asia)
    asia.demand = 0

    assert asia.shortfall == -25
    assert asia.profit == 0


def test_province_with_negative_demand(asia):
    asia = Province(asia)
    asia.demand = -1

    assert asia.shortfall == -26
    assert asia.profit == -10


def test_province_with_empty_demand(asia):
    asia = Province(asia)

    with pytest.raises(ValueError):
        asia.demand = ""

    # asia.demand에 문자열을 넣는 행위가 Exception이 터지므로
    # 허용하지 않는다. (i.e., NaN 케이스가 없음)

def test_province_with_invalid_producers():
    data = {
        "name": "Asia",
        "producers": " ",    # 아예 안맞는 값을 넣으면?
        "demand": 30,
        "price": 20
    }

    # 반복문을 정상으로 판단함(str도 Sequence니까 iterable함)
    # 그리고 빈 문자열을 `Producer` 객체에 넣으려다보니 터짐
    with pytest.raises(AttributeError):
        assert Province(data)
