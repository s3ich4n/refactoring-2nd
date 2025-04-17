# 12.4 메소드 내리기

_Push Down Method_

## 개요

Before

```python
class Employee:
    def quota(self):
        ...


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
    def quota(self):
        ...
```

> [!TIP]
> 반대 리팩터링: 메소드 올리기 (12.1절)

## 배경

특정 서브클래스 하나(혹은 소수)와 연관된 메소드는 슈퍼클래스에서 빼고 직접 서브클래스에 추가하는게 더 깔끔하다.
근데 이 시도는 서프클래스가 정확히 무엇인지 호출자가 알고있을 때만 적용할 수 있다.
그렇지 못한 상황이라면 서브클래스에 따라 다르게 동작하는 슈퍼클래스의 기만적인 조건부 로직을 다형성으로 바꿔야(10.4절)한다

## 절차

1. 대상 메소드를 모든 서브클래스에 복사한다
2. 슈퍼클래스에서 그 메소드를 제거한다
3. 테스트한다
4. 이 메소드를 쓰지 않는 모든 서브클래스에서 제거한다
5. 테스트한다

## 예시
