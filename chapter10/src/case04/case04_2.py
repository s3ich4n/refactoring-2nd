from dataclasses import dataclass


@dataclass
class Voyage:
    zone: str
    length: int


@dataclass
class HistoryItem:
    zone: str
    profit: float


def rating(voyage, history):
    vpf = voyage_profit_factor(voyage, history)
    vr = voyage_risk(voyage)
    chr = captain_history_risk(voyage, history)
    if vpf * 3 > (vr + chr * 2):
        return "A"
    else:
        return "B"


def voyage_risk(voyage):
    result = 1
    if voyage.length > 4:
        result += 2
    if voyage.length > 8:
        result += voyage.length - 8
    if ["china", "east-indies"].count(voyage.zone) > 0:
        result += 4
    return max(result, 0)


def captain_history_risk(voyage, history):
    result = 1
    if len(history) < 5:
        result += 4
    result += len([v for v in history if v.profit < 0])
    if voyage.zone == "china" and has_china(history):
        result -= 2
    return max(result, 0)


def has_china(history):
    return any(v.zone == "china" for v in history)


def voyage_profit_factor(voyage, history):
    result = 2
    if voyage.zone == "china":
        result += 1
    if voyage.zone == "east-indies":
        result += 1
    if voyage.zone == "china" and has_china(history):
        result += 3
        if len(history) > 10:
            result += 1
        if voyage.length > 12:
            result += 1
        if voyage.length > 18:
            result -= 1
    else:
        if len(history) > 8:
            result += 1
        if voyage.length > 14:
            result -= 1
    return result
