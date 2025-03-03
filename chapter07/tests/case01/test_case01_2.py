from copy import deepcopy

import pytest
from src.case01.case01_2 import (
    compare_usage,
    get_customer_data,
    initialize_data,
    CustomerData,
    raw_data,
)


# 각 테스트 전에 깨끗한 데이터로 시작
@pytest.fixture
def setup_data():
    test_data = deepcopy(raw_data)
    initialize_data(test_data)
    return test_data


def test_set_usage(setup_data):
    # CustomerData 객체의 메서드 테스트
    customer_data = get_customer_data()
    customer_data.set_usage("1920", "2016", "3", 60)
    assert customer_data.usage("1920", "2016", "3") == 60


def test_usage_method(setup_data):
    # usage 메서드 테스트
    customer_data = get_customer_data()
    assert customer_data.usage("1920", "2016", "1") == 50
    assert customer_data.usage("1920", "2015", "1") == 70


def test_compare_usage(setup_data):
    # 전역 함수 테스트
    result = compare_usage("1920", "2016", "1")
    assert result["later_amount"] == 50
    assert result["change"] == -20

    result = compare_usage("1920", "2016", "2")
    assert result["later_amount"] == 55
    assert result["change"] == -8


def test_compare_usage_method(setup_data):
    # 클래스 메서드 직접 테스트
    customer_data = get_customer_data()
    result = customer_data.compare_usage("1920", "2016", "1")
    assert result["later_amount"] == 50
    assert result["change"] == -20
