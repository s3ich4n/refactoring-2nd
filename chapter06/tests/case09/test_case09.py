from src.case09.case09 import (
    acquire_reading,
    Reading,
)


def test_integration():
    # 통합 테스트: 전체 흐름 테스트
    raw_reading = acquire_reading()
    reading = Reading(**raw_reading)

    # 첫 번째 예시
    base_charge_direct = reading.base_charge()

    # 두 번째 예시
    base = reading.base_rate() * reading.quantity
    taxable_charge = reading.taxable_charge()

    # 세 번째 예시
    basic_charge_amount = reading.base_charge()

    # 모든 계산이 일치하는지 확인
    assert base_charge_direct == 7.0
    assert base == 7.0
    assert basic_charge_amount == 7.0
    assert taxable_charge == 0
