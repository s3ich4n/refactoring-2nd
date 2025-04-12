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
        "base_price, discount_level, expected",
        [
            (1000, 1, 950),  # 할인 레벨 1: 5% 할인
            (1000, 2, 900),  # 할인 레벨 2: 10% 할인
            (1000, 3, 1000),  # 알 수 없는 할인 레벨: 할인 없음
        ],
    )
    def test_discounted_price(self, base_price, discount_level, expected):
        """
        할인된 가격 계산 테스트: 할인 레벨에 따른 가격 검증
        """
        order = Order(1, 1)  # 여기서는 quantity와 item_price가 중요하지 않음
        assert order.discounted_price(base_price, discount_level) == expected

    @pytest.mark.parametrize(
        "quantity, expected_level",
        [
            (1, 1),  # 최소 주문: 레벨 1
            (100, 1),  # 경계값 테스트 (100): 레벨 1
            (101, 2),  # 경계값 테스트 (101): 레벨 2
            (1000, 2),  # 대량 주문: 레벨 2
        ],
    )
    def test_discount_level(self, quantity, expected_level):
        """
        할인 레벨 결정 테스트: 주문 수량에 따른 할인 레벨 검증
        """
        order = Order(quantity, 1)  # item_price는 이 테스트에서 중요하지 않음
        # 내부 메소드지만 테스트를 위해 접근
        assert order._discount_level() == expected_level
