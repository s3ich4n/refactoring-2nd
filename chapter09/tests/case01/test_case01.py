from dataclasses import dataclass

import pytest

from chapter09.src.case01.case01 import distance_travelled


@dataclass
class Scenario:
    primary_force: float
    secondary_force: float
    mass: float
    delay: float


def test_distance_travelled():
    # 테스트 시나리오 설정
    scenario = Scenario(primary_force=10.0, secondary_force=5.0, mass=2.0, delay=5.0)

    # 시간이 지연 시간보다 작은 경우
    assert distance_travelled(scenario, 3.0) == 0.5 * (10.0 / 2.0) * 3.0 * 3.0

    # 시간이 지연 시간보다 큰 경우
    time = 10.0
    primary_time = 5.0
    secondary_time = time - primary_time
    acc1 = 10.0 / 2.0
    primary_result = 0.5 * acc1 * primary_time * primary_time
    primary_velocity = acc1 * primary_time
    acc2 = (10.0 + 5.0) / 2.0
    secondary_result = (
            primary_velocity * secondary_time + 0.5 * acc2 * secondary_time * secondary_time
    )

    assert distance_travelled(scenario, time) == pytest.approx(
        primary_result + secondary_result
    )

    # 시간이 정확히 지연 시간과 같은 경우
    assert distance_travelled(scenario, 5.0) == 0.5 * (10.0 / 2.0) * 5.0 * 5.0
