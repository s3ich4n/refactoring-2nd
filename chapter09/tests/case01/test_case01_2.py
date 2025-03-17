import pytest

from chapter09.src.case01.case01_2 import discount


@pytest.mark.parametrize(
    "input_value, quantity, expected",
    [
        # 기본 케이스: 할인 없음
        (50, 100, 50),
        # 첫 번째 조건만 만족: input_value > 50
        (60, 50, 58),
        # 두 번째 조건만 만족: quantity > 100
        (40, 150, 39),
        # 두 조건 모두 만족
        (70, 200, 67),
        # 경계값 테스트
        (51, 101, 48),  # 두 조건 경계값 약간 초과
        (50, 101, 49),  # 첫 번째 조건 경계값과 같음
        (51, 100, 49),  # 두 번째 조건 경계값과 같음
    ],
)
def test_discount(input_value, quantity, expected):
    assert discount(input_value, quantity) == expected
