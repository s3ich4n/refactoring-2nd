class TempRange:
    """온도 범위를 나타내는 클래스"""

    def __init__(self, low, high):
        self.low = low
        self.high = high


class Room:
    """방을 나타내는 클래스"""

    def __init__(self, days_temp_range):
        self.days_temp_range = days_temp_range


class HeatingPlan:
    """난방 계획을 나타내는 클래스"""

    def __init__(self, temperature_range):
        self.temperature_range = temperature_range

    def zz_neo_within_range(self, a_number_range: TempRange):
        return (a_number_range.low >= self.temperature_range.low) and (
            a_number_range.high <= self.temperature_range.high
        )


def check_room_temperature(room, plan, alerts):
    """방 온도가 계획의 범위를 벗어났는지 확인하고 경고를 추가"""
    if not plan.zz_neo_within_range(room.days_temp_range):
        alerts.append("room temperature went outside range")
