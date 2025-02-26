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

    def base_charge(self):
        return base_rate(self._month, self._year) * self._quantity


# 전력 요금을 계산하는 간단한 base_rate 함수 예시
def base_rate(month, year):
    # 월별 기본 요금 (간단한 예시)
    if month in [12, 1, 2]:  # 겨울철
        return 0.8
    elif month in [6, 7, 8]:  # 여름철
        return 0.9
    else:  # 봄/가을
        return 0.7


# 세금 공제 기준액을 계산하는 함수 예시
def tax_threshold(year):
    # 연도별 세금 공제 기준
    thresholds = {2016: 50, 2017: 55, 2018: 60}
    return thresholds.get(year, 45)  # 기본값 45


# 데이터 구조 예시와 acquire_reading 함수
def acquire_reading():
    return {"customer": "ivan", "quantity": 10, "month": 5, "year": 2017}


def calculate_base_charge(a_reading):
    return base_rate(a_reading["month"], a_reading["year"]) * a_reading["quantity"]


# 현재 코드의 AS-IS
reading = {"customer": "ivan", "quantity": 10, "month": 5, "year": 2017}

# 첫 번째 예시: 기본 요금 계산
a_reading = acquire_reading()
base_charge = base_rate(a_reading["month"], a_reading["year"]) * a_reading["quantity"]
# 이 경우: 0.7 * 10 = 7.0

# 두 번째 예시: 과세 대상 요금 계산
a_reading = acquire_reading()
base = base_rate(a_reading["month"], a_reading["year"]) * a_reading["quantity"]
taxable_charge = max(0, base - tax_threshold(a_reading["year"]))
# 이 경우: max(0, 7.0 - 55) = max(0, -48) = 0

# 세 번째 예시: 함수로 분리된 기본 요금 계산
a_reading = acquire_reading()
basic_charge_amount = calculate_base_charge(a_reading)
# 이 경우: 7.0
