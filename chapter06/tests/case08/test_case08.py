from src.case08.case08 import readings_outside_range, station, OperationPlan


def test_readings_outside_range():
    plan = OperationPlan(min=45, max=55)
    assert readings_outside_range(station, plan) == [58]
