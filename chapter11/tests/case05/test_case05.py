import pytest

from chapter11.src.case05.case05 import Order


class TestOrder:
    """
    Order 클래스를 테스트하는 클래스
    """

    @pytest.mark.parametrize(
        "quantity, item_price, expected",
        [
            (10, 100, 950),  # 소량 주문: 5% 할인
            (50, 20, 950),  # 중간 주문: 5% 할인
            (100, 10, 950),  # 경계값 테스트 (100): 5% 할인
            (101, 10, 909),  # 경계값 테스트 (101): 10% 할인
            (200, 5, 900),  # 대량 주문: 10% 할인
            (1000, 1, 900),  # 매우 대량 주문: 10% 할인
        ],
    )
    def test_final_price(self, quantity, item_price, expected):
        """
        최종 가격 계산 테스트: 주문 수량과 가격에 따른 할인율 적용 검증
        """
        order = Order(quantity, item_price)
        assert order.final_price() == expected

    @pytest.mark.parametrize(
        "quantity, base_price, expected",
        [
            (50, 1000, 950),   # 소량 주문(100 이하): 5% 할인
            (100, 1000, 950),  # 경계값 테스트 (100): 5% 할인
            (101, 1000, 900),  # 경계값 테스트 (101): 10% 할인
            (200, 1000, 900),  # 대량 주문: 10% 할인
        ],
    )
    def test_discounted_price(self, quantity, base_price, expected):
        """
        할인된 가격 계산 테스트: 주문 수량에 따른 할인율 적용 검증
        """
        order = Order(quantity, 1)  # item_price는 이 테스트에서 중요하지 않음
        assert order.discounted_price(base_price) == expected
