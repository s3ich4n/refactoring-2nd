from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Dict,
    Any,
)


@dataclass(frozen=True)
class Show:
    price: int
    properties: Dict[str, Any] = field(default_factory=dict)

    def has_own_property(self, property_name):
        return property_name in self.properties


@dataclass(frozen=True)
class Extras:
    premium_fee: int
    properties: Dict[str, Any] = field(default_factory=dict)

    def has_own_property(self, property_name):
        return property_name in self.properties


class Booking:
    def __init__(self, show, date):
        self._show = show
        self._date = date

    def is_peakday(self):
        """날짜가 성수기인지 확인"""
        # 예시로 성수기는 특정 조건에 따라 정해진다고 가정
        return self._date.weekday() >= 5  # 주말(토,일)은 성수기

    def has_talk_back(self):
        """비성수기에 관객과의 대화시간이 있나 점검"""
        return self._show.has_own_property("talkback") and not self.is_peakday()

    def base_price(self):
        result = self._show.price
        if self.is_peakday():
            result += round(result * 0.15)
        return result


class PremiumBooking(Booking):
    def __init__(self, show, date, extras):
        super().__init__(show, date)
        self._extras = extras

    def has_talk_back(self):
        """(성수기와 무관) 관객과의 대화시간이 있나 점검"""
        return self._show.has_own_property("talkback")

    def base_price(self):
        return round(super().base_price() + self._extras.premium_fee)

    def has_dinner(self):
        return self._extras.has_own_property("dinner") and not self.is_peakday()


def create_booking(show, date):
    return Booking(show, date)


def create_premium_booking(show, date, extras):
    return PremiumBooking(show, date, extras)


class PremiumBookingDelegate:
    def __init__(self, host_booking, extras):
        """예약객체로 향하는 역참조(back-reference)를 매개변수로 받음"""
        self._host = host_booking
        self._extras = extras
