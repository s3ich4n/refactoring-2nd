# 12.5 필드 내리기

_Push Down Field_

## 개요

Before

```python
class Employee:
    def __init__(self):
        self._quota = "12.5. Push Down Field"

class Engineer(Employee):
    ...

class Salesperson(Employee):
    ...
```

After

```python
class Employee:
    ...

class Engineer(Employee):
    ...

class Salesperson(Employee):
    def __init__(self):
        self._quota = "12.5. Push Down Field"
```

> [!TIP]
> 반대 리팩터링: 필드 올리기 (12.2절)

## 배경

서브클래스 하나(혹은 소수)에만 쓰는 필드는 해당 서브클래스로 옮긴다.

## 절차

`<br />`, `→` 복사해서 쓰기

1. 대상 필드를 모든 서브클래스에 정의한다
2. 슈퍼클래스에서 그 필드를 제거한다
3. 테스트한다
4. 이 필드를 쓰지 않는 모든 서브클래스에서 제거한다
5. 테스트한다

## 예시
