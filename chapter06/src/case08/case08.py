from dataclasses import dataclass


@dataclass
class OperationPlan:
    min: int
    max: int

    def contains(self, value):
        return self.min <= value <= self.max


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
