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

    def xx_neo_within_range(self, temp_range):
        return (temp_range.low >= self.temperature_range.low) and (
            temp_range.high <= self.temperature_range.high
        )

    def within_range(self, bottom, top):
        """주어진 범위가 계획의 온도 범위 내에 있는지 확인"""
        return


def check_room_temperature(room, plan, alerts):
    """방 온도가 계획의 범위를 벗어났는지 확인하고 경고를 추가"""
    temp_range = room.days_temp_range

    is_within_range = plan.xx_neo_within_range(temp_range)
    if not is_within_range:
        alerts.append("room temperature went outside range")
