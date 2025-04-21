# 11.13 예외를 사전확인으로 바꾸기

_Replace Exception with Precheck_

## 개요

Before

```python
def get_value_for_period(period_number):
    try:
        return values[period_number]
    except IndexError:
        return 0
```

After

```python
def get_value_for_period(period_number):
    return 0 if period_number >= len(values) else values[period_number]
```

## 배경

예외란 개념은 앞서 말한 대로 정말 좋은 개념이지만 남용해선 곤란하다.
책에서도 다시 강조하듯 예외는 말 그대로 '뜻밖의 오류'이므로, 예외적으로 동작할 때만 쓰여야 한다.
함수 수행 시 문제가 될 수 있는 조건을 함수 호출 전에 검사할 수 있다면, 예외를 던지는 대신 호출하는 쪽에서 조건을 검사하도록 해야한다.

## 절차

1. 예외를 유발하는 상황을 검사할 수 있는 조건문을 만든다. `catch` 블록의 코드를 조건문의 조건절 중 하나로 옮기고, 남은 try 블록의 코드를 다른 조건절로 옮긴다.
2. `catch` 블록에 assertion을 추가하고 테스트한다
3. try 문과 catch 블록을 제거한다
4. 테스트한다

## 예시
