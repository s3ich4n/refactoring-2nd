from src.case09.case09 import (
    base_rate,
    tax_threshold,
    acquire_reading,
    calculate_base_charge,
)


def test_base_rate():
    # 봄/가을, 여름, 겨울에 대한 테스트
    assert base_rate(5, 2017) == 0.7  # 봄
    assert base_rate(7, 2017) == 0.9  # 여름
    assert base_rate(1, 2017) == 0.8  # 겨울


def test_tax_threshold():
    assert tax_threshold(2016) == 50
    assert tax_threshold(2017) == 55
    assert tax_threshold(2018) == 60
    assert tax_threshold(2019) == 45  # 정의되지 않은 연도는 기본값 45 반환


def test_acquire_reading():
    reading = acquire_reading()
    assert reading["customer"] == "ivan"
    assert reading["quantity"] == 10
    assert reading["month"] == 5
    assert reading["year"] == 2017


def test_calculate_base_charge():
    reading = acquire_reading()
    expected = base_rate(reading["month"], reading["year"]) * reading["quantity"]
    assert calculate_base_charge(reading) == expected
    assert calculate_base_charge(reading) == 7.0  # 0.7 * 10 = 7.0


def test_taxable_charge():
    # 두 번째 예시의 과세 대상 요금 계산 테스트
    reading = acquire_reading()
    base = calculate_base_charge(reading)
    taxable_charge = max(0, base - tax_threshold(reading["year"]))
    assert taxable_charge == 0  # max(0, 7.0 - 55) = 0


def test_integration():
    # 통합 테스트: 전체 흐름 테스트
    reading = acquire_reading()

    # 첫 번째 예시
    base_charge_direct = (
        base_rate(reading["month"], reading["year"]) * reading["quantity"]
    )

    # 두 번째 예시
    base = base_rate(reading["month"], reading["year"]) * reading["quantity"]
    taxable_charge = max(0, base - tax_threshold(reading["year"]))

    # 세 번째 예시
    basic_charge_amount = calculate_base_charge(reading)

    # 모든 계산이 일치하는지 확인
    assert base_charge_direct == 7.0
    assert base == 7.0
    assert basic_charge_amount == 7.0
    assert taxable_charge == 0
