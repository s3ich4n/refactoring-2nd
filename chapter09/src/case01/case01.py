def distance_travelled(scenario, time):
    result = 0
    acc = scenario.primary_force / scenario.mass
    primary_time = min(time, scenario.delay)
    result = 0.5 * acc * primary_time * primary_time

    secondary_time = time - scenario.delay
    if secondary_time > 0:
        primary_velocity = acc * scenario.delay
        acc = (scenario.primary_force + scenario.secondary_force) / scenario.mass
        result += (
                primary_velocity * secondary_time
                + 0.5 * acc * secondary_time * secondary_time
        )

    return result
