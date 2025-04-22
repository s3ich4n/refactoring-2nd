import pytest

from chapter08.src.case01.case01_2 import (
    Account,
    AccountType,
)


# 각 테스트에서 사용할 계좌 객체들을 생성하는 픽스처
@pytest.fixture
def normal_account():
    return Account(AccountType(is_premium=False), 5)


@pytest.fixture
def premium_account_within_limit():
    return Account(AccountType(is_premium=True), 5)


@pytest.fixture
def premium_account_beyond_limit():
    return Account(AccountType(is_premium=True), 10)


@pytest.fixture
def account_without_overdraft():
    return Account(AccountType(is_premium=False), 0)


# 테스트 함수들
def test_bank_charge_without_overdraft(account_without_overdraft):
    # 초과 인출이 없는 일반 계좌
    assert account_without_overdraft.bank_charge == 4.5


def test_bank_charge_with_overdraft_normal(normal_account):
    # 초과 인출이 있는 일반 계좌
    expected = 4.5 + (5 * 1.75)  # 기본 요금 + 초과 인출 요금
    assert normal_account.bank_charge == expected


def test_bank_charge_with_overdraft_premium_within_limit(premium_account_within_limit):
    # 7일 이하 초과 인출이 있는 프리미엄 계좌
    expected = 4.5 + 10  # 기본 요금 + 프리미엄 초과 인출 기본 요금
    assert premium_account_within_limit.bank_charge == expected


def test_bank_charge_with_overdraft_premium_beyond_limit(premium_account_beyond_limit):
    # 7일 초과 인출이 있는 프리미엄 계좌
    expected = (
        4.5 + 10 + (10 - 7) * 0.85
    )  # 기본 요금 + 프리미엄 초과 인출 기본 요금 + 추가 일수 요금
    assert premium_account_beyond_limit.bank_charge == expected


def test_overdraft_charge_normal(normal_account):
    # 일반 계좌의 초과 인출 요금
    assert normal_account.overdraft_charge == 5 * 1.75


def test_overdraft_charge_premium_within_limit(premium_account_within_limit):
    # 7일 이하 초과 인출의 프리미엄 계좌 요금
    assert premium_account_within_limit.overdraft_charge == 10


def test_overdraft_charge_premium_beyond_limit(premium_account_beyond_limit):
    # 7일 초과 인출의 프리미엄 계좌 요금
    assert premium_account_beyond_limit.overdraft_charge == 10 + (10 - 7) * 0.85
