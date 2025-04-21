from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Show:
    price: int
    properties: Dict[str, Any] = field(default_factory=dict)

    def has_own_property(self, property_name):
        return property_name in self.properties


@dataclass
class Extras:
    premium_fee: int
    properties: Dict[str, Any] = field(default_factory=dict)

    def has_own_property(self, property_name):
        return property_name in self.properties


class Booking:
    def __init__(self, show, date):
        self._show = show
        self._date = date
        self._premium_delegate = None

    def is_peakday(self):
        """날짜가 성수기인지 확인"""
        # 예시로 성수기는 특정 조건에 따라 정해진다고 가정
        return self._date.weekday() >= 5  # 주말(토,일)은 성수기

    def has_talk_back(self):
        """비성수기에 관객과의 대화시간이 있나 점검

        Notes:
            처음 __init__에는 관련 변수를 뺀다
            추후 _be_premium 을 호출하면 위임하는 객체를 추가한다

        """
        return (
            self._premium_delegate.has_talk_back()
            if self._premium_delegate is not None
            else self._show.has_own_property("talkback") and not self.is_peakday()
        )

    def base_price(self):
        return (
            self._premium_delegate.base_price()
            if self._premium_delegate is not None
            else self._private_base_price()
        )

    def _private_base_price(self):
        result = self._show.price
        if self.is_peakday():
            result += round(result * 0.15)
        return result

    def _be_premium(self, extras):
        self._premium_delegate = PremiumBookingDelegate(self, extras)


class PremiumBooking(Booking):
    def __init__(self, show, date, extras):
        super().__init__(show, date)
        self._extras = extras

    def has_dinner(self):
        return self._extras.has_own_property("dinner") and not self.is_peakday()


# 팩토리 함수
def create_booking(show, date):
    return Booking(show, date)


def create_premium_booking(show, date, extras):
    result = PremiumBooking(show, date, extras)
    result._be_premium(extras)
    return result


class PremiumBookingDelegate:
    def __init__(self, host_booking, extras):
        """예약객체로 향하는 역참조(back-reference)를 매개변수로 받음"""
        self._host = host_booking
        self._extras = extras

    def has_talk_back(self):
        """(성수기와 무관) 관객과의 대화시간이 있나 점검"""
        return self._host._show.has_own_property("talkback")

    def base_price(self):
        return round(self._host._private_base_price() + self._extras.premium_fee)
