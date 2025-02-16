from chapter04.src.province import Province


def test_sample_province_data():
    test_data = {
        "name": "Asia",
        "producers": [
            {"name": "Byzantium", "cost": 10, "production": 9},
            {"name": "Attalia", "cost": 12, "production": 10},
            {"name": "Sinope", "cost": 10, "production": 6},
        ],
        "demand": 30,
        "price": 20,
    }

    assert Province(test_data)
