from dataclasses import dataclass

import pytest

from chapter09.src.case03.case03 import SomeClass


@dataclass
class Adjustment:
    amount: float


def test_production_adjustment():
    # 테스트 설정
    item = SomeClass()

    # 초기 상태 확인
    assert item.production == 0
    assert len(item._adjustments) == 0

    # 조정 적용
    adjustment1 = Adjustment(amount=10)
    item.apply_adjustment(adjustment1)

    # 결과 확인
    assert item.production == 10
    assert len(item._adjustments) == 1
    assert item._adjustments[0] == adjustment1

    # 추가 조정 적용
    adjustment2 = Adjustment(amount=-5)
    item.apply_adjustment(adjustment2)

    # 최종 결과 확인
    assert item.production == 5
    assert len(item._adjustments) == 2
    assert item._adjustments[1] == adjustment2


def test_production_calculation():
    # 테스트 설정
    item = SomeClass()

    # 초기 상태 확인
    assert item.calculated_production == 0

    # 조정 추가
    item._adjustments.append(Adjustment(amount=10))
    item._adjustments.append(Adjustment(amount=5))
    item._production = 15  # 수동으로 _production 설정

    # 테스트 - 생산량과 계산된 생산량이 일치
    assert item.production == 15

    # 테스트 - 불일치 상황
    item._production = 20  # 계산된 값과 불일치하게 변경
    with pytest.raises(AssertionError):
        item.production  # AssertionError 발생 예상
