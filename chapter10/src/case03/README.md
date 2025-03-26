# 10.3 중첩 조건문을 보호 구문으로 바꾸기

_Replace Nested Conditional with Guard Clauses_

## 개요

Before

```python
def get_pay_amount():
    if is_dead:
        result = dead_amount()
    else:
        if is_separated:
            result = separated_amount()
        else:
            if is_retired:
                result = retired_amount()
            else:
                result = normal_pay_amount()
    return result
```

After

```python
def get_pay_amount():
    if is_dead:
        return dead_amount()
    
    if is_separated:
        return separated_amount()
    
    if is_retired:
        return retired_amount()
    
    return normal_pay_amount()
```

## 배경

조건문은 두 타입으로 나뉜다.

1. 참인 경로/거짓인 경로 모두 정상 동작인 형태
2. 한쪽만 정상인 형태

둘은 의도가 다르므로 코드로도 바로 알 수 있어야 한다.
마틴 파울러는 두 경로 모두가 정상동작이라면 if-else 구문을 사용한다.
한쪽만 정상이라면 비정상 조건을 `if` 에서 검사하고, 조건이 참이면(비정상 케이스인 경우) 함수에서 나온다.
이런 검사 형태를 보호 구문(_guard clause_)이라고 한다.

중첩 조건문을 보호 구문으로 바꾸는 리팩터링 기법은 **의도 부각**이다. 위에서 언급한 두 타입에 대해 다시 살펴보자.

1. if-then-else 구조라면 if-else절 두 갈래 모두 중요함을 전달한다.
2. 보호 구문이라면, 이 일이 발생하면 조치를 취한 후 함수를 빠져나옴을 전달한다. 

진입점이 하나인건 동의할만하나 반환점이 하나일 필요는 없다는 뜻을 내비친다. 코드는 명확함이 핵심이다.
반환점이 하나일 때 명확한 코드라면 그렇게 하고, 그게 아니라면 하지 말자.

## 절차

`<br />`, `→` 복사해서 쓰기

1. 교체해야 할 조건 중 가장 바깥의 것을 선택하여 보호구문으로 바꾼다
2. 테스트한다
3. 1~2를 필요한 만큼 반복한다
4. 모든 보호 구문이 같은 결과를 반환한다면 보호 구문들의 조건식을 통합(10.2절)한다

## 예시
