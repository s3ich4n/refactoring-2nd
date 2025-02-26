class OperationPlan:
    def __init__(self, temperature_min: int, temperature_max: int):
        self.temperature_min: int = temperature_min
        self.temperature_max: int = temperature_max

    def __eq__(self, other):
        return (
            self.temperature_min == other.temperature_min
            and self.temperature_max == other.temperature_max
        )

    def contains(self, value):
        return self.temperature_min <= value <= self.temperature_max


station = {
    "name": "ZB1",
    "readings": [
        {"temp": 47, "time": "2016-11-10 09:10"},
        {"temp": 53, "time": "2016-11-10 09:20"},
        {"temp": 58, "time": "2016-11-10 09:30"},
        {"temp": 53, "time": "2016-11-10 09:40"},
        {"temp": 51, "time": "2016-11-10 09:50"},
    ],
}


def readings_outside_range(station, range=None):
    return [r["temp"] for r in station["readings"] if not range.contains(r["temp"])]
