import pytest

from chapter11.src.case02.case02 import (
    usd,
    base_charge,
    within_band,
)


def test_usd():
    """USD 변환 테스트"""
    assert usd(1) == 1420
    assert usd(0) == 0
    assert usd(2.5) == 3550


@pytest.mark.parametrize(
    "usage, expected",
    [
        (0, 0),  # 사용량 0
        (-10, 0),  # 음수 사용량
        (50, 50 * 0.03 * 1420),  # 하단 밴드만 사용
        (100, 100 * 0.03 * 1420),  # 하단 밴드 최대 사용
        (150, (100 * 0.03 + 50 * 0.05) * 1420),  # 하단 + 중단 밴드 사용
        (200, (100 * 0.03 + 100 * 0.05) * 1420),  # 하단 + 중단 밴드 최대 사용
        (300, (100 * 0.03 + 100 * 0.05 + 100 * 0.07) * 1420),  # 모든 밴드 사용
    ],
)
def test_base_charge(usage, expected):
    """기본 요금 계산 테스트"""
    assert base_charge(usage) == expected


@pytest.mark.parametrize(
    "usage, expected",
    [
        (0, 0),  # 사용량 0
        (50, 0),  # 중단 밴드 미만
        (100, 0),  # 중단 밴드 시작점
        (150, 50),  # 중단 밴드 내 사용
        (200, 100),  # 중단 밴드 최대치
        (300, 100),  # 중단 밴드 초과
    ],
)
def test_within_band(usage, expected):
    """중단 밴드 계산 테스트"""
    assert within_band(usage, 100, 200) == expected
