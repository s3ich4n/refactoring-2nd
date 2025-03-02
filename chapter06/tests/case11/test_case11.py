import pytest

from src.case11.case11 import price_order


@pytest.mark.parametrize(
    "product, quantity, shipping_method, expected_price",
    [
        (
            {"base_price": 100, "discount_threshold": 10, "discount_rate": 0.1},
            5,
            {"discount_threshold": 1000, "discounted_fee": 30, "fee_per_case": 50},
            5 * 100 + 5 * 50,  # 할인 없음, 기본 배송비 적용
        ),
        (
            {"base_price": 100, "discount_threshold": 10, "discount_rate": 0.1},
            5,
            {"discount_threshold": 1000, "discounted_fee": 30, "fee_per_case": 50},
            5 * 100 + 5 * 50,  # 할인 없음, 기본 배송비
        ),
        (
            {"base_price": 100, "discount_threshold": 10, "discount_rate": 0.1},
            15,
            {"discount_threshold": 1000, "discounted_fee": 30, "fee_per_case": 50},
            15 * 100 - 5 * 100 * 0.1 + 15 * 30,  # 할인 적용, 할인된 배송비 적용
        ),
        (
            {"base_price": 100, "discount_threshold": 10, "discount_rate": 0.1},
            20,
            {"discount_threshold": 1000, "discounted_fee": 30, "fee_per_case": 50},
            20 * 100 - 10 * 100 * 0.1 + 20 * 30,  # 할인 적용, 할인된 배송비 적용
        ),
        (
            {"base_price": 100, "discount_threshold": 10, "discount_rate": 0.1},
            50,
            {"discount_threshold": 1000, "discounted_fee": 30, "fee_per_case": 50},
            50 * 100 - 40 * 100 * 0.1 + 50 * 30,  # 할인 적용, 할인된 배송비 적용
        ),
    ],
)
def test_price_order(product, quantity, shipping_method, expected_price):
    result = price_order(product, quantity, shipping_method)
    assert result == expected_price
