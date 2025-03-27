from dataclasses import dataclass


@dataclass
class Voyage:
    zone: str
    length: int


@dataclass
class HistoryItem:
    zone: str
    profit: float


class Rating:
    def __init__(
        self,
        voyage: Voyage,
        history: list[HistoryItem] | None = None,
    ):
        self.voyage = voyage
        self.history = history

    def value(self):
        vpf = self.voyage_profit_factor()
        vr = self.voyage_risk()
        chr = self.captain_history_risk()
        if vpf * 3 > (vr + chr * 2):
            return "A"
        else:
            return "B"

    def voyage_profit_factor(self):
        result = 2
        if self.voyage.zone == "china":
            result += 1
        if self.voyage.zone == "east-indies":
            result += 1
        result += self.history_length_factor()
        result += self.voyage_length_factor()
        return result

    def voyage_risk(self):
        result = 1
        if self.voyage.length > 4:
            result += 2
        if self.voyage.length > 8:
            result += self.voyage.length - 8
        if ["china", "east-indies"].count(self.voyage.zone) > 0:
            result += 4
        return max(result, 0)

    def captain_history_risk(self):
        result = 1
        if len(self.history) < 5:
            result += 4
        result += len([v for v in self.history if v.profit < 0])
        return max(result, 0)

    def has_china_history(self):
        return any(v.zone == "china" for v in self.history)

    def history_length_factor(self):
        return 1 if len(self.history) > 8 else 0

    def voyage_length_factor(self):
        return -1 if self.voyage.length > 14 else 0


class ExperiencedChinaRating(Rating):
    def voyage_profit_factor(self):
        return super().voyage_profit_factor() + 3

    def captain_history_risk(self):
        result = super().captain_history_risk() - 2
        return max(result, 0)

    def voyage_length_factor(self):
        result = 0

        if self.voyage.length > 12:
            result += 1
        if self.voyage.length > 18:
            result -= 1

        return result

    def history_length_factor(self):
        return 1 if len(self.history) > 10 else 0


def rating(voyage, history):
    return create_rating(voyage, history).value()


def create_rating(voyage, history):
    if voyage.zone == "china" and any(v.zone == "china" for v in history):
        return ExperiencedChinaRating(voyage, history)

    return Rating(voyage, history)
