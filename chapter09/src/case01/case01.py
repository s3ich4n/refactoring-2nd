def distance_travelled(scenario, time):
    result = 0
    primary_acceleration = scenario.primary_force / scenario.mass
    primary_time = min(time, scenario.delay)
    result = 0.5 * primary_acceleration * primary_time * primary_time

    secondary_time = time - scenario.delay
    if secondary_time > 0:
        primary_velocity = primary_acceleration * scenario.delay
        acc = (scenario.primary_force + scenario.secondary_force) / scenario.mass   # 두번째 대입 전까지
        result += (
            primary_velocity * secondary_time
            + 0.5 * acc * secondary_time * secondary_time
        )

    return result
