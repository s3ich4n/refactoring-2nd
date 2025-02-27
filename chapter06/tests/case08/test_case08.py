from src.case08.case08 import readings_outside_range, station, OperationPlan


def test_readings_outside_range():
    plan = OperationPlan(temperature_min=45, temperature_max=55)
    assert readings_outside_range(station, plan) == [58]


def test_operation_plan_equality():
    plan1 = OperationPlan(temperature_min=45, temperature_max=55)
    plan2 = OperationPlan(temperature_min=45, temperature_max=55)
    plan3 = OperationPlan(temperature_min=45, temperature_max=57)

    assert plan1 == plan2
    assert plan2 != plan3
