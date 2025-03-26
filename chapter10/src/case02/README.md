# 10.2 조건식 통합하기

_Consolidate Conditional Expression_

## 개요

Before

```python
if an_employee.seniority < 2:
    return 0
if an_employee.months_disabled > 12:
    return 0
if an_employee.is_part_time:
    return 0
```

After

```python
def is_not_eligible_for_disability(an_employee):
    return (
        (an_employee.seniority < 2)
        or (an_employee.months_disabled > 12)
        or (an_employee.is_part_time)
    )

if is_not_eligible_for_disability(an_employee):
    return 0
```

## 배경

이 케이스는 비교하는 조건은 다르지만 그 결과로 수행하는 동작이 동일한 코드를 다듬는 방법이다.
이럴거면 조건검사도 하나로 비교해서 함수로 합친 후, `and`, `or` 로 감싸주는 게 더 낫다.

이런 코드는 두 가지 장점을 가진다:
1. 하려는 일이 명확해진다
2. 이 리팩터링이 잘 되면 함수 추출하기(6.1절)로 쉽게 이어질 수 있다. 이러면 코드가 매우 명확해진다.

함수 추출하기를 하면 "무엇을" 하는지 포함하기도 쉽고 "왜" 하는지도 쉽게 풀 수 있다.

> ![CAUTION]
> 진짜 독립된 검사를 해야한다면 이 리팩터링을 쓰면 안 된다.
> 
> 그건 진짜로 나눠야하는 케이스니까.

## 절차

1. 해당 조건식들에 사이드 이펙트가 없나 확인한다. <br />
→ 사이드 이펙트가 있는 조건식은 질의 함수와 변경 함수 분리하기(11.1절) 부터 적용한다.
2. 조건문 두 개를 선택해서, 두 조건문의 조건식을 논리 연산자로 결합한다. <br />
→ 순차적으로 이뤄지는 조건문은 `or` 로 결합하고, 중첩된 조건문은 `and` 로 결합한다.
3. 테스트한다
4. 조건이 하나만 남을 때 까지 2, 3을 반복한다
5. 하나로 합쳐진 조건식을 함수로 추출(6.1절)할지 고민한다.

## 예시
