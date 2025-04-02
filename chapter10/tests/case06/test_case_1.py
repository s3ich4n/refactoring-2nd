from chapter10.src.case06.case_06_1 import Customer


def test_apply_discount_with_valid_discount_rate():
    # 정상적인 할인율 테스트
    customer = Customer(0.1)  # 10% 할인
    result = customer.apply_discount(100)
    assert result == 90

    customer = Customer(0.5)  # 50% 할인
    result = customer.apply_discount(100)
    assert result == 50


def test_apply_discount_with_zero_discount_rate():
    # 할인율이 0인 경우 테스트
    customer = Customer(0)
    result = customer.apply_discount(100)
    assert result == 100


def test_apply_discount_with_none_discount_rate():
    # 할인율이 None인 경우 테스트
    customer = Customer(None)
    result = customer.apply_discount(100)
    assert result == 100


def test_apply_discount_with_negative_discount_rate():
    # 음수 할인율 테스트 (가격 인상 효과)
    customer = Customer(-0.1)  # -10% 할인 (즉, 10% 인상)
    result = customer.apply_discount(100)
    assert result == 110


def test_apply_discount_with_full_discount_rate():
    # 100% 할인 테스트
    customer = Customer(1.0)
    result = customer.apply_discount(100)
    assert result == 0


def test_apply_discount_with_excessive_discount_rate():
    # 100% 초과 할인 테스트 (음수 결과가 나옴)
    customer = Customer(1.2)  # 120% 할인
    result = customer.apply_discount(100)
    assert result == -20


def test_apply_discount_with_zero_amount():
    # 할인 금액이 0인 경우
    customer = Customer(0.1)
    result = customer.apply_discount(0)
    assert result == 0
