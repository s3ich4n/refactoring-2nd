from chapter11.src.case04.case04_2 import (
    TempRange,
    Room,
    HeatingPlan,
    check_room_temperature,
)


def test_within_range_within_limits():
    """온도가 난방 계획 범위 내에 있는 경우 테스트"""
    # Given
    plan_range = TempRange(18, 25)  # 18°C ~ 25°C 범위의 난방 계획
    heating_plan = HeatingPlan(plan_range)

    # When / Then
    # 정확히 범위와 일치
    assert heating_plan.xx_neo_within_range(TempRange(18, 25)) is True
    # 범위 내에 있음
    assert heating_plan.xx_neo_within_range(TempRange(20, 22)) is True


def test_within_range_outside_limits():
    """온도가 난방 계획 범위를 벗어난 경우 테스트"""
    # Given
    plan_range = TempRange(18, 25)  # 18°C ~ 25°C 범위의 난방 계획
    heating_plan = HeatingPlan(plan_range)

    # When / Then
    assert heating_plan.xx_neo_within_range(TempRange(17, 25)) is False  # 하한선 미만
    assert heating_plan.xx_neo_within_range(TempRange(18, 26)) is False  # 상한선 초과
    assert (
        heating_plan.xx_neo_within_range(TempRange(17, 26)) is False
    )  # 양쪽 모두 벗어남


def test_check_room_temperature_within_range():
    """방 온도가 계획 범위 내에 있는 경우 테스트"""
    # Given
    plan_range = TempRange(18, 25)  # 계획 온도 범위
    room_range = TempRange(20, 22)  # 방 온도 범위 (계획 내)

    heating_plan = HeatingPlan(plan_range)
    room = Room(room_range)
    alerts = []

    # When
    check_room_temperature(room, heating_plan, alerts)

    # Then
    assert len(alerts) == 0  # 경고 없음


def test_check_room_temperature_outside_range():
    """방 온도가 계획 범위를 벗어난 경우 테스트"""
    # Given
    plan_range = TempRange(18, 25)  # 계획 온도 범위
    room_range = TempRange(16, 26)  # 방 온도 범위 (계획 벗어남)

    heating_plan = HeatingPlan(plan_range)
    room = Room(room_range)
    alerts = []

    # When
    check_room_temperature(room, heating_plan, alerts)

    # Then
    assert len(alerts) == 1  # 경고 발생
    assert alerts[0] == "room temperature went outside range"


def test_check_room_temperature_edge_case():
    """방 온도가 경계값에 있는 경우 테스트"""
    # Given
    plan_range = TempRange(18, 25)  # 계획 온도 범위
    room_range = TempRange(18, 25)  # 방 온도 범위 (정확히 일치)

    heating_plan = HeatingPlan(plan_range)
    room = Room(room_range)
    alerts = []

    # When
    check_room_temperature(room, heating_plan, alerts)

    # Then
    assert len(alerts) == 0  # 경고 없음 (경계값도 포함)
