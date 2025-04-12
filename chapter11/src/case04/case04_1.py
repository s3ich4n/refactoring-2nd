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

    def neo_within_range(self, a_number_range: TempRange): ...

    def within_range(self, bottom, top):
        """주어진 범위가 계획의 온도 범위 내에 있는지 확인"""
        return (bottom >= self.temperature_range.low) and (
            top <= self.temperature_range.high
        )


def check_room_temperature(room, plan, alerts):
    """방 온도가 계획의 범위를 벗어났는지 확인하고 경고를 추가"""
    low = room.days_temp_range.low
    high = room.days_temp_range.high
    if not plan.within_range(low, high):
        alerts.append("room temperature went outside range")
