from src.case08.case08 import readings_outside_range, station, OperationPlan


def test_readings_outside_range():
    plan = OperationPlan(
        temperature_floor=45,
        temperature_ceiling=55,
    )
    assert readings_outside_range(
        station, plan.temperature_floor, plan.temperature_ceiling
    ) == [58]
