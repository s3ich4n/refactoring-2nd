class Reading:
    def __init__(
        self,
        customer: str,
        quantity: int,
        month: int,
        year: int,
    ):
        self._customer = customer
        self._quantity = quantity
        self._month = month
        self._year = year

    @property
    def customer(self):
        return self._customer

    @property
    def quantity(self):
        return self._quantity

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    # 전력 요금을 계산하는 간단한 base_rate 함수 예시
    def base_rate(self):
        # 월별 기본 요금 (간단한 예시)
        if self.month in [12, 1, 2]:  # 겨울철
            return 0.8
        elif self.month in [6, 7, 8]:  # 여름철
            return 0.9
        else:  # 봄/가을
            return 0.7

    # 세금 공제 기준액을 계산하는 함수 예시
    def tax_threshold(self, year):
        # 연도별 세금 공제 기준
        thresholds = {2016: 50, 2017: 55, 2018: 60}
        return thresholds.get(year, 45)  # 기본값 45

    def taxable_charge(self):
        return max(0, int(self.base_charge() - self.tax_threshold(self.year)))

    def base_charge(self):
        return self.base_rate() * self._quantity


# 데이터 구조 예시와 acquire_reading 함수
def acquire_reading():
    return {"customer": "ivan", "quantity": 10, "month": 5, "year": 2017}


def calculate_base_charge(a_reading):
    return base_rate(a_reading["month"], a_reading["year"]) * a_reading["quantity"]
