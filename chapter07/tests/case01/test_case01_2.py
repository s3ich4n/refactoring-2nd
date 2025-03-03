from src.case01.case01_2 import (
    compare_usage,
    customer_data,
    CustomerData,
    raw_data,
)


def test_set_usage():
    data = CustomerData(raw_data)
    data.set_usage("1920", "2016", "3", 60)
    assert data._data["1920"]["usages"]["2016"]["3"] == 60


def test_compare_usage():
    result = compare_usage("1920", "2016", "1")
    assert result["later_amount"] == 50
    assert result["change"] == -20

    result = compare_usage("1920", "2016", "2")
    assert result["later_amount"] == 55
    assert result["change"] == -8
