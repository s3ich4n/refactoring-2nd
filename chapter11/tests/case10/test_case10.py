from unittest.mock import MagicMock

from chapter11.src.case10.case10 import ChargeCalculator


class TestChargeCalculator:
    def test_charge(self):
        # 테스트를 위한 Mock 객체 설정
        customer = MagicMock()
        customer.base_rate = 10.0

        usage = 5.0

        provider = MagicMock()
        provider.connection_charge = 15.0

        # ChargeCalculator 인스턴스 생성
        calculator = ChargeCalculator(customer, usage, provider)

        # 총 요금 계산 테스트
        assert calculator.charge == 65.0  # (10.0 * 5.0) + 15.0

    def test_with_different_values(self):
        # 다른 값으로 테스트
        customer = MagicMock()
        customer.base_rate = 7.5

        usage = 8.0

        provider = MagicMock()
        provider.connection_charge = 20.0

        # ChargeCalculator 인스턴스 생성
        calculator = ChargeCalculator(customer, usage, provider)

        # 총 요금 계산 테스트
        assert calculator.charge == 80.0  # (7.5 * 8.0) + 20.0
