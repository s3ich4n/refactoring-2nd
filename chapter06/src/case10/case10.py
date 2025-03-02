from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Reading:
    customer: str
    quantity: int
    month: int
    year: int


# 데이터 구조 예시와 acquire_reading 함수
def acquire_reading():
    return Reading(**{"customer": "ivan", "quantity": 10, "month": 5, "year": 2017})


def calculate_base_charge(a_reading: Reading):
    return base_rate(a_reading.month, a_reading.year) * a_reading.quantity


def tax_threshold(year):
    # 연도별 세금 공제 기준
    thresholds = {2016: 50, 2017: 55, 2018: 60}
    return thresholds.get(year, 45)  # 기본값 45


def base_rate(month, year):
    # 월별 기본 요금 (간단한 예시)
    if year % 10 == 0:
        if month in [12, 1, 2]:  # 겨울철
            return 0.8
        elif month in [6, 7, 8]:  # 여름철
            return 0.9
        else:  # 봄/가을
            return 0.7
    else:
        return 0.5


# 입력 객체를 그대로 복사해 반환하는 변환함수(enrich) 를 만듦.
#   본질을 같고 부가 정보만 덧붙이는 변환함수
def enrich_reading(original):
    result = deepcopy(original)

    # 여기서부턴 내 입맛대로 데이터를 바꿀 수 있음. 카피한 값이니까

    # 기본 소비량을 부가 정보로 덧붙임(enriching)
    result.base_charge = calculate_base_charge(result)
    result.taxable_charge = max(0, int(result.base_charge - tax_threshold(result.year)))
    return result
