# 10.1 조건문 분해하기

_Decompose Conditional_

## 개요

Before

```python
if not a_date.is_before(plan.summer_start) and not a_date.is_after(plan.summer_end):
    charge = quantity * plan.summer_rate
else:
    charge = quantity * plan.regular_rate + plan.regular_service_charge
```

After

```python
if is_summer():
    charge = calculate_summer_charge()
else:
    charge = calculate_regular_charge()
```

## 배경

조건문이 복잡해지는 건 필연적이다. 조건은 다양해지고, 복잡해지고, 동작도 다양해진다.
이를 담는 함수도 커질 뿐더러 그 속의 조건문은 복잡함을 가중시킨다.
이런 코드는 잘 도는 건 알겠는데, 왜 잘돌고 있는지를 바로 파악하기 힘들다.

이런 코드는 부위별로 잘 쪼개고, 해체한 코드덩어리를 함수화한다.
조건문이 보이면 조건식과 조건절에 이 작업을 해주는 것을 권한다.
이러면 해당 조건이 뭔지 강조하고, 뭘 분기한지 명확하게 알 수 있다.

함수화하는 리팩터링 방안은 6.1절이다.

## 절차

1. 조건식과 그 조건식에 딸린 조건절 각각을 함수로 추출(6.1절)

## 예시

로직이 복잡하다면 삼항 연산자보다 그냥 직접 풀어넣는게 직관적인 이해를 도와서 좋은 코드라고 본다.

쉬운 수준의 if/else 에는 도입할 가치가 있다고 보고.