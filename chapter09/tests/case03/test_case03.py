from dataclasses import dataclass

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
