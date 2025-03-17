def distance_travelled(scenario, time):
    result = calculate_primary_distance(scenario, time)

    if time > scenario.delay:
        result += calculate_secondary_distance(scenario, time)

    return result


def calculate_primary_distance(scenario, primary_time):
    primary_time = min(primary_time, scenario.delay)
    primary_acceleration = scenario.primary_force / scenario.mass
    return 0.5 * primary_acceleration * primary_time * primary_time


def calculate_secondary_distance(scenario, time):
    secondary_time = time - scenario.delay
    primary_acceleration = scenario.primary_force / scenario.mass
    primary_velocity = primary_acceleration * scenario.delay

    secondary_acceleration = (
        scenario.primary_force + scenario.secondary_force
    ) / scenario.mass

    return (
        primary_velocity * secondary_time
        + 0.5 * secondary_acceleration * secondary_time * secondary_time
    )
