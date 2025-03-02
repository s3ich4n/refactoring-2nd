import pytest

from src.case11.case11 import price_order


@pytest.mark.parametrize(
    "product, quantity, shipping_method, expected_price",
    [
        (
            {"basePrice": 100, "discountThreshold": 10, "discountRate": 0.1},
            5,
            {"discountThreshold": 1000, "discountedFee": 30, "feePerCase": 50},
            5 * 100 + 5 * 50,  # 할인 없음, 기본 배송비 적용
        ),
        (
            {"basePrice": 100, "discountThreshold": 10, "discountRate": 0.1},
            5,
            {"discountThreshold": 1000, "discountedFee": 30, "feePerCase": 50},
            5 * 100 + 5 * 50,  # 할인 없음, 기본 배송비
        ),
        (
            {"basePrice": 100, "discountThreshold": 10, "discountRate": 0.1},
            15,
            {"discountThreshold": 1000, "discountedFee": 30, "feePerCase": 50},
            15 * 100 - 5 * 100 * 0.1 + 15 * 30,  # 할인 적용, 할인된 배송비 적용
        ),
        (
            {"basePrice": 100, "discountThreshold": 10, "discountRate": 0.1},
            20,
            {"discountThreshold": 1000, "discountedFee": 30, "feePerCase": 50},
            20 * 100 - 10 * 100 * 0.1 + 20 * 30,  # 할인 적용, 할인된 배송비 적용
        ),
        (
            {"basePrice": 100, "discountThreshold": 10, "discountRate": 0.1},
            50,
            {"discountThreshold": 1000, "discountedFee": 30, "feePerCase": 50},
            50 * 100 - 40 * 100 * 0.1 + 50 * 30,  # 할인 적용, 할인된 배송비 적용
        ),
    ],
)
def test_price_order(product, quantity, shipping_method, expected_price):
    result = price_order(product, quantity, shipping_method)
    assert result == expected_price
